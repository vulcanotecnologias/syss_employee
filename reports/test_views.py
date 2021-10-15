import json
import pytest
from datetime import datetime
from datetime import date
from django.db.models import Sum

from reports.services.reports.reports import Reports
from employees.models import Employee

# Arrange
@pytest.fixture
def employees():
   Employee.objects.create(name="teste1", email='teste1@teste.com', department='MSL', salary='4530.20', birth_date=datetime.strptime('01-01-1994', '%d-%m-%Y')), 
   Employee.objects.create(name="teste2", email='teste2@teste.com', department='KSM', salary='5520.13', birth_date=datetime.strptime('12-06-1990', '%d-%m-%Y')),
   Employee.objects.create(name="teste3", email='teste3@teste.com', department='JSN', salary='6501.10', birth_date=datetime.strptime('20-12-1987', '%d-%m-%Y')),
   Employee.objects.create(name="teste4", email='teste4@teste.com', department='ELF', salary='7982.46', birth_date=datetime.strptime('13-03-1985', '%d-%m-%Y')),
   Employee.objects.create(name="teste5", email='teste5@teste.com', department='JDS', salary='4584.95', birth_date=datetime.strptime('12-10-1990', '%d-%m-%Y')),
   Employee.objects.create(name="teste6", email='teste6@teste.com', department='POS', salary='9563.23', birth_date=datetime.strptime('27-02-1984', '%d-%m-%Y')),
   Employee.objects.create(name="teste7", email='teste7@teste.com', department='RMA', salary='12568.03', birth_date=datetime.strptime('12-03-1990', '%d-%m-%Y')), 

@pytest.mark.django_db
def test_reports_salary_average(employees):
   employees
   count = Employee.objects.count()
   report_salary = Reports.get_salary()
   json_report_age = json.loads(json.dumps(report_salary))
   sumSalary = Employee.objects.all().aggregate(sum=Sum('salary'))['sum']

   return json_report_age["average"] == round((sumSalary / count), 2)

@pytest.mark.django_db
def test_reports_age_average(employees):
   employees
   count = Employee.objects.count()
   sumAge = 0
   report_age = Reports.get_ages()
   json_report_age = json.loads(json.dumps(report_age))
   employees = Employee.objects.all()

   for employee in employees.iterator():
      today = date.today()
      sumAge = sumAge + (today.year - employee.birth_date.year - ((today.month, today.day) < (employee.birth_date.month, employee.birth_date.day)))
   average = sumAge / count

   return json_report_age["average"] == round(average, 2)