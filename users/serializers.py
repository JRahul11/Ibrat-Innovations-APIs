from rest_framework import serializers



class AddUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone_number = serializers.IntegerField()