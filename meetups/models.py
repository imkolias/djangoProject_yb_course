from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email = models.EmailField()
    date = models.DateField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)



    def __str__(self):
        return f'{self.title} - {self.slug}'
