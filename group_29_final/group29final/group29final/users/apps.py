import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "group29final.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import group29final.users.signals  # noqa: F401
