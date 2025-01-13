from django.urls import path
from .views import BankListView, BranchListView

urlpatterns = [
    # List of banks
    path('bank/', BankListView.as_view(), name='bank-list'),
    # Single branch details by ifsc
    path('branch/<str:ifsc>/', BranchListView.as_view(), name='branch-detail'),
]
