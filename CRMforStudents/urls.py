"""
URL configuration for CRMforStudents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tests.views import (
    AllQuestionsAPIView,
    AllTestCategoriesAPIView,
    QuestionsByCategoryAPIView,
    AddQuestionAPIView,
    AddStudentAnswerAPIView,
    TotalStudentAnswerAPIView,
    GetStudentResultAPIView
)

from students.views import (
    get_all_groups,
    geolocation_view,
    get_all_profiles,
    get_profiles_by_parameter,
    get_field_values,
    add_profile,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/all', AllQuestionsAPIView.as_view()),
    path('api/v1/test_categories/all', AllTestCategoriesAPIView.as_view()),
    path('api/v1/test_by_categorie', QuestionsByCategoryAPIView.as_view()),
    path('api/v1/geolocation', geolocation_view),
    path('api/v1/get_groups', get_all_groups),
    path('api/v1/get_all_profiles', get_all_profiles),
    path('api/v1/get_profiles_by_parameter', get_profiles_by_parameter),
    path('api/v1/get_field_values', get_field_values),
    path('api/v1/add_profile', add_profile),
    path('api/v1/add_question', AddQuestionAPIView.as_view()),
    path('api/v1/add_student_answer', AddStudentAnswerAPIView.as_view()),
    path('api/v1/total_student_answers', TotalStudentAnswerAPIView.as_view()),
    path('api/v1/get_student_result', GetStudentResultAPIView.as_view()),
    # path('bots/bot.py/', include('aiogram.contrib.fsm_storage.django_views')),
]
