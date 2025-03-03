from rest_framework import serializers
from .models import SuperPower, League, Superheroe

class SuperPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperPower
        fields = ['id', 'name']

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name']

class SuperheroeSerializer(serializers.ModelSerializer):
    superPowers = SuperPowerSerializer(many=True)
    league = LeagueSerializer()

    class Meta:
        model = Superheroe
        fields = ['id', 'name', 'lastName', 'superPowers', 'league']
