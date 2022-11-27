from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import mysql.connector as sql
import jwt,json
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
import json

em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="kesar12345678",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd = value
        c="select * from users1 where email='{}'".format(em)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        print(t)
        a = check_password(pwd,t[0][4])
        print(t[0][4])
        print(a)
        if t==() or not a:
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login.html')