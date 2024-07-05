
from django.urls import path
from . import views
# . is current dir

#localhost:8000/chai/order
urlpatterns = [
    path('',views.all_chai,name='all_chai'), #name is not necessary
    # path('order/',views.order,name='order'),

]
