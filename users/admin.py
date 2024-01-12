from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'is_active',)


admin.site.register(User, UserAdmin)





