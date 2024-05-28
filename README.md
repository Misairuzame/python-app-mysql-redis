# Applicazione Python Flask + Mysql + Redis cache
"Fork" di https://github.com/paulmchen/employee-flaskpythonapp

Python web app example (with Flask web framework) - employee app + mysql db + Redis cache

Tutte le configurazioni necessarie si possono specificare in `loadconfig.py`.

## Container MySQL
docker run --rm --name my-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=PASSWORD_MYSQL -d mysql
