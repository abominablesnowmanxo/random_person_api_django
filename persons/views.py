from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET', 'POST'])
def list_create(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    persons = Person.objects.all()
    serilalizer = PersonSerializer(persons, many=True)
    return Response(serilalizer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_update_delete(request, pk):
    person = Person.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        person.delete()
        return Response('User was deleted')
