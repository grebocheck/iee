from django.db import models

class Event(models.Model):
    title_event = models.TextField( max_length = 200, verbose_name = 'Назва івенту')
    event_article = models.TextField( verbose_name = 'Опис івенту')
    event_img = models.ImageField(height_field=None, width_field=None,null = True , blank = True , upload_to = "images/events/" , verbose_name = 'Картинка івенту' )
    date_post = models.DateTimeField('Дата створення посту')
    date_do = models.DateField('Дата початку івенту')

    def __str__(self):
        return self.title_event

    def get_absolute_url(self):
        return '/events/'+str(self.id)+'/'

    class Meta:
        verbose_name = "Івент"
        verbose_name_plural = 'Івенти'

class Member(models.Model):
    event = models.ForeignKey(Event , on_delete = models.CASCADE)
    name_member = models.TextField( max_length= 200 , verbose_name='Імя учасника')
    contact = models.TextField( max_length = 200 , verbose_name='Контакти учасника')
    born_date = models.TextField( max_length=200 , verbose_name = 'Дата народження')
    class Meta:
        
        verbose_name = "Учасник"
        verbose_name_plural = 'Учасники'