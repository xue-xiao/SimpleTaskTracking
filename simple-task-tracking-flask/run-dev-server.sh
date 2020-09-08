#!/bin/bash

export FLASK_APP=app
export FLASK_ENV=development

# listen on all incoming IP
flask run --host=0.0.0.0
