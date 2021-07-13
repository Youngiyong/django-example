from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

# from ..tutorials.models import Tutorial
from serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def tutorial(request):
    if request.method == 'POST':

        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        print(tutorial_serializer)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer, status=status.HTTP_201_CREATED)
# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     pass
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     # find tutorial by pk (id)

    # tutorial = Tutorial.objects.get(pk=pk)

