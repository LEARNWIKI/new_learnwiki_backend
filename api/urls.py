from django.urls import path

from .views import *


urlpatterns = [
    path("node/", NodeListView.as_view(), name="node"),

]