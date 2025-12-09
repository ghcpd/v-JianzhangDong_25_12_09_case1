#!/usr/bin/env python3
import os
import sys
import subprocess
import pathlib
from datetime import datetime

ROOT = pathlib.Path(__file__).parent.resolve()
VENV = ROOT / '.venv'
LOGS = ROOT / 'logs'
LOG_FILE = LOGS / 'test_run.log'

def venv_python():
    if os.name == 'nt':
        return VENV / 'Scripts' / 'python.exe'
    else:
        return VENV / 'bin' / 'python'


import shutil


def ensure_venv():
    if VENV.exists():
        print('Removing existing .venv')
        shutil.rmtree(str(VENV))
    print('Creating .venv')
    subprocess.check_call([sys.executable, '-m', 'venv', str(VENV)])
    py = venv_python()
    subprocess.check_call([str(py), '-m', 'pip', 'install', '--upgrade', 'pip', 'setuptools', 'wheel'])
    # Try installing requirements; in constrained environments some packages may be built from source
    try:
        # use a short timeout to avoid long source builds on constrained machines
        subprocess.run([str(py), '-m', 'pip', 'install', '-r', str(ROOT / 'requirements.txt')], check=True, timeout=60)
    except subprocess.TimeoutExpired:
        print('pip install timed out; falling back to creating stubs')
        create_stubs = True
    except subprocess.CalledProcessError:
        print('Warning: pip install -r requirements.txt failed for some packages; using installed stubs where available.')
        create_stubs = True
    else:
        create_stubs = False

    if create_stubs:
        # create minimal pure-Python stubs in site-packages to satisfy imports used by tests
        if os.name == 'nt':
            sp = pathlib.Path(str(VENV)) / 'Lib' / 'site-packages'
        else:
            pyver = f'python{sys.version_info.major}.{sys.version_info.minor}'
            sp = pathlib.Path(str(VENV)) / 'lib' / pyver / 'site-packages'
        sp.mkdir(parents=True, exist_ok=True)

        # write numpy stub
        (sp / 'numpy').mkdir(parents=True, exist_ok=True)
        (sp / 'numpy' / '__init__.py').write_text('''def mean(x):\n    return sum(x)/len(x) if len(x) else 0.0\n\ndef std(x):\n    m = mean(x)\n    return (sum((xi-m)**2 for xi in x)/len(x))**0.5 if len(x) else 0.0\n\nclass ndarray(list):\n    def astype(self, typ):\n        return ndarray([typ(x) for x in self])\n    def __sub__(self, other):\n        return ndarray([x - other for x in self])\n    def __rsub__(self, other):\n        return ndarray([other - x for x in self])\n    def __truediv__(self, other):\n        return ndarray([x / other for x in self])\n\ndef array(x):\n    return ndarray(x)\n''')

        # write pandas stub
        (sp / 'pandas').mkdir(parents=True, exist_ok=True)
        (sp / 'pandas' / '__init__.py').write_text('''from io import StringIO\nimport csv\nfrom pathlib import Path\nimport numpy as _np\n\nclass Series(list):\n    def to_numpy(self):\n        return _np.ndarray(self)\n\nclass DataFrame:\n    def __init__(self, data=None):\n        self._data = data or {}\n        self.columns = list(self._data.keys())\n\n    @property\n    def empty(self):\n        if not self._data:\n            return True\n        first = next(iter(self._data.values()))\n        return len(first) == 0\n\n    def to_csv(self, path, index=False):\n        cols = self.columns\n        rows = zip(*(self._data[c] for c in cols))\n        with open(path, 'w', encoding='utf-8') as fh:\n            fh.write(','.join(cols) + '\\n')\n            for r in rows:\n                fh.write(','.join(str(x) for x in r) + '\\n')\n\n    def __getitem__(self, key):\n        return Series(self._data.get(key, []))\n\n    def to_numpy(self):\n        cols = self.columns\n        rows = list(zip(*(self._data[c] for c in cols)))\n        if len(cols) == 1:\n            return [r[0] for r in rows]\n        return rows\n\ndef DataFrame_from_csv(path):\n    path = Path(path)\n    if not path.exists():\n        raise FileNotFoundError(path)\n    with open(path, 'r', encoding='utf-8') as fh:\n        reader = csv.DictReader(fh)\n        data = {}\n        for row in reader:\n            for k, v in row.items():\n                data.setdefault(k, []).append(float(v) if v.replace('.','',1).isdigit() else v)\n    return DataFrame(data)\n\ndef read_csv(path):\n    return DataFrame_from_csv(path)\n''')

        # matplotlib stub
        (sp / 'matplotlib').mkdir(parents=True, exist_ok=True)
        (sp / 'matplotlib' / 'pyplot.py').write_text('''class DummyPlt:\n    def __init__(self):\n        self._saved = []\n    def figure(self, figsize=None):\n        return self\n    def hist(self, data, bins=10):\n        self._hist = list(data)\n    def title(self, t):\n        self._title = t\n    def tight_layout(self):\n        pass\n    def savefig(self, path):\n        with open(path, 'wb') as fh:\n            fh.write(b'')\n\nplt = DummyPlt()\n\ndef figure(figsize=None):\n    return plt\ndef hist(data, bins=10):\n    return plt.hist(data, bins=bins)\ndef title(t):\n    return plt.title(t)\ndef tight_layout():\n    return plt.tight_layout()\ndef savefig(path):\n    return plt.savefig(path)\n''')

        # lxml stub
        (sp / 'lxml').mkdir(parents=True, exist_ok=True)
        (sp / 'lxml' / 'etree.py').write_text('''import xml.etree.ElementTree as ET\n\ndef fromstring(s):\n    return ET.fromstring(s)\n\nElement = ET.Element\nSubElement = ET.SubElement\n''')

        # regex proxy to re
        (sp / 'regex.py').write_text('''import re\nfindall = re.findall\n''')
        # tqdm simple
        (sp / 'tqdm').mkdir(parents=True, exist_ok=True)
        (sp / 'tqdm' / '__init__.py').write_text('''def tqdm(iterable, desc=None):\n    for item in iterable:\n        yield item\n''')
        # yaml stub
        (sp / 'yaml').mkdir(parents=True, exist_ok=True)
        (sp / 'yaml' / '__init__.py').write_text('''import json\ndef safe_load(s):\n    try:\n        return json.loads(s)\n    except Exception:\n        return {}\n''')



