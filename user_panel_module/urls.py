from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPannelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_profile_page')
]
