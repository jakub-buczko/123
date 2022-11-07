from django.contrib import admin

from .models import Question, Choice, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pub_date','question_text']
    list_filter = ('pub_date','question_text')
    search_fields = ('pub_date','question_text')

    def get_question(self, obj):
        return obj.question.question_text

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['get_question','choice_text','votes']
    list_filter = ('question', 'votes',)
    search_fields = ('choice_text', 'question__question_text')

    def get_question(self,obj):
        return obj.question.question_text

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text','get_question']
    list_filter = ['question','answer_text']
    search_fields = ['question','answer_text']

    def get_question(self,obj):
        return obj.question.question_text

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Answer,AnswerAdmin)