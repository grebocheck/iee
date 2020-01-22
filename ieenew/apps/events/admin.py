from django.contrib import admin
from .models import Event , Member

class EventAdmin(admin.ModelAdmin):
    list_display = ["title_event" ,"event_img", "date_post" , "date_do"]
    class Meta:
        model = Event

admin.site.register(Event , EventAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ["event","name_member" , "contact" , "born_date"]
    class Meta:
        model = Member

admin.site.register(Member , MemberAdmin)