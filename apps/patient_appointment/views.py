from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import requests
from service_registrar.mixins import ServiceAddressMixin

# Create your views here.

class PatientAppointmentView(APIView, ServiceAddressMixin):
    def get(self, request, id=None):
        try:
            self.get_service_address('appointment')

        except Exception as exc:
            return self.response_from_exception(exc)
        
        response = requests.get(f'{self.url}/api/appointment/{id}/')
        if response.status_code != 200:
            return JsonResponse(response.json(), status=response.status_code)
        return JsonResponse(response.json(), status=response.status_code)