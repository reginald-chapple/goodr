from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model."""

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': (
            'name',
            'photo',
            'phone_number',
            'birthdate',
            'address',
            'city',
            'state',
            'country',
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_member', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'password1', 'password2'),
        }),
    )
    list_display = ('name', 'is_staff', 'is_member',)
    list_filter = ('is_staff','is_member',)
    search_fields = ('email', 'name',)
    ordering = ('name',)
