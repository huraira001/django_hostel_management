from django.contrib import admin
from .models import *
 

admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions) 
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(Eats)
admin.site.register(HostelManager)
admin.site.register(Hostels)
admin.site.register(Mess)
admin.site.register(ResidentTutor)
admin.site.register(Room)
admin.site.register(Servants)
admin.site.register(Student)
