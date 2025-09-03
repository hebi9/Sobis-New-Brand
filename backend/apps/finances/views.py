from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.db.models import Q
from .models import Finances, Category, Payment_method
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
import json
from datetime import datetime

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def finances(request):
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            if not username:
                return JsonResponse({"error": "Username is required"}, status=400)

            user = User.objects.get(username=username)
            categories = Category.objects.filter(user=user)
            payment_methods = Payment_method.objects.filter(user=user)
            category = request.GET.get('category')
            payment_method = request.GET.get('payment_method')
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')

            finances = Finances.objects.filter(user=user).select_related("category", "payment_method")
            # Filtros
            if category:
                finances = finances.filter(category__name=category)
            if payment_method:
                finances = finances.filter(payment_method__name=payment_method)
            if start_date:
                finances = finances.filter(create__gte=start_date)
            if end_date:
                finances = finances.filter(create__lte=end_date)

            data = [
                {
                    "id": finance.id,
                    "amount": float(finance.amount),
                    "create": finance.create.strftime("%d-%m-%Y"),
                    "category": finance.category.name,
                    "payment_method": finance.payment_method.name,
                    "type": finance.type,
                    "note": finance.note,
                }
                for finance in finances
            ]

            cat = [{"name": cat.name} for cat in categories]
            payment = [{"name": payment.name} for payment in payment_methods]
            return JsonResponse({
                'success': True,
                'finances': data,
                'categories': cat,
                'payment_methods': payment
            }, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'POST':
        try:
            data = request.data if hasattr(request, 'data') else json.loads(request.body)
            print(request.data)
            username = data.get('username')
            if not username:
                return JsonResponse({"error": "Username is required"}, status=400)

            user = User.objects.get(username=username)
            category_name = data.get('category')
            category, _ = Category.objects.get_or_create(user=user, name=category_name)
            payment_method_name = data.get('payment_method')
            payment_method, _ = Payment_method.objects.get_or_create(user=user, name=payment_method_name)

            finances = Finances.objects.create(
                user=user,
                amount=data.get('amount'),
                category=category,
                payment_method=payment_method,
                type=data.get('type'),
                note=data.get('note'),
                create=data.get('create'),
            )

            return JsonResponse({'success': True, 'finances_id': finances.id}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)