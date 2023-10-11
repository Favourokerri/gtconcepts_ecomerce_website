from django.contrib import admin
from user_profile.models import Profile, ShippingFee
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified',)
    list_filter = ('user', 'is_verified')
    search_fields = ('user__username', 'user__email')

class ShippingFeeAdmin(admin.ModelAdmin):
    list_display = ('location', 'fee')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(ShippingFee, ShippingFeeAdmin)