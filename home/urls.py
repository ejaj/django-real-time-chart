from django.urls import path
from .views import HomeView, GraphChartView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('graph/chart', GraphChartView.as_view(), name='graph_chart'),
]
