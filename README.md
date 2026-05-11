# Python Admin Panel

A small Django 5.2 project with a custom `accounts` app and a custom user model.

## Features

- Django admin enabled
- Custom user model with an optional `phone` field
- Basic CRUD-style user functions in the `accounts` app
- SQLite database for local development

## Project Structure

- `myproject/manage.py` - Django management entry point
- `myproject/myproject/` - Project settings and URL configuration
- `myproject/accounts/` - Custom user app
- `myproject/db.sqlite3` - Local SQLite database

## Requirements

- Python 3.10+
- Django 5.2+

## Setup

1. Create and activate a virtual environment.
2. Install Django:

   ```bash
   pip install django
   ```

3. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Routes

- `/` - Home page check that returns `Home Page Working`
- `/admin/` - Django admin site
- `/accounts/create/` - Creates a sample user
- `/accounts/list/` - Returns all users

## Custom User Model

This project uses:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

The custom user model extends Django's built-in user and adds:

- `phone` - optional text field

## Notes

- The project uses SQLite by default.
- The current `accounts` views are simple function-based CRUD examples and are not yet wired to templates or JSON responses.
- If you delete `db.sqlite3`, run migrations again before starting the server.

## Example Workflow

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
