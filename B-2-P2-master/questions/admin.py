from django.contrib import admin
from .models import Question, QuestionComment

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)

class QuestionCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuestionComment, QuestionCommentAdmin)