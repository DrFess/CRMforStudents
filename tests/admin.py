from django.contrib import admin
from .models import Category, Question, StudentAnswers, TotalStudentAnswers


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'theme')
    search_fields = ('text', 'theme')


class StudentAnswersAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'theme', 'text', 'correct_answer', 'student_answer', 'date')
    search_fields = ('student_id', 'theme', 'date')


class TotalStudentAnswersAdmin(admin.ModelAdmin):
    list_display = ('total_student_id', 'total_theme', 'total_text', 'total_correct_answer', 'total_student_answer', 'total_date')


admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(StudentAnswers, StudentAnswersAdmin)
admin.site.register(TotalStudentAnswers, TotalStudentAnswersAdmin)

