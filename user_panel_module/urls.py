from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPannelDashboardPage.as_view(), name='user_panel_dashboard')
]
