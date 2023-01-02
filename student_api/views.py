from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from mid2.serializer import StudentSerializer
from .models  import Student


@api_view(['GET'])
def getStudent(request):
    data = Student.objects.all();
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def setStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteStudent(request, pk):
	student = Student.objects.get(id=pk)
	student.delete()
	return Response('Item succsesfully delete!')

@api_view(['POST'])
def updateStudent(request, pk):
	student = Student.objects.get(id=pk)
	serializer = StudentSerializer(instance=student, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)