from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisment(models.Model):
    title = models.CharField('Заголовок', max_length= 128)
    descrition = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete= models.CASCADE)
    image = models.ImageField('изображение', upload_to='page/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: green; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%D.%m.%Y в %H:%M:%S')
    
    @admin.display(description = 'фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src = "{url}" style = "max-width: 40px; max-height: 40px;">', url = self.image.url
            )
# Create your models here.
