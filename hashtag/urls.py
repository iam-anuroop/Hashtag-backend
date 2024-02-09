from django.urls import path
from .views import (
    ManageHashtags
)



urlpatterns = [
    path("hashtag/", ManageHashtags.as_view(), name="hashtag"),
]