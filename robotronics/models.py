from django.db import models

class Member(models.Model):
    Faculty = 'Faculty'
    Coord = 'Coord'
    Team = 'Team'
    WebDev = 'WebDev'
    CHOICES = ((Faculty, 'Faculty'), (Coord, 'Coord'), (Team, 'Team'), (WebDev, 'WebDev'))
    role = models.CharField(max_length=20, choices=CHOICES, default=Team)
    name = models.CharField(max_length=200)
    facebook = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.role + ' - ' + self.name

class Project(models.Model):
    Title = models.CharField(max_length=200)
    details = models.TextField()

class Tutorial(models.Model):
    Title = models.CharField(max_length=200)
    details = models.TextField()
