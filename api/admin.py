from django.contrib import admin
from .models import (WorkType, Work, Stock, Reminder, Record)

admin.site.register([WorkType, Work, Stock, Reminder, Record])
