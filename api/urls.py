from django.conf.urls import url

from .views import SubscriberView

app_name = 'api'
urlpatterns = [
    url(r'^subscriber', SubscriberView.as_view(), name="subscriber"),
]
