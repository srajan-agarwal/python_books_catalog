source .venv/bin/activate
.venv/bin/pip install --upgrade pip setuptools wheel
.venv/bin/pip -V
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -r test_requirements.txt
.venv/bin/pip install --upgrade pysqlite3
deactivate
