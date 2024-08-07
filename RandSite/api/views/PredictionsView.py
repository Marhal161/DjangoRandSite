from django.views.generic import View
from django.http import JsonResponse
from ..models import Predictions
import random


class RandomPredictionView(View):
    @staticmethod
    def get(request):
        try:
            predictions = Predictions.objects.all()
            if predictions.exists():
                prediction = random.choice(list(predictions))
                # Отправка JSON-ответа
                return JsonResponse({'prediction': prediction.name})
            else:
                return JsonResponse({'error': 'Прогнозов не найдено.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Ошибка: {str(e)}'}, status=500)