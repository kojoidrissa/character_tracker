from django.db import models


class Character(models.Model):
    pass
    # FK to PLAYER  
    # Org Play Number Suffix
    # Starting Gold
    # XP (default to 0)
    # Faction Points (later; how to deal with faction changes?)
    # Do I want to track starting gear?

class Scenario(models.Model):
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
    pass
    # FK to CHARACTER
    # Gold (plus/minus)
    # AoN URL