from rest_framework import serializers
from .models import advisor,booking
from authentication.serializers import UserSerializer

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = advisor
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer()

    class Meta:
        model = booking
        fields =  '__all__'        

