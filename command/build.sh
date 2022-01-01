#!/bin/bash


set -o errexit
set -o pipefail
set -o nounset


pip install -r requirements/prod.txt
python manage.py migrate
