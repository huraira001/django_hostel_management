from django.urls import path
from django.views import View
from . import views 


urlpatterns = [
    path('',views.home , name = 'home'),
    path('student/',views.Student, name = 'student'),
    path('mess_manager/',views.mess_manager, name = 'mm'),
    path('resident_tutor/',views.resident_tutor, name = 'rt' ),
    path('data/',views.data, name = 'data' ),
    path('sadd/',views.sadd, name = 'sadd' ),
    path('student_management/',views.student_management, name = 'student_management' ),
    
    
    ]



