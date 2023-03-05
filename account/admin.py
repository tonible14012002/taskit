from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import MyUser


class MyUserAdmin(BaseUserAdmin):
    model = MyUser
    list_display = ('username', 'is_staff', 'is_superuser', 
                    'email', 'first_name', 'last_name', 'birth')
    list_filter = list_display
    fieldsets = (
        ('Credentials', {'fields': ('username', 'email',)}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active',
                       'groups', 'user_permissions')
            })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password', 'birth',
                'first_name', 'last_name'
            )
        }),
    )

    search_fields = ('username', 'email', 'birth')
    ordering = ('username', 'first_name', 'last_name', 'email')


admin.site.register(MyUser, MyUserAdmin)


# Register your models here.