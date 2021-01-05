from django.contrib.contenttypes.models import ContentType
import threading

_thread_locals = threading.local()


def set_current_user(user):
    _thread_locals.user = user


def get_current_user():
    return getattr(_thread_locals, 'user', None)


def remove_current_user():
    _thread_locals.user = None


def load_model(model_name, app_label=None):
    if app_label is not None:
        model = ContentType.objects.get(app_label=app_label, model=model_name)
    else:
        model = ContentType.objects.get(model=model_name)
    return model.model_class()
