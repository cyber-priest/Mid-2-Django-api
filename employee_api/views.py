from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from mid2.serializer import EmployeeSerializer
from .models  import Employee


@api_view(['GET'])
def getEmployee(request):
    data = Employee.objects.all();
    serializer = EmployeeSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def setEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEployee(request, pk):
	student = Employee.objects.get(id=pk)
	student.delete()
	return Response('Item succsesfully delete!')

