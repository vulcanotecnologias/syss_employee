from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reports.services.reports.reports import Reports


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @api_view(('GET',))
    def age(self):
        datas = Reports.get_ages()
        return Response( datas, status=status.HTTP_200_OK )
        
    @api_view(('GET',))
    def salary(self):
        datas = Reports.get_salary()
        return Response( datas, status=status.HTTP_200_OK )

    