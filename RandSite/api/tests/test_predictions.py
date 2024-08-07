from django.test import TestCase
from django.urls import reverse
from ..models import Predictions


class RandomPredictionViewTests(TestCase):
    def setUp(self):
        # Создаем тестовые прогнозы
        Predictions.objects.create(id=10, name="Прогноз 1")
        Predictions.objects.create(id=11, name="Прогноз 2")
        Predictions.objects.create(id=12, name="Прогноз 3")

    def test_get_with_predictions(self):
        url = reverse('prediction')
        response = self.client.get(url)

        # Проверяем статус-код и содержимое ответа
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json())

    def test_get_with_no_predictions(self):
        Predictions.objects.all().delete()  # Удаляем все прогнозы
        url = reverse('prediction')
        response = self.client.get(url)

        # Проверяем статус-код и содержимое ответа
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())