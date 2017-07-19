from django.shortcuts import render, HttpResponse
from django.views import View
from model_model import models
from dbms import forms
from back.views.AuthAccount import AuthAccount
from django.utils.decorators import method_decorator
from scripts import functions


@method_decorator(AuthAccount, name='dispatch')
class SlowQuery(View):
    def get(self, request):
        return render(request, 'dbms/slow_query/slow_sql_display.html')


    def post(self, request):
        pass