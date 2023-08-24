from api.models import  User
from rest_framework import serializers
# this file to provide json format as a response

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = '__all__'