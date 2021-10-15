from rest_framework import serializers
from django.db import models

from employees.models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    email = serializers.CharField(required=True, max_length=100)
    department = serializers.CharField(max_length=100)
    salary = serializers.FloatField()
    birth_date = serializers.DateField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary', 'birth_date', 'email']

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('department', instance.email)
        instance.salary = validated_data.get('salary', instance.email)
        instance.birth_date = validated_data.get('birth_date', instance.email)
        instance.save()
        return instance

class EmployeeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary', 'birth_date', 'email']