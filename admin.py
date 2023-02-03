from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fields=['pub_date','question_text']
    #list_display=('question_text','pub_date')
    #list_display=['qestion_text','pub_date','was_published_recently']

    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)