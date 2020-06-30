from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Employee
from .serializer import EmployeeSerializer, EmployeeDeSerializer


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            emp_obj = Employee.objects.get(pk=user_id)
            emp_user = EmployeeSerializer(emp_obj).data
            return Response({
                "status": 200,
                "msg": "查询单个",
                "results": emp_user,
            })
        else:
            emp_list = Employee.objects.all()
            emp_list_user = EmployeeSerializer(emp_list, many=True).data
            return Response({
                "status": 200,
                "msg": "查询所有",
                "results": emp_list_user,
            })
    def post(self,request,*args,**kwargs):
        user_data=request.data
        print(user_data)
        # return Response("1")
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        serializer = EmployeeDeSerializer(data=user_data)
        if serializer.is_valid():
            emp_obj = serializer.save()
            print(emp_obj, "this is obj", type(emp_obj))
            return Response({
                "status": 200,
                "msg": "用户创建成功",
                    "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                "results": "数据错误"
            })