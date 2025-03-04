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
    superPowers = SuperPowerSerializer(many=True, required=False)  # Puede estar vacío
    league = LeagueSerializer(required=False, allow_null=True)     # Puede ser null

    class Meta:
        model = Superheroe
        fields = '__all__'

    def create(self, validated_data):
        superpowers_data = validated_data.pop('superPowers', [])
        league_data = validated_data.pop('league', None)

        superheroe = Superheroe.objects.create(**validated_data)

        # Asign Superpowers if not None
        for power_data in superpowers_data:
            power, _ = SuperPower.objects.get_or_create(**power_data)
            superheroe.superPowers.add(power)

        # Assign league if not None
        if league_data:
            league, _ = League.objects.get_or_create(**league_data)
            superheroe.league = league
            superheroe.save()

        return superheroe

    def update(self, instance, validated_data):
        superpowers_data = validated_data.pop('superPowers', [])
        league_data = validated_data.pop('league', None)

        instance.name = validated_data.get('name', instance.name)
        instance.lastName = validated_data.get('lastName', instance.lastName)

        # Update superPowers
        instance.superPowers.clear()
        for power_data in superpowers_data:
            power, _ = SuperPower.objects.get_or_create(**power_data)
            instance.superPowers.add(power)

        # Update league or remove it if None
        if league_data:
            league, _ = League.objects.get_or_create(**league_data)
            instance.league = league
        else:
            instance.league = None

        instance.save()
        return instance