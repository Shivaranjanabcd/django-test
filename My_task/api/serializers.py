from myapp.models import app
from rest_framework import serializers

class appserializer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = "__all__"