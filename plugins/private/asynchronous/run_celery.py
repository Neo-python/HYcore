from init import create_app, celery

app = create_app()
app.app_context().push()
celery.conf.enable_utc = False
celery.conf.timezone = "Asia/Shanghai"
