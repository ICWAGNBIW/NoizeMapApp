from django.urls import path
from .views import Map, SubmitForm, Form, Index, Edit, Delete, Stat

app_name = 'noizedb'

urlpatterns = [
    path('', Map, name='home'),
    path('Form/', Form, name='Form'),
    path('Form/SubmitForm/', SubmitForm, name='SubmitForm'),
    path('MyMeasures/', Index, name='MyMeasures'),
    path('MyMeasures/Edit/<int:id>', Edit, name='Edit<int:id>'),
    path('MyMeasures/Delete/<int:id>', Delete, name='Delete<int:id>'),
    path('stats/', Stat, name='Stats'),
]