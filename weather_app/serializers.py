from rest_framework import serializers
from .models import Continent, Country, City, DateWeather, TimeWeather, TimeWeather6, TimeWeather9, TimeWeather12, TimeWeather15, TimeWeather20, TimeWeather23


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = DateWeather
        fields = '__all__'

class TimeWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather
        fields = ['time', 'temp', 'sky']

class TimeWeather6Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather6
        fields = ['time', 'temp', 'sky']

class TimeWeather9Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather9
        fields = ['time', 'temp', 'sky']

class TimeWeather12Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather12
        fields = ['time', 'temp', 'sky']

class TimeWeather15Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather15
        fields = ['time', 'temp', 'sky']

class TimeWeather20Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather20
        fields = ['time', 'temp', 'sky']

class TimeWeather23Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWeather23
        fields = 'time', 'temp', 'sky'


class CitySerializer(serializers.ModelSerializer):
    dateweather = WeatherSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    city = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        fields = '__all__'
