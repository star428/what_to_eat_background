from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Users


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from .models import Users
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        try:
            t = Users.objects.get(user_id = user_id)
            if t.password == password:
                return HttpResponse("post_ok")
            else:
                return HttpResponse("passward_error")

        except ObjectDoesNotExist:
            return HttpResponse("post_error")

    else:
        return HttpResponse("you package is get")


def index(request):
    return render(request, 'polls/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer