from rest_framework.generics import ListAPIView, RetrieveAPIView

from procurement.models import Component, Supplier, Representative
from procurement.serializers import ComponentSerializer, SupplierSerializer, RepresentativeSerializer


class ComponentAPIList(ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentAPIRetrieve(RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class SupplierAPIList(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierAPIRetrieve(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class RepresentativeAPIList(ListAPIView):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer


class RepresentativeAPIRetrieve(RetrieveAPIView):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer
