from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, WorkListView, WorkTypeListView, WorkTypeRetrieveView, WorkRetrieveView, StockViewSet, ReminderViewSet, RecordViewSet

router = routers.DefaultRouter()
router.register('stock', StockViewSet, basename='stock')
router.register('reminder', ReminderViewSet, basename='reminder')
router.register('record', RecordViewSet, basename='record')

urlpatterns = [
    path('list-work/', WorkListView.as_view(), name='list-work'),
    path('detail-work/<str:pk>/', WorkRetrieveView.as_view(), name='detail-work'),
    path('list-worktype/', WorkTypeListView.as_view(), name='list-worktype'),
    path('detail-worktype/<str:pk>/',
         WorkTypeRetrieveView.as_view(), name='detail-worktype'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]
