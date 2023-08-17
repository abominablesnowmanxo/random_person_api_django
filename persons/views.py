from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSerializer


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    lookup_url_kwarg = 'pk'


# @api_view(['GET', 'POST'])
# def list_create(request):
#     if request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     persons = Person.objects.all()
#     serilalizer = PersonSerializer(persons, many=True)
#     return Response(serilalizer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def retrieve_update_delete(request, pk):
#     person = get_object_or_404(Person, pk=pk)

#     if request.method == 'GET':
#         serializer = PersonSerializer(person, many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = PersonSerializer(instance=person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         person.delete()
#         return Response('User was deleted')
