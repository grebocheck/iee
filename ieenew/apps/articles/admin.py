from django.contrib import admin
from .models import Article , Coment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title' ,'author', 'pub_data' , 'article_image']
    class Meta:
        model = Article

admin.site.register(Article ,ArticleAdmin) 

class ComentAdmin(admin.ModelAdmin):
    list_display = ['article' , 'author_name' , 'coment_text', ]
    class Meta:
        model = Coment

admin.site.register(Coment ,ComentAdmin)


