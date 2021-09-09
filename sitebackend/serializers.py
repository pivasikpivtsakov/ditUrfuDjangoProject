from rest_framework import serializers
from .models import DirectionGroup, Direction

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('code', 'name', 'selected')


class DirectionGroupSerializer(serializers.ModelSerializer):
    directions = DirectionSerializer(many=True, read_only=True)

    class Meta:
        model = DirectionGroup
        fields = ('code', 'name', 'directions')
