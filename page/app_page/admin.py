from django.contrib import admin
from .models import Advertisment

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'descrition', 'price', 'auction', 'created_date', 'get_html_image']
    list_filter = ['auction', 'created_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)


    fieldsets = (
        ('Общее', {
            'fields': ('title', 'descrition', 'image')
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        })
    )

admin.site.register(Advertisment, AdvertisementAdmin)

# Register your models here.
