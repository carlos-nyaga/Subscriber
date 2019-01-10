
from rest_framework.generics import ListCreateAPIView


from .serializers import SubscriberSerializer
from .models import Subscriber

# Create your views here.
class SubscriberView(ListCreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
