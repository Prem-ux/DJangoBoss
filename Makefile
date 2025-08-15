run-django:
\tpython manage.py runserver

run-flask
\tcd flaskapp && source ../.venv/bin/activate && python app.py

test-flask:
\thttp :5001/health
\thttp POST :5001/echo hello=world
