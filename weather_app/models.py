from django.db import models

# Create your models here.


class Continent(models.Model):
    continent_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    conitnent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="country")
    conutry_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.conutry_name


class City(models.Model):

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name
    
class TimeWeather(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather6(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather9(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather12(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather15(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather20(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather23(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')


class DateWeather(models.Model):

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dateweather")

    date = models.DateField()
    
    timeWeather = models.ForeignKey(
        TimeWeather, on_delete=models.CASCADE, related_name="timeweather", null=True)
    
    timeWeather6 = models.ForeignKey(
        TimeWeather6, on_delete=models.CASCADE, related_name="timeweather6", null=True)
    
    timeWeather9 = models.ForeignKey(
        TimeWeather9, on_delete=models.CASCADE, related_name="timeweather9", null=True)
    
    timeWeather12 = models.ForeignKey(
        TimeWeather12, on_delete=models.CASCADE, related_name="timeweather12", null=True)
   
    timeWeather15 = models.ForeignKey(
        TimeWeather15, on_delete=models.CASCADE, related_name="timeweather15", null=True)
    
    timeWeather20 = models.ForeignKey(
        TimeWeather20, on_delete=models.CASCADE, related_name="timeweather20", null=True)
    
    timeWeather23 = models.ForeignKey(
        TimeWeather23, on_delete=models.CASCADE, related_name="timeweather23", null=True)
    
    timeRise = models.TimeField(null=True)
    timeSet = models.TimeField(null=True)
    
    attent_name = models.CharField(max_length=500, null=True)

    # def __str__(self):
    #     return str(self.date)
