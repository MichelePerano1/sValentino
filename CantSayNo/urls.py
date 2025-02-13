from django.urls import path
from .views import *

urlpatterns=[
    path('', sanVal_view),
    path('si', yes_view, name='siResp')
]