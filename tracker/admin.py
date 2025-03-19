from django.contrib import admin

from .models import Character, Scenario


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "character_number"]


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ["number", "name"]
