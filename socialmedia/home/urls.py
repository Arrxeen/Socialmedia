from django.urls import path
from home.views import index, CreatePostView, CategoryView

urlpatterns = [
    path('', index, name="home"),
    path('mkpost/', CreatePostView.as_view(), name="mkpost"),
    path('category/<pk>', CategoryView.as_view(), name="category"),
]