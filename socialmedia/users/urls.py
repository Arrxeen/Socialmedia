from django.urls import path
from users.views import RegisterUserView , LoginUserView , exit


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('logout/', exit, name="logout"),
]