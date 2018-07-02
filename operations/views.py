# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import version as py_version
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class MainAPI(APIView):
    def get(self, request, format=None):
        return Response({'pymongo_version': py_version}, status=200)