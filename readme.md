## 1. Rename the project:

### python manage.py rename_project <Current project_name> <New project_name>

## 2. Rename the app:

### python manage.py rename_app <Current project_name> <Current app_name> <New app_name>

## To delete the migration files

### `find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`

### `find . -path "*/*.pyc" -delete`

### `rm -f db.sqlite3`

### `find . -path "*/__pycache__" -delete`

## Fourcefully remove previous commit from local and remote

### `git reset HEAD^` # remove commit locally

### `git push origin` +HEAD # force-push the new HEAD commit
