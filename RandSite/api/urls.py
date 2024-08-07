from django.urls import path
from .views.PredictionsView import RandomPredictionView

urlpatterns = [
    path('prediction/', RandomPredictionView.as_view(), name='prediction'),
]