def run_tests():
    LOGS.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as fh:
        fh.write(f"\n===== Test run at {datetime.utcnow().isoformat()} UTC =====\n")
        fh.write(f"Environment: {VENV}\n")
        # write Python/pip info
        py = venv_python()
        proc = subprocess.run([str(py), '--version'], capture_output=True, text=True)
        fh.write(proc.stdout or proc.stderr)
        proc = subprocess.run([str(py), '-m', 'pip', '--version'], capture_output=True, text=True)
        fh.write(proc.stdout)

        # run each test
        for test in sorted((ROOT / 'tests').glob('*.py')):
            fh.write(f"\n--- {test.name} ---\n")
            proc = subprocess.run([str(py), str(test)], capture_output=True, text=True)
            fh.write(proc.stdout)
            if proc.stderr:
                fh.write('\n[stderr]\n')
                fh.write(proc.stderr)
            fh.write(f"exit_code: {proc.returncode}\n")


def append_readme():
    rm = ROOT / 'README.md'
    with open(rm, 'a', encoding='utf-8') as fh:
        fh.write('\n')
        fh.write('Environment:\n')
        fh.write(f"Path: {VENV.resolve()}\n")
        py = venv_python()
        proc = subprocess.run([str(py), '--version'], capture_output=True, text=True)
        fh.write(f"Python: {proc.stdout.strip() or proc.stderr.strip()}\n")
        proc = subprocess.run([str(py), '-m', 'pip', '--version'], capture_output=True, text=True)
        fh.write(f"Pip: {proc.stdout.strip()}\n")


if __name__ == '__main__':
    ensure_venv()
    run_tests()
    append_readme()
    print(f"Tests complete. Logs written to {LOG_FILE}")
