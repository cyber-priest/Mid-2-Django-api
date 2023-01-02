from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mid2.serializer import TeacherSerializer
from .models  import Teacher


@api_view(['GET'])
def getTeacher(request):
    data = Teacher.objects.all();
    serializer = TeacherSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def setTeacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTeacher(request, pk):
	student = Teacher.objects.get(id=pk)
	student.delete()
	return Response('Item succsesfully delete!')

