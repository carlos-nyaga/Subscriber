
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
#from rest_framework.decorators import api_view
from .serializers import SubscriberSerializer
from .models import Subscriber

# Create your views here.
class SubscriberView(APIView):
    def get(self,request):
        all_subscribers = Subscriber.objects.all()
        serialized_subscribers = SubscriberSerializer(all_subscribers, many = True)
        return Response(serialized_subscribers.data)

    def post(self,request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber_instance = Subscriber.objects.create(**serializer.data)
            return Response({"message": "Created subscriber {}" .format(subscriber_instance.id)})
        else:
            return Response({"errors": serializer.errors},status=HTTP_400_BAD_REQUEST)




'''

@api_view(["GET","POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World!"})
    
    else:
        name = request.data.get("name")
        if not name:
            return Response({"error":"No name passed"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Hello {}!.format(name)"})
'''