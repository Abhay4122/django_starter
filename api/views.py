from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from core.custom import prin, resp_fun


class student(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        if bool(dict(request.GET)):
            std = Student.objects.filter(id=request.GET['id'])
            if std.exists():
                resp = StudentSerializer(std[0], many=False).data
            else:
                msg = 'Student data has been not found.'
                resp = {
                    **{'status': status.HTTP_404_NOT_FOUND},
                    **resp_fun(msg, '', 'error')
                }
        else:
            resp = StudentSerializer(Student.objects.all(), many=True).data

        return Response(resp)

    def put(self, request, *args, **kwargs):
        if bool(dict(request.GET)):
            std = Student.objects.filter(id=request.GET['id'])
            if std.exists():
                serializer = StudentSerializer(std[0], data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    resp = serializer.data
                else:
                    resp = serializer.errors
            else:
                msg = 'Student has been not found.'
                resp = {
                    **{'status': status.HTTP_404_NOT_FOUND},
                    **resp_fun(msg, '', 'error')
                }
        else:
            msg = 'Student id has been not found.'
            resp = {
                **{'status': status.HTTP_400_BAD_REQUEST},
                **resp_fun(msg, '', 'error')
            }

        return Response(resp)

    def delete(self, request, *args, **kwargs):
        if bool(dict(request.GET)):
            std = Student.objects.filter(id=request.GET['id'])
            if std.exists():
                std[0].delete()
                msg = f'Student {std[0].name} had been deleted successfully.'
                resp = {
                    **{'status': status.HTTP_200_OK},
                    **resp_fun(msg, '', 'success')
                }
            else:
                msg = 'Student has been not found.'
                resp = {
                    **{'status': status.HTTP_404_NOT_FOUND},
                    **resp_fun(msg, '', 'error')
                }
        else:
            msg = 'Student id has been not found.'
            resp = {
                **{'status': status.HTTP_400_BAD_REQUEST},
                **resp_fun(msg, '', 'error')
            }

        return Response(resp)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = serializer.data
        else:
            resp = serializer.errors

        return Response(resp)
