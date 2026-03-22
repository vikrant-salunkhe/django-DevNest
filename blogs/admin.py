from django.contrib import admin
from .models import Category, Blog, Comment

# slug should be auto generated
# when the blog title is very large then it is not possible to write slug manually
# in Django we make it by using prepopulated_fields

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  #as we write in title field the slug is auto generated
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)