from django.contrib import admin

from .models import Question, Choice, Answer

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['get_question','choice_text','votes']
    list_filter = ('question', 'votes',)
    search_fields = ('choice_text', 'question__question_text',)
    def get_question(self,obj):
        return obj.question.question_text

class AnswerAdmin(admin.ModelAdmin):
    fields = ['answer_text','question']
    def get_answer(self,obj):
        return obj.answer.answer_text
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Answer,AnswerAdmin)