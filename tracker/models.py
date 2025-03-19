from django.contrib.postgres.fields import ArrayField
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
    This model should largely mirror what's recorded on a chronicle sheet. That's the v1 approach I'm taking.
    I may also want to sort out a way to distinguish between Scenarios and Quests/Bounties/Etc.

    But, should I have a different "Chronicle" model for that? Should THIS model contain more info about the CONTENT of the scenario?

    As of 2025-03-18, I'm making a design decision to ignore Quests, etc and largely ignore Starfinder scenarios. To get the MVP working, I'm going to focus on PF2e scenarios. I'll leave the `starfinder` boolean in place for now.
    """

    character = models.ForeignKey(
        Character,
        related_name="scenario",
        on_delete=models.CASCADE,
        help_text="Which character has played this scenario?",
        null=True,
    )
    name = models.CharField(
        blank=True, max_length=256, help_text="What's the name of this scenario?"
    )
    number = models.CharField(
        blank=True,
        max_length=25,
        help_text="How is this scenario identified? 1-01? 6-05?",
    )
    starfinder = models.BooleanField(
        default=False, help_text="Is this a Starfinder Society scenario?"
    )
    paizo_url = models.URLField(
        blank=True, null=True, help_text="Where can this be found on the Paizo site?"
    )
    other_url = models.URLField(
        blank=True,
        null=True,
        help_text="Where can reference to this be found outside the Paizo site? One of the community wikis, for example.",
    )
    repeatable = models.BooleanField(default=False, help_text="Is this repeatable")
    # How do I enforce the UniqueConstraint for scenarios with the repatable tag?
    # ANSWER: Repeatable refers to the PLAYER; Each CHARACTER can only play a scenario once.
    tags = ArrayField(
        models.CharField(max_length=128),
        blank=True,
        default=list,
        help_text="What tags (other than repeatable) does this scenario have",
    )
    gold_earned = models.DecimalField(
        default=0.00,
        max_digits=5,
        decimal_places=2,
        help_text="How much gold was earned. Include your Earned Income. Represent Silver and Copper as decimal values. For Platinum, multiply by 10. MOVE TO CHRONICLE",
    )
    xp_earned = models.IntegerField(
        default=0, help_text="How many Experience Points were earned. MOVE TO CHRONICLE"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="various textual data you want to store; now for results for Recall Knowledge checks. MOVE TO JOURNAL",
    )
    # Faction Points (Does this need to be a dict with choices?)
    # ToDo for later: Replayed with a boon; how can I override the UniqueConstraint in that case?

    def __str__(self):
        return f"{self.number}: {self.name}; "


class Transaction(models.Model):
    """
    Keep track of items/gear a character purchases or sells
    """

    pass
    # FK to CHARACTER
    # Gold (plus/minus)
    # AoN URL
