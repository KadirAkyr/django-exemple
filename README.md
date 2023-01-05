﻿# django-exemple
 ## Create virtualenv
  ### Windows
- pip install virtualenv 
- python -m venv .venv                                                                          
- .\\.venv\Scripts\activate
  
  ### Mac
- pipx install virtualenv
- virtualenv venv 
- source venv/bin/activate

 ## Install packages
- pip install -r requirements.txt

## Config then run server
- python manage.py createsuperuser
- python manage.py runserver
