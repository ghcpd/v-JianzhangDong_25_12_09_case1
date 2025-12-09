#!/usr/bin/env python
"""
auto_test.py - Automated test runner with environment detection

This script:
1. Detects the Python version and virtual environment
2. Discovers all test files in the tests/ directory
3. Runs them and logs results to logs/test_run.log
4. Provides detailed error reporting
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

def setup_logging():
    """Create logs directory and setup logging"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir / "test_run.log"

def get_environment_info():
    """Gather environment information"""
    info = {
        "python_version": sys.version,
        "python_executable": sys.executable,
        "virtual_env": os.environ.get("VIRTUAL_ENV", "None"),
        "working_directory": os.getcwd(),
        "timestamp": datetime.datetime.now().isoformat()
    }
    return info

def discover_tests():
    """Discover all test files in the tests/ directory"""
    tests_dir = Path("tests")
    if not tests_dir.exists():
        return []
    
    test_files = sorted(tests_dir.glob("case_*.py"))
    return test_files

def run_test(test_file, log_file):
    """Run a single test file and log results"""
    print(f"\n{'='*60}")
    print(f"Running: {test_file.name}")
    print(f"{'='*60}")
    
    try:
        # Run the test with proper PYTHONPATH to include the project root
        env = os.environ.copy()
        env['PYTHONPATH'] = os.getcwd()
        
        # Run the test
        result = subprocess.run(
            [sys.executable, str(test_file)],
            capture_output=True,
            text=True,
            timeout=30,
            env=env
        )
        
        success = result.returncode == 0
        output = result.stdout
        error = result.stderr
        
        # Log to file
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Test: {test_file.name}\n")
            f.write(f"Status: {'PASSED' if success else 'FAILED'}\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
            f.write(f"Return Code: {result.returncode}\n")
            f.write(f"{'='*60}\n")
            
            if output:
                f.write(f"\nOutput:\n{output}\n")
            if error:
                f.write(f"\nErrors:\n{error}\n")
        
        # Print to console
        if success:
            print(f"✓ PASSED")
            if output:
                print(f"Output:\n{output}")
        else:
            print(f"✗ FAILED")
            if error:
                print(f"Error:\n{error}")
            if output:
                print(f"Output:\n{output}")
        
        return success
    
    except subprocess.TimeoutExpired:
        error_msg = f"Test timed out after 30 seconds"
        print(f"✗ TIMEOUT: {error_msg}")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Test: {test_file.name}\n")
            f.write(f"Status: TIMEOUT\n")
            f.write(f"Error: {error_msg}\n")
        return False
    
    except Exception as e:
        error_msg = f"Exception occurred: {str(e)}"
        print(f"✗ ERROR: {error_msg}")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Test: {test_file.name}\n")
            f.write(f"Status: ERROR\n")
            f.write(f"Error: {error_msg}\n")
        return False

def main():
    """Main test execution function"""
    # Setup
    log_file = setup_logging()
    env_info = get_environment_info()
    test_files = discover_tests()
    
    # Write header to log
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("AUTOMATED TEST RUN LOG\n")
        f.write("=" * 60 + "\n\n")
        f.write("Environment Information:\n")
        f.write("-" * 60 + "\n")
        for key, value in env_info.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")
    
    # Print header to console
    print("=" * 60)
    print("AUTOMATED TEST RUN")
    print("=" * 60)
    print("\nEnvironment Information:")
    for key, value in env_info.items():
        print(f"  {key}: {value}")
    
    # Discover tests
    print(f"\nDiscovered {len(test_files)} test files:")
    for test_file in test_files:
        print(f"  - {test_file.name}")
    
    if not test_files:
        print("\nNo test files found in tests/ directory!")
        return 1
    
    # Run tests
    print("\n" + "=" * 60)
    print("RUNNING TESTS")
    print("=" * 60)
    
    results = []
    for test_file in test_files:
        success = run_test(test_file, log_file)
        results.append((test_file.name, success))
    
    # Summary
    passed = sum(1 for _, success in results if success)
    failed = len(results) - passed
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    # Write summary to log
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write("TEST SUMMARY\n")
        f.write("=" * 60 + "\n")
        f.write(f"Total Tests: {len(results)}\n")
        f.write(f"Passed: {passed}\n")
        f.write(f"Failed: {failed}\n")
        f.write(f"Success Rate: {(passed/len(results)*100):.1f}%\n")
    
    print(f"Success Rate: {(passed/len(results)*100):.1f}%")
    print(f"\nLog file: {log_file.absolute()}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
