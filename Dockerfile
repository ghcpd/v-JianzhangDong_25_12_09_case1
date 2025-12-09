FROM python:3.14-slim

WORKDIR /app

# keep pip up-to-date
RUN python -m pip install --upgrade pip setuptools wheel

# copy pinned requirements and install into a virtual environment
COPY requirements.txt /app/requirements.txt

# create a venv inside container for isolation
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

ENV PATH="/opt/venv/bin:$PATH"

CMD ["/bin/sh","-c","./run_test.sh"]
