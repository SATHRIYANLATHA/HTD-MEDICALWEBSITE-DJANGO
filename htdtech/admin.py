from django.contrib import admin

from .models import  Session, Course, Prevyearinfo

class AdminPrevyearinfo(admin.ModelAdmin):
    list_display=('Session', 'Course', 'Prospectus', 'Meritlist' ,'Schedule' , 'Allottedlist' , 'Amendments' , 'Cutoff' )
    
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Prevyearinfo, AdminPrevyearinfo)













# from .models import prevyearinfo  # Import the model

# Register your model here

# admin.site.register(prevyearinfo)
