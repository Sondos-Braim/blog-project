from django.urls import path,include
from .views import blog_view,details_view

urlpatterns = [
    path('',blog_view.as_view(),name='home'),
    path('<int:pk>/',details_view.as_view(),name='details')
]