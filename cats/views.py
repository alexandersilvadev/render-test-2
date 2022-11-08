from rest_framework.generics import ListCreateAPIView
from .models import Cat
from .serializers import CatsSerializer

class CatView(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer
