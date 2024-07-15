from django.contrib import admin
from .models import Team, Member


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass