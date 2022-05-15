from rest_framework import viewsets
from InfosTodo.api import serializers
from InfosTodo import models

class InfosTodoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InfosTodoSerializer
    queryset = models.todo.objects.all() 
