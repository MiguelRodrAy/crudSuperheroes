from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Superheroe, League, SuperPower
from .serializers import SuperheroeSerializer, LeagueSerializer, SuperPowerSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def superheroesApi(request, id=0):
    # Read superheroes data
    if request.method == 'GET':
        if id == 0:
            superheroes = Superheroe.objects.all()
            serializer = SuperheroeSerializer(superheroes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                superheroe = Superheroe.objects.get(pk=id)
                serializer = SuperheroeSerializer(superheroe)
                return JsonResponse(serializer.data, safe=False)
            except Superheroe.DoesNotExist:
                return JsonResponse({"error": "Superheroe not found"}, status=404)

    # Create a new superheroe
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuperheroeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "Superheroe created successfully",
                "superheroe": serializer.data
            }, status=201)
        return JsonResponse(serializer.errors, status=400)

    # Update an existing superheroe
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            superheroe = Superheroe.objects.get(pk=id)
        except Superheroe.DoesNotExist:
            return JsonResponse({"error": "Superheroe not found"}, status=404)

        serializer = SuperheroeSerializer(superheroe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "Superheroe updated successfully",
                "superheroe": serializer.data
            })
        return JsonResponse(serializer.errors, status=400)

    # Delete a superheroe
    elif request.method == 'DELETE':
        try:
            superheroe = Superheroe.objects.get(pk=id)
            superheroe.delete()
            return JsonResponse({"message": "Superheroe deleted successfully"}, status=200)
        except Superheroe.DoesNotExist:
            return JsonResponse({"error": "Superheroe not found"}, status=404)

@csrf_exempt
def superpowersApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            superpowers = SuperPower.objects.all()
            serializer = SuperPowerSerializer(superpowers, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                superpower = SuperPower.objects.get(pk=id)
                serializer = SuperPowerSerializer(superpower)
                return JsonResponse(serializer.data, safe=False)
            except SuperPower.DoesNotExist:
                return JsonResponse({"error": "SuperPower not found"}, status=404)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuperPowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "SuperPower created successfully",
                "superpower": serializer.data
            }, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            superpower = SuperPower.objects.get(pk=id)
        except SuperPower.DoesNotExist:
            return JsonResponse({"error": "SuperPower not found"}, status=404)

        serializer = SuperPowerSerializer(superpower, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "SuperPower updated successfully",
                "superpower": serializer.data
            })
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            superpower = SuperPower.objects.get(pk=id)
            superpower.delete()
            return JsonResponse({"message": "SuperPower deleted successfully"}, status=200)
        except SuperPower.DoesNotExist:
            return JsonResponse({"error": "SuperPower not found"}, status=404)


@csrf_exempt
def leaguesApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            leagues = League.objects.all()
            serializer = LeagueSerializer(leagues, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                league = League.objects.get(pk=id)
                serializer = LeagueSerializer(league)
                return JsonResponse(serializer.data, safe=False)
            except League.DoesNotExist:
                return JsonResponse({"error": "League not found"}, status=404)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LeagueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "League created successfully",
                "league": serializer.data
            }, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            league = League.objects.get(pk=id)
        except League.DoesNotExist:
            return JsonResponse({"error": "League not found"}, status=404)

        serializer = LeagueSerializer(league, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "message": "League updated successfully",
                "league": serializer.data
            })
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            league = League.objects.get(pk=id)
            league.delete()
            return JsonResponse({"message": "League deleted successfully"}, status=200)
        except League.DoesNotExist:
            return JsonResponse({"error": "League not found"}, status=404)
        
@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
