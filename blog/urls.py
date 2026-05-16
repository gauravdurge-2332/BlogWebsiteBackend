from django.urls import path , include 


from .views import * 

urlpatterns = [
    path("" , Postapiview.as_view() , name='getAllpost') ,
    path('catg/' ,CategoryApiview.as_view() , name='tempdatapost' ),
    path('tags/' ,TagApiView.as_view() , name='tagkapost' )


]