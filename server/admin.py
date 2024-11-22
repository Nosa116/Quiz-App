from django.contrib import admin
from .models import Questions

# Option 1: Simple Registration
# admin.site.register(QuizQuestion)

# Option 2: Custom Admin Interface
@admin.register(Questions)
class QuizQuestionAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('question', 'type', 'difficulty', 'category')
    
    # Filters for the sidebar in the admin interface
    list_filter = ('type', 'difficulty', 'category')
    
    # Searchable fields
    search_fields = ('question', 'category')

    # Ordering of the records
    ordering = ('category', 'difficulty')
