from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register the custom User model
User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	pass
