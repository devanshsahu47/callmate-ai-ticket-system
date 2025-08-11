from django.urls import path
from .views import SubmitTicketView, DashboardView

urlpatterns = [
    path('submit', SubmitTicketView.as_view(), name='submit_ticket'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]
