from django import forms
from django.contrib import admin
from news.models import News, Category, UserSettings
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id', 'title', 'category', 'created_at', 'updated_at', 'is_published'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    
    
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')
    readonly_fields = (
        # 'phone_verification_code', 'telegram_verification_code',
        'is_phone_verified', 'is_telegram_verified'
    )
    

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserSettings, UserSettingsAdmin)
