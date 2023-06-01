from django.shortcuts import render
from .models import Student
from .serilizers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerilizer(stu)
    return JsonResponse(serializer.data)


# All student data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerilizer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')