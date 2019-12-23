from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from voteapp.models import *
from django.contrib.auth.models import User


class VotingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voting
        fields = ('url', 'id',  'date', 'links_to_menu', 'likes', 'result')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu
        fields = ('url', 'id', 'belongsTo', 'item_name', 'price', 'about')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('url', 'id', 'full_name', 'mobile', 'about')
