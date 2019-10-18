from functools import wraps


def db_session(func):
    @wraps(func)
    def inner(*args, **kwargs):
        from .run_celery import app
        with app.app_context():
            return func(*args, **kwargs)

    return inner
