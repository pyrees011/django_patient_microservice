from django.urls import path
from .views import PatientAppointmentView

urlpatterns = [
    path('appointments/<int:id>/', PatientAppointmentView.as_view(), name='patient-appointment'),
]
