from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import mysql.connector as sql
import jwt,json
from rest_framework import views
from rest_framework.response import Response

fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="kesar12345678",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd = make_password(value)
        
        c="insert into users1 Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')