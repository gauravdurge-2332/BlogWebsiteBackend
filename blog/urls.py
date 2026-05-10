from django.urls import path , include 


from .views import * 

urlpatterns = [
    path("" , Postapiview.as_view() , name='getAllpost') 
]