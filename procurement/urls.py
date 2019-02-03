from django.urls import path
from procurement.views import ComponentSearchView, DocumentationView
from procurement.api import ComponentAPIList, ComponentAPIRetrieve, SupplierAPIList, SupplierAPIRetrieve, RepresentativeAPIList, RepresentativeAPIRetrieve

urlpatterns = [
    path('', ComponentSearchView.as_view(), name='component-search'),
    path('documentation', DocumentationView.as_view(), name='documentation'),

    # API Urls
    path('api/components/', ComponentAPIList.as_view(), name='api-component-list'),
    path('api/components/<int:pk>/', ComponentAPIRetrieve.as_view(), name='api-component-retrieve'),
    path('api/suppliers/', SupplierAPIList.as_view(), name='api-supplier-list'),
    path('api/suppliers/<int:pk>/', SupplierAPIRetrieve.as_view(), name='api-supplier-retrieve'),
    path('api/representatives/', RepresentativeAPIList.as_view(), name='api-representative-list'),
    path('api/representatives/<int:pk>/', RepresentativeAPIRetrieve.as_view(), name='api-representative-retrieve'),
]
