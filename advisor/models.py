from django.db import models
from django.db.models.fields import related
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from authentication.models import User 

class advisor(models.Model):
    advisor_id = models.AutoField(primary_key=True,unique= True)
    Advisor_name = models.CharField(max_length=150)
    Advisor_Photo_URL = models.ImageField(upload_to ='img')

    @property
    def Advisor_Photo(self):
        if self.Advisor_Photo_URL:
            _thumbnail = get_thumbnail(self.Advisor_Photo_URL,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    


class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='user+')
    advisor = models.ForeignKey(advisor, on_delete=models.DO_NOTHING,related_name='advisor')
    booking_id = models.AutoField(primary_key=True,unique= True,serialize=True)
    time = models.TimeField(auto_now_add=True, blank=False)  
    contact_date = models.DateField(auto_now_add=True, blank=False)



