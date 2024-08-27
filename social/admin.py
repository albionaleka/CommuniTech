from django.contrib import admin
from .models import Profile, Tweet, Comment
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Tweet)

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(DefaultUserAdmin):
    inlines = [ProfileInLine]

admin.site.register(User, UserAdmin)

admin.site.register(Comment)
