from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Character(models.Model):
    """
    Details for a specific PFS/SFS Character
    """

    player = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="Who is playing this character?"
    )
    name = models.CharField(
        max_length=255, help_text="What's the name of this character?"
    )
    character_number = models.IntegerField(
        default=2001, help_text="What's the unique identifier for this character?"
    )
    gold = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    # ToDo: create a calculated "Level" attribute: experience/12
    profile = models.TextField(
        blank=True, help_text="Include character description, background and notes here"
    )
    # Faction Points (later; how to deal with faction changes?)
    # Do I want to track starting gear?

    # make sure no player uses the same character number twice
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["player", "character_number"],
                name="unique_player_character_number",
            )
        ]

    def __str__(self):
        return f"{self.name}; {self.character_number}"


class Scenario(models.Model):
    """
    What Org Play scenarios have been played
    """

    pass
    # character = models.ForeignKey(
    #     Character,
    #     related_name="scenario",
    #     on_delete=models.CASCADE,
    #     help_text="Which character was played in this scenario?",
    # )
    # Number (Identifier; 6-01 or Q18)
    # Paizo URL
    # Other URL (PF or SF wiki)
    # Gold Earned
    # XP Earned
    # Faction Points (Does this need to be a dict with choices?)
    # Notes (various textual data you want to store)


class Transaction(models.Model):
    """
    Keep track of items/gear a character purchases or sells
    """

    pass
    # FK to CHARACTER
    # Gold (plus/minus)
    # AoN URL
