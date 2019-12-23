from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Restaurant', views.RestaurantViewSet)
router.register(r'Menu', views.MenuViewSet)
router.register(r'Voting', views.VotingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    path('api/likestoggle/', views.LikeAPIToggle.as_view()),
    path('api/todayresult/', views.TodaysResult.as_view())
]
