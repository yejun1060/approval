from django.contrib import admin
from .models import User, UserAuth, AuthInfo


# separate AutoInfo filed
class AuthInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'description']}),
        ('Date Information', {'fields': ['created_date']}),
        ('Valid Information (0: false, 1: true(default))', {'fields': ['is_valid']}),
    ]
    list_display = ('id', 'name', 'created_date')
    list_filter = ['is_valid']
    search_fields = ['name']


# separate filed
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': ['last_name', 'first_name', 'nickname']}),
        ('Login Information', {'fields': ['email', 'password']}),
        ('Date Information', {'fields': ['joined_date']}),
        ('other Informations - 1 (0: false, 1: true(default))', {'fields': ['is_active']}),
        ('other Informations - 2 (0: false(default), 1: true)', {'fields': ['is_staff', 'is_superuser']}),
    ]
    list_display = ('id', 'last_name', 'first_name', 'joined_date', 'is_staff')
    list_filter = ['joined_date', 'is_active', 'is_staff']
    search_fields = ['nickname', 'last_name']


# separate filed
class UserAuthAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['UserId', 'AuthId']}),
        ('Date Information', {'fields': ['given_date', 'modified_date']}),
        ('Valid Information (0: false, 1: true(default))', {'fields': ['is_valid', 'authorization']}),
    ]
    list_display = ('id', 'UserId', 'authorization', 'modified_date', 'AuthId')
    list_filter = ['authorization', 'modified_date']


# add admin site
admin.site.register(User, UserAdmin)
admin.site.register(UserAuth, UserAuthAdmin)
admin.site.register(AuthInfo, AuthInfoAdmin)