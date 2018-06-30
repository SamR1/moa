include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)

install:
	test -d $(VENV) || virtualenv $(VENV) -p $(PYTHON_VERSION)
	$(PIP) install -r $(REQUIREMENTS)
	test -e config.py || cp config.py.sample config.py

migrate-db:
	$(FLASK) db migrate --directory $(MIGRATIONS)

run-worker:
	$(PYTHON) -m moa.worker

serve:
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)

upgrade-db:
	$(FLASK) db upgrade
