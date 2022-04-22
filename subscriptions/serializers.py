from rest_framework import serializers



class ValidationSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()
    plan_id = serializers.IntegerField()