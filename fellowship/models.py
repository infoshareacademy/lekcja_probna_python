from django.db import models

class TimeStampable(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(TimeStampable):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Member(TimeStampable):
    RACES = (
        (1, "Hobbit"),
        (2, "Human"),
        (3, "Elf"),
        (4, "Dwarf"),
        (5, "Other")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    race = models.IntegerField(choices=RACES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

