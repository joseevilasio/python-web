#!/usr/bin/env bash

set -e

 python manage.py migrate --noinput
 python manage.py createsuperuser --username=admin --email=admin@example.com

$@
