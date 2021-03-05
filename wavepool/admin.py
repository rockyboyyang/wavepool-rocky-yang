from django import forms
from django.contrib import admin
from wavepool.models import NewsPost


class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostForm
    
    def get_queryset(self, request):
        queryset = super(NewsPostAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-publish_date')
        return queryset



admin.site.register(NewsPost, NewsPostAdmin)
