from django.http.response import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from datetime import date

from employees.models import Employee
from employees.serializers import EmployeeObjectSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @api_view(('GET',))
    def age(self):
        count = Employee.objects.count()
        serializer_younger = EmployeeObjectSerializer(Employee.objects.order_by('-birth_date').first())
        serializer_older = EmployeeObjectSerializer(Employee.objects.order_by('birth_date').first())
        sumAge = 0
        employees = Employee.objects.all()
        for employee in employees.iterator():
            today = date.today()
            sumAge = sumAge + (today.year - employee.birth_date.year - ((today.month, today.day) < (employee.birth_date.month, employee.birth_date.day)))
        average = sumAge / count
        datas = {
            "younger":
                json.loads(json.dumps(serializer_younger.data))
            ,
            "older": 
                json.loads(json.dumps(serializer_older.data))
            ,
            "average": round(average, 2)
        }
        return Response( datas, status=status.HTTP_200_OK )
        
    @api_view(('GET',))
    def salary(self):
        count = Employee.objects.count()
        serializer_lowest = EmployeeObjectSerializer(Employee.objects.order_by('-salary').first())
        serializer_highest = EmployeeObjectSerializer(Employee.objects.order_by('salary').first())
        sumSalary = 0
        employees = Employee.objects.all()
        for employee in employees.iterator():
            sumSalary = sumSalary + employee.salary
        average = sumSalary / count
        datas = {
            "lowest":
                json.loads(json.dumps(serializer_lowest.data))
            ,
            "highest": 
                json.loads(json.dumps(serializer_highest.data))
            ,
            "average": round(average, 2)
        }
        return Response( datas, status=status.HTTP_200_OK )