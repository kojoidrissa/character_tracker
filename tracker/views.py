from django.views.generic import ListView
from tracker.models import Character


class CharacterListView(ListView):
    model = Character
    # template_name = "templates/character_list.html"
    context_object_name = "character_list"
