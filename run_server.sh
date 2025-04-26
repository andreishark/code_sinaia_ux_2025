#!/bin/bash

. ./activate_venv.sh
flask --app ./flask_app.py run -p 3000 
