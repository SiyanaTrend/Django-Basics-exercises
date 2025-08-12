from django.db import models


class GamePlatformChoices(models.TextChoices):
    PC_GAMES = "PC Games", "PC Games"
    CONSOLE = "Console Games", "Console Games"
    OTHER = "Other Games", "Other Games"
