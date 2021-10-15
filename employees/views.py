from django.shortcuts import render

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework import permissions

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]