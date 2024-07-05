from django.shortcuts import render
from constants import APPOINTMENT_SERVICE_URL
from utils.proxy import ProxyView

# Create your views here.

class appointmentGetDetails(ProxyView):
    def get(self, request, patient_id=None):
            service_url = f"{APPOINTMENT_SERVICE_URL}{patient_id}/"
            return self.proxy_request(request, service_url)