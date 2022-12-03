from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json


@require_http_methods(["POST", "OPTIONS"])
def create_user(request):
    reason = ''
    user = None
    body = request.body.decode('utf-8')
    body = json.loads(body)

    try:
        username = body['username']
        password = body['password']
        email = body['email']

        user = User.objects.create_user(username, email, password)
    except:
        if username and password and email:
            reason = 'Integrity error!'
        else:
            reason = 'Incorrect arguments!'

    if user is not None:
        return JsonResponse({
            'success': 'true'
        })
    else:
        return JsonResponse({
            'success': 'false',
            'reason': reason
        })

@require_http_methods(["POST", "OPTIONS"])
def login_user(request):
    reason = 'Invalid Credentials!'
    username = ''
    password = ''
    user = None
    body = request.body.decode('utf-8')
    body = json.loads(body)

    try:
        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)
    except:
        reason = 'Incorrect Arguments!'

    if user is not None:
        login(request, user)
        return JsonResponse({
            'success': 'true'
        })
    else:
        return JsonResponse({
            'success': 'false',
            'reason': reason
        })

@require_http_methods(["POST", "OPTIONS"])
def logout_user(request):
    logout(request)
    return JsonResponse({
        'success': 'true'
    })
