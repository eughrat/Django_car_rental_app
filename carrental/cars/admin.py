from django.contrib import admin
from .models import Car, CarDetail, CarMain, Booking, Comment


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['get_main_brand', 'get_main_model', 'get_detail_production_date']

    def get_main_brand(self, obj):
        return obj.main.brand

    def get_main_model(self, obj):
        return obj.main.model

    def get_detail_production_date(self, obj):
        return obj.detail.production_date

    get_main_brand.admin_order_field = "brand"
    get_main_brand.short_description = "Brand"
    get_main_model.admin_order_field = "model"
    get_main_model.short_description = "Model"
    get_detail_production_date.admin_order_field = "production_date"
    get_detail_production_date.short_description = "Production Date"

admin.site.register(Car, CarAdmin)
admin.site.register(CarDetail)
admin.site.register(CarMain)
admin.site.register(Booking)
admin.site.register(Comment)