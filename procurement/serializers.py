from rest_framework import serializers
from procurement.models import Component, Supplier, Representative


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        exclude = ('created', 'updated')


class SupplierSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='__str__', read_only=True)
    representatives = RepresentativeSerializer(many=True, read_only=True)
    class Meta:
        model = Supplier
        exclude = ('created', 'updated')


class ComponentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='__str__', read_only=True)
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Component
        exclude = ('created', 'updated')
