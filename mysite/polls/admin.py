from django.contrib import admin
from .models import *

# Register your models here.
# CRUD
# admin은 커스터마이징 할것을 알려줌

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields' : ['question_text']}),
        ('생성일', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInLine]
    list_filter =['pub_date']
    search_fields = ['question_text','choice__choice_text']

admin.site.register(Question, QuestionAdmin)