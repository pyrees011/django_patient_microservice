from django.urls import path
from .views import PatientListCreate, PatientRetrieveUpdateDestroy

urlpatterns = [
    path('', PatientListCreate.as_view(), name='patient-list-create'),
    path('<int:pk>/', PatientRetrieveUpdateDestroy.as_view(), name='patient-retrieve-update-destroy'),
]