from django.contrib import admin
from weather_app.models import Continent, Country, City, DateWeather, TimeWeather, TimeWeather6, TimeWeather9, TimeWeather12, TimeWeather15, TimeWeather20, TimeWeather23

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(TimeWeather)
admin.site.register(TimeWeather6)
admin.site.register(TimeWeather9)
admin.site.register(TimeWeather12)
admin.site.register(TimeWeather15)
admin.site.register(TimeWeather20)
admin.site.register(TimeWeather23)


@admin.register(DateWeather)
class DateWeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'date']
