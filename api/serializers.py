from rest_framework import serializers
from .models import Work, WorkType, Stock, Reminder, Record
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = ('id', 'name',)


class WorkSerializer(serializers.ModelSerializer):
    typename = serializers.CharField(read_only=True, source='type.name')

    class Meta:
        model = Work
        fields = ('id', 'name',  'type', 'typename')


class StockSerializer(serializers.ModelSerializer):
    add_workname = serializers.CharField(
        read_only=True, source='add_work.name')
    decrease_workname = serializers.CharField(
        read_only=True, source='decrease_work.name')

    class Meta:
        model = Stock
        fields = ('id', 'name', 'num', 'add_work', 'add_workname',
                  'decrease_work', 'decrease_workname', 'updated_at')


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    workname = serializers.CharField(read_only=True, source='work.name')
    typeid = serializers.IntegerField(read_only=True, source='work.type.id')
    typename = serializers.CharField(read_only=True, source='work.type.name')

    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Record
        fields = ('id', 'work', 'workname', 'typeid',
                  'typename', 'num', 'created_at')
