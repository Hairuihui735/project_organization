from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

class Tariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

class Leader(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='leaders/', blank=True, null=True)

class ConsultationQueue(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    application_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='consultation_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name