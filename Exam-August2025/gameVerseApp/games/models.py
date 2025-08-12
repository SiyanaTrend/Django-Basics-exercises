from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from games.choices import GamePlatformChoices


class Game(models.Model):
    title = models.CharField(
        max_length=130,
        validators=[
            MinLengthValidator(3),
        ]
    )
    platform = models.CharField(
        max_length=15,
        choices=GamePlatformChoices.choices,
        default=GamePlatformChoices.OTHER,
    )
    release_date = models.DateField()

    level = models.SmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ]
    )
    screenshot_url = models.URLField(
        null=True,
        blank=True,
    )
    player = models.ForeignKey(
        to='players.Player',
        on_delete=models.CASCADE,
        related_name='games',
    )
