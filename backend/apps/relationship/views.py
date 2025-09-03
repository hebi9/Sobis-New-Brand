
from django.http import JsonResponse
from .models import Relationship, Streak
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def relationship(request):
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            if not username:
                return JsonResponse({"error": "Username is required"}, status=400)
            user = User.objects.get(username=username)
            relationship_id = request.GET.get('relationship')
            if relationship_id:
                relationships = [Relationship.objects.get(id=relationship_id)]
            else:
                relationships = Relationship.objects.filter(user=user)
            streak = Streak.objects.filter(user=user)
            data = [
                {
                    "id": relation.id,
                    'user': relation.user.username,
                    'estatus': relation.estatus,
                    'note': relation.note,
                    'dessert': relation.dessert,
                    'create': relation.create.strftime("%d-%m-%Y"),
                    'empathy': relation.empathy,
                    'comprehension': relation.comprehension,
                    'curiosity': relation.curiosity,
                    'learn_more': relation.learn_more,
                    'learn_from_you': relation.learn_from_you,
                    'miracle': relation.miracle
                }
                for relation in relationships
            ]
            return JsonResponse({
                'success': True,
                'relationships': data,
                'streak': list(streak.values())[0] if streak.exists() else {},
            }, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'POST':
        try:
            data = request.data if hasattr(request, 'data') else json.loads(request.body)
            relationship_id = data.get('id')
            if relationship_id:
                relationship = Relationship.objects.get(id=relationship_id)
                relationship.estatus = data.get('estatus')
                relationship.note = data.get('note')
                relationship.dessert = data.get('dessert')
                relationship.empathy = data.get('empathy')
                relationship.comprehension = data.get('comprehension')
                relationship.curiosity = data.get('curiosity')
                relationship.learn_more = data.get('learn_more')
                relationship.learn_from_you = data.get('learn_from_you')
                relationship.miracle = data.get('miracle')
                relationship.save()
                return JsonResponse({'success': True}, status=200)
            username = data.get('username')
            if not username:
                return JsonResponse({"error": "Username is required"}, status=400)
            user = User.objects.get(username=username)
            relationship = Relationship.objects.create(
                user=user,
                estatus=data.get('estatus'),
                note=data.get('note'),
                dessert=data.get('dessert'),
                create=data.get('create'),
                empathy=data.get('empathy'),
                comprehension=data.get('comprehension'),
                curiosity=data.get('curiosity'),
                learn_more=data.get('learn_more'),
                learn_from_you=data.get('learn_from_you'),
                miracle=data.get('miracle')
            )
            return JsonResponse({'success': True, 'relationship_id': relationship.id}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def relationship_detail(request, pk):
    try:
        relation = Relationship.objects.get(id=pk)
        data = {
            "id": relation.id,
            "estatus": relation.estatus,
            "note": relation.note,
            "dessert": relation.dessert,
            "create": relation.create.strftime("%Y-%m-%d"),
            "empathy": relation.empathy,
            "comprehension": relation.comprehension,
            "curiosity": relation.curiosity,
            "learn_more": relation.learn_more,
            "learn_from_you": relation.learn_from_you,
            "miracle": relation.miracle,
            "username": relation.user.username,
        }
        return JsonResponse(data, status=200)
    except Relationship.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)