import django
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.views.generic import RedirectView
from .serializers import *
from .models import *
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class VotingViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Voting.objects.all()
    serializer_class = VotingSerializer


class LikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        menu = Menu.objects.filter(id=1)
        print(menu[0])
        obj = Voting.objects.get(links_to_menu=menu[0])
        print(obj.result)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
                obj.result -= 1
                obj.save()
            else:
                liked = True
                obj.likes.add(user)
                obj.result += 1
                obj.save()
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


class TodaysResult(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        obj = Voting.objects.get(date=django.utils.timezone.datetime.today())
        # print(obj.result)
        data = {
            "result": obj.result,
        }
        return Response(data)


def index(request):
    return render(request, 'app/index.html')
