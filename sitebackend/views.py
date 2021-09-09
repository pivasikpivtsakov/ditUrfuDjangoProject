from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .direction_selector import select_directions
from .models import DirectionGroup
from .serializers import DirectionGroupSerializer

# Create your views here.


class DirectionGroupViewSet(viewsets.ModelViewSet):
    queryset = DirectionGroup.objects.all().order_by('code')
    serializer_class = DirectionGroupSerializer


@api_view(['POST'])
def apply_selected_to_db(request):
    data = JSONParser().parse(request)
    serializer = serializers.ListSerializer(data=data, child=serializers.CharField(), allow_empty=True, allow_null=False)
    if serializer.is_valid(raise_exception=True):
        codes = serializer.validated_data
        select_directions(codes)
        return Response()
