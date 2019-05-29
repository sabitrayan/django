from django.urls import path
from myapp import views

urlpatterns = [
    path('myapp/review_lists/', views.ReviewList.as_view()),
    path('myapp/login/', views.login),
    path('myapp/logout/', views.logout),
]