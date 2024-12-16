from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from ConnextoSocial.accounts.forms import AppUserCreationForm, AppUserChangeForm
from ConnextoSocial.accounts.models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

UserModel = get_user_model()


# Inline model to manage related Profile directly from the User admin
class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    can_delete = False
    verbose_name_plural = 'Profiles'


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    # Custom list display fields
    list_display = ('pk', 'email', 'is_active', 'is_staff', 'is_superuser', 'get_user_roles')

    # Add search fields for email
    search_fields = ('email',)

    # Add list filter options
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Add ordering by email instead of primary key
    ordering = ('email',)

    # Define inlines
    inlines = [ProfileInline]

    # Customize fieldsets for better clarity
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    # Add an action to deactivate selected users
    actions = ["deactivate_users"]

    def deactivate_users(self, request, queryset):
        """Custom action to deactivate selected users."""
        queryset.update(is_active=False)
    deactivate_users.short_description = "Deactivate selected users"

    def get_user_roles(self, obj):
        """Display user roles based on permissions."""
        if obj.is_superuser:
            return "Superuser"
        elif obj.is_staff:
            return "Staff"
        return "User"
    get_user_roles.short_description = "Roles"


class CustomGroupAdmin(GroupAdmin):
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of critical groups."""
        if obj and obj.name in ("Superusers", "Staff"):
            return False
        return super().has_delete_permission(request, obj)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
