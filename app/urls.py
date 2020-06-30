from django.urls import path
from app import views

app_name="app"
urlpatterns=[
    path('emp/',views.EmployeeAPIView.as_view()),
    path("emp/<str:pk>/",views.EmployeeAPIView.as_view()),
]