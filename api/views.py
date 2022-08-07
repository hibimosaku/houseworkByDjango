from rest_framework import generics
from rest_framework import viewsets
from .models import Work, WorkType, Stock, Reminder, Record
from .serializers import UserSerializer, WorkSerializer, WorkTypeSerializer, StockSerializer, ReminderSerializer, RecordSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class WorkListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class WorkRetrieveView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class WorkTypeListView(generics.ListAPIView):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer


class WorkTypeRetrieveView(generics.RetrieveAPIView):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
