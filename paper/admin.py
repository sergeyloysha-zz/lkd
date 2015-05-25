from django.contrib import admin
from paper.models import Paper, Category, Comment

class PaperAdmin(admin.ModelAdmin):
    prepopulated_fields = {'paper_slug': ('paper_title',)}
    list_display = ('paper_title', 'paper_category', 'paper_created', 'paper_author')
    list_filter = ['paper_created']
    search_fields = ['paper_title', 'paper_text']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_title',)}
    list_display = ('category_title', 'category_slug')
    search_fields = ['category_title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'comment_paper', 'comment_author', 'comment_created')
    list_filter = ['comment_created', 'comment_author']

admin.site.register(Paper, PaperAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)