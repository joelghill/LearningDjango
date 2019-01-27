from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from procurement.models import Supplier, Component, Representative


class ComponentAdminForm(forms.ModelForm):
    suppliers = forms.ModelMultipleChoiceField(
        queryset=Supplier.objects.filter(is_authorized=True),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Suppliers',
            is_stacked=False
        )

    )

    class Meta:
        model = Component
        fields = ['name', 'sku', 'suppliers']


class SupplierAdminForm(forms.ModelForm):
    representatives = forms.ModelMultipleChoiceField(
        queryset=Representative.objects.filter(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Representatives',
            is_stacked=False
        )

    )

    class Meta:
        model = Supplier
        fields = ['name', 'is_authorized', 'representatives']
