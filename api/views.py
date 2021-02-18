from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from core.custom import prin, resp_fun
from django.conf import settings
# Caching modules import
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# import DB connections
from django.db import connection, connections
# import pandas for geting db
import pandas as pd


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class student(APIView):
    # permission_classes = (IsAuthenticated, )

    CURSOR = connection.cursor()

    def get(self, request, *args, **kwargs):
        if bool(dict(request.GET)):
            s_id = request.GET['id']
            if cache.get(s_id): # Check if user exist in redis catche or not
                resp = cache.get(s_id)
                prin('cache found', resp)
            else:
                # Query process
                print('cache not found')
                query = f'select count(*) from api_student where id={s_id}'
                self.CURSOR.execute(query)
                exist = self.CURSOR.fetchall()

                if exist[0][0] > 0:
                # ORM Process
                # std = Student.objects.filter(id=s_id)
                # if std.exists():
                    # resp = StudentSerializer(std[0], many=False).data
                    query = f'select name, email, contact, address from api_student where id={s_id}'
                    self.CURSOR.execute(query)
                    resp = self.CURSOR.fetchall()
                    cache.set(s_id, resp) # Set value in cache
                else:
                    msg = 'Student data has been not found.'
                    resp = {
                        **{'status': status.HTTP_404_NOT_FOUND},
                        **resp_fun(msg, '', 'error')
                    }
        else:
            # ORM Process
            # resp = StudentSerializer(Student.objects.all(), many=True).data
            # Query process
            query = 'select name, email, contact, address from api_student'
            self.CURSOR.execute(query)
            resp = self.CURSOR.fetchall()
            ## Using Pandas to read data of sqlite
            # sql_con = connections['db']
            # sql_con.ensure_connection()
            # pds = pd.read_sql_query(query, sql_con)
            # prin(pds)

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
