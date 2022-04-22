from rest_framework import serializers



class AddPlanSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    validity_in_days = serializers.IntegerField()
    voice = serializers.CharField(max_length=20)
    data_per_day = serializers.IntegerField()
    sms_per_day = serializers.IntegerField()
    add_ons = serializers.CharField(max_length=100)