from django.contrib import admin
from django.shortcuts import render_to_response, get_object_or_404

from procurement.admin_forms import ComponentAdminForm, SupplierAdminForm
from procurement.models import Supplier, Component, Representative


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_authorized', 'updated')
    form = SupplierAdminForm
    filter_horizonal = ('components',)


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'updated')
    form = ComponentAdminForm
    source_components_template = 'procurement/admin_templates/source_components.html'

    def source_components(self, request, pk):
        component = get_object_or_404(Component, pk=pk)

        return render_to_response(self.source_components_template, {
            'title': 'Source Suppliers for: %s' % component,
            'opts': self.model._meta,
            'component': component,
            'supplier_results': component.suppliers.filter(is_authorized=True),

        })


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Representative)
admin.site.register(Component, ComponentAdmin)
