from django.contrib.admin.apps import AdminConfig as _AdminConfig


class AdminConfig(_AdminConfig):
    """
    Inherit Django AdminConfig. We want the autodiscover feature.
    """
    default_site = 'captcha_admin.admin.AdminSite'
