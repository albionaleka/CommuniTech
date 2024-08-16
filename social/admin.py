from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Unregister the original User admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Define your custom ProfileInline
class ProfileInLine(admin.StackedInline):
    model = Profile

# Define your custom UserAdmin
class UserAdmin(DefaultUserAdmin):
    inlines = [ProfileInLine]
    # fields = ["username"]  # Not needed if you're using DefaultUserAdmin

# Register the User model with your custom UserAdmin
admin.site.register(User, UserAdmin)
