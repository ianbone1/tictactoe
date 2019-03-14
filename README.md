##Description
This is a game of Tic-Tac-Toe.

This project is written in Python, and uses django to handle user interation.
It also uses django-crispy-forms to tidy up the input forms. The application is the result of training thru CodeClan and thru PluralSight.
 
### Setup
Ensure Python3 is installed.

Create a directory for the virtual environment.

Change into the directory and setup a virtual environment:
```
python3 -m venv project_name
cd project_name
. bin/activate
pip install django
pip install django-crispy-forms
mkdir tictactoe
cd tictactoe
git init
git pull git@github.com:ianbone1/tictactoe.git
```

To run the applications
```buildoutcfg
python manage.py runserver 
```
Point your browser at:

http://localhost:8000



