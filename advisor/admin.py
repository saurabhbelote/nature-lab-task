from .models import advisor, booking
from django.contrib import admin


class advisorAdmin(admin.ModelAdmin):
    model = advisor
    list_display = ('Advisor_name', 'Advisor_Photo')


    def Advisor_Photo_URL(self, obj):
        return obj.Advisor_Photo_URL

    Advisor_Photo_URL.short_description = 'Advisor_Photo Preview'
    Advisor_Photo_URL.allow_tags = True

admin.site.register(advisor,advisorAdmin)    


class bookingAdmin(admin.ModelAdmin):
    model = booking
    list_display = ( 'booking_id','user','time','contact_date','advisor')
admin.site.register(booking,bookingAdmin)    

 

