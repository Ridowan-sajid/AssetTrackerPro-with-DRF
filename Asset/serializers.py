from rest_framework import serializers
from .models import Company,GadgetUser,Gadget


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

class GadgetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=GadgetUser
        fields='__all__'

class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = '__all__'