from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner,Question,Choice,Submission

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class ChoiceInline(admin.StackedInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]
admin.site.register(Question ,QuestionAdmin)

class QuestionLinkInline(admin.TabularInline):
    model = Question
    fields = ('txt_question', 'question_grade')
    # Django 1.8 introduced this, no need to make your own link
    show_change_link = True

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionLinkInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)