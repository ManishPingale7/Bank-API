from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
# Create your views here.


class BankListView(APIView):
    # API endpoint that allows banks to be viewed or edited.
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)


class BranchListView(APIView):
    # API endpoint that allows branches to be viewed or edited.
    def get(self, request, ifsc):
        try:
            branch = Branch.objects.get(ifsc=ifsc)
            serializer = BranchSerializer(branch)
            return Response(serializer.data)
        except Branch.DoesNotExist:
            return Response({"error": "Branch not found "},
                            status=status.HTTP_404_NOT_FOUND)
