from django.db import models

# Create your models here.

class SuperPower(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Superheroe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    lastName = models.CharField(max_length=30)

    # A superhero can have none, one or more superwores
    superPowers = models.ManyToManyField(SuperPower, blank=True)

    # A superhero can belong to only one league or none of them
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.lastName}"