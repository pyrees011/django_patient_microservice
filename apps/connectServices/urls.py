from django.urls import path
from .views import appointmentGetDetails

urlpatterns = [
    path('/get_appointment_details/<int:patient_id>/', appointmentGetDetails.as_view(), name='get-appointment-details'),
]