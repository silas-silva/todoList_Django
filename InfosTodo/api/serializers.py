from rest_framework import serializers
from InfosTodo import models

class InfosTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.todo
        fields = '__all__'