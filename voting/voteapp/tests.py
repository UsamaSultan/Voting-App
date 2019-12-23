from django.test import TestCase
from .models import *


class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(
            full_name="zzz", mobile="9999999999", about="pqr")
        Restaurant.objects.create(
            full_name="yyy", mobile="9999999999", about="abc")

    def check_Restaurant(self):
        zzz = Restaurant.objects.get(full_name="zzz")
        yyy = Restaurant.objects.get(about="abc")


class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(
            belongsTo="zzz", item_name="apple", price="123", about="pqr")
        Menu.objects.create(
            belongsTo="yyy", item_name="banana", price="311", about="abc")

    def check_menus(self):
        zzz = Menu.objects.get(item_name="apple")
        yyy = Menu.objects.get(about="abc")


class VotingTestCase(TestCase):
    def setUp(self):
        Voting.objects.create(date="2019-06-16", likes="1",
                              links_to_menu="zzz", result="0")
        Voting.objects.create(date="2019-06-10", likes="0",
                              links_to_menu="yyy", result="0")

    def voting_func(self):
        zzz = Voting.objects.get(date="2019-06-16")
        yyy = Voting.objects.get(links_to_menu="yyy")
        xxx = Voting.objects.get(result="0")
