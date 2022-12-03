from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def create_user(request):
    reason = ''
    user = None

    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username, email, password)
    except:
        reason = 'Integrity error!'

    if user is not None:
        return JsonResponse({
            'success': 'true'
        })
    else:
        return JsonResponse({
            'success': 'false',
            'reason': reason
        })

@require_http_methods(["POST"])
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            'success': 'true'
        })
    else:
        return JsonResponse({
            'success': 'false',
            'reason': 'Invalid Credentials!'
        })

@require_http_methods(["POST"])
def logout_user(request):
    logout(request)
    return JsonResponse({
        'success': 'true'
    })
