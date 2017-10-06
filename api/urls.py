from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^long-text/', views.long_text),
]
