from django.db import models
import datetime

class Member(models.Model):
    Coord16 = 'Coord16'
    Coord = 'Coord'
    Team = 'Team'
    Team16 = 'Team16'
    Webdev = 'Webdev'
    CHOICES = ((Coord16, 'Coord16'), (Coord, 'Coord'), (Team, 'Team'), (Team16, 'Team16'), (Webdev, 'Webdev'))
    role = models.CharField(max_length=20, choices=CHOICES, default=Team)
    name = models.CharField(max_length=200)
    facebook = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.role + ' - ' + self.name

class Project(models.Model):
    Title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.Title

    def desc(self):
        return self.text[:75]

class Tutorial(models.Model):
    Title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.Title

    def desc(self):
        return self.text[:75]
