from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Pay
from .serializers import PaysSerializer
from .permissions import IsOwner

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def pay_list(request):
    if request.method == 'GET':
        pays = Pay.objects.filter(owner=request.user)
        serializer = PaysSerializer(pays, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = PaysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwner])
def pay_detail(request, id):
    try:
        pay = Pay.objects.get(id=id, owner=request.user)
    except Pay.DoesNotExist:
        return JsonResponse({'error': 'Pay not found'}, status=404)

    if request.method == 'GET':
        serializer = PaysSerializer(pay)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = PaysSerializer(pay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        pay.delete()
        return JsonResponse({'message': 'Pay deleted'}, status=204)

