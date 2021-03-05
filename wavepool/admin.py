from django import forms
from django.contrib import admin
from wavepool.models import NewsPost


class NewsPostForm(forms.ModelForm):
    model = NewsPost.objects.all()
    fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    # print(NewsPostForm.query)
    form = NewsPostForm
    # print(form.query)


admin.site.register(NewsPost, NewsPostAdmin)
