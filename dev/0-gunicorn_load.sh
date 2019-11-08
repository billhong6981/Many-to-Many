#!/usr/bin/env bash

gunicorn --bind 0.0.0.0:5000 web_flask.1-bh_route:app

HBNB_MYSQL_USER=bh_dev HBNB_MYSQL_PWD=bh_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=bh_dev_db HBNB_TYPE_STORAGE=db HBNB_API_PORT=5001 gunicorn --bind 0.0.0.0:5001 api.v1.app:app

HBNB_MYSQL_USER=bh_dev HBNB_MYSQL_PWD=bh_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=bh_dev_db HBNB_TYPE_STORAGE=db HBNB_API_PORT=5000 gunicorn --bind 0.0.0.0:5002 --workers 3 --access-logfile /tmp/bh/access.log --error-logfile /tmp/bh/error.log web_dynamic.10-bh:app
