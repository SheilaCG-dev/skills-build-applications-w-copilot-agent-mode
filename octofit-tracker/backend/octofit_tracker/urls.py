

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

def get_api_url(component):
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        return f'https://{codespace}-8000.app.github.dev/api/{component}/'
    return f'http://localhost:8000/api/{component}/'

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': get_api_url('users'),
        'teams': get_api_url('teams'),
        'activities': get_api_url('activities'),
        'workouts': get_api_url('workouts'),
        'leaderboard': get_api_url('leaderboard'),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
