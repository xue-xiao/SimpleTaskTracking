#!/bin/bash

# Need to add NGINX or ALB to the front of 5000 so that request is buffered
# Configure ./instance/prod_config.py with the correct database URL.

gunicorn -w 2 -k gevent -b 0.0.0.0:5000 "app:create_app(stage='prod')"
