import json
from datetime import date
from django.db.models import Sum

from employees.models import Employee
from employees.serializers import EmployeeObjectSerializer

class Reports:
    def get_salary():
        count = Employee.objects.count()
        if count == 0:
            datas = {
                "lowest":
                    ""
                ,
                "highest": 
                    ""
                ,
                "average": 0
            }    
            return datas
        serializer_lowest = EmployeeObjectSerializer(Employee.objects.order_by('salary').first())
        serializer_highest = EmployeeObjectSerializer(Employee.objects.order_by('-salary').first())
        sumSalary = Employee.objects.all().aggregate(sum=Sum('salary'))['sum']
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
        return datas

    def get_ages():
        count = Employee.objects.count()
        if count == 0:
            datas = {
                "younger":
                    ""
                ,
                "older": 
                    ""
                ,
                "average": 0
            }    
            return datas
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
        return datas