# How to build it?
I'll probably build multiple versions. This is a tentative order, but Vanilla Django will be first.
- Vanilla Django
- Django & htmx
- Django w/ Django Ninja to add an API (for mobile or CLI apps?)
- FastAPI?


## Build/Deploy Timeline
- Get an MVP done before PyTexas (2025-04-10), so I can try it at the Thursday night pre-conf game
- Use it again in Pittsburg during PyCon US (2025-05)
- REALLY give it a test during PaizoCon Online
- Try it again at ChupacabraCon
- Refine b/w each use

### Models
PLAYER (User)
- Email
- Org Play Number

CHARACTER
- FK to PLAYER
- Org Play Number Suffix
- Starting Gold
- XP (default to 0)
- Faction Points (later; how to deal with faction changes?)
- Do I want to track starting gear?

SCENARIO (mostly chronicle sheet data; look at a chronicle sheet)
- FK to CHARACTER
- Number
- Paizo URL
- Other URL (PF or SF wiki)
- Gold Earned
- XP Earned
- Faction Points (Does this need to be a duct with choices?)
- Notes (various textual data you want to store)

TRANSACTION (stuff you buy/sell/craft?)
- FK to CHARACTER
- Gold (plus/minus)
- AoN URL


### FORMS
- Add Player
- Add Character
- Add Scenario
- Add Transaction


### PAGES
- Display Character
- Display list of Player’s Characters
