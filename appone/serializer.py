from rest_framework import serializers
from appone.models import *


#assign --> same code- ->
class EmpSerializer(serializers.ModelSerializer):   # whenever someone requests for emp --> all addresses for tht emp shud be given
    adrs= serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(),many=True)
    class Meta:
        model = Emp
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    emps = EmpSerializer(many=True)     # whenever u request for address type --> make sure all address belongs to all emps --< shud be given
    class Meta:
        model = Address
        fields = '__all__'