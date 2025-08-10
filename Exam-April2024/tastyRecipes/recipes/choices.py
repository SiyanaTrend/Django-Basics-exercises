from django.db import models


class CuisineChoices(models.TextChoices):
    FRENCH = "FR", "French"
    CHINESE = "CN", "Chinese"
    ITALIAN = "IT", "Italian"
    BALKAN = "BK", "Balkan"
    OTHER = "Other", "Other"
