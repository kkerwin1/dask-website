from django.contrib import admin

# Register your models here.

from .models import Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines         = [ChoiceInline]
    list_display    = ("question_text", "pub_date", "was_published_recently")
    list_filter     = ["pub_date"]
    search_fields   = ["question_text"]
    
    fieldsets       = [
        (None,               {"fields": [question_text]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)
