from django.contrib import admin
# from django.contrib.admin import autodiscover
# from django.contrib.auth.admin import UserAdmin, GroupAdmin
# from django.contrib.auth.models import User, Group


from .forms import AdminAuthenticationForm


class AdminSite(admin.AdminSite):
    login_form = AdminAuthenticationForm
    login_template = 'admin/captcha_login.html'

site = AdminSite()
admin.site = site
# admin.site.register(Group, GroupAdmin)
# admin.site.register(User, UserAdmin)
