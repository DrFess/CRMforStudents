from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Question, StudentAnswers, TotalStudentAnswers
from Serializers.serializer import QuestionSerializer, StudentAnswerSerializer, TotalStudentAnswerSerializer

from bots.utils.same_functions import calculate_result


class AllQuestionsAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all().values()
        return Response(list(questions))


class AllTestCategoriesAPIView(APIView):
    def get(self, request):
        answer = Category.objects.all().values()
        return Response(list(answer))


class QuestionsByCategoryAPIView(APIView):
    def get(self, request):
        try:
            questions = Question.objects.filter(
                theme_id=int(request.body)).values('id', 'text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer')
            return Response(list(questions))
        except Exception:
            return Response({'status': 500})


class AddQuestionAPIView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AddStudentAnswerAPIView(APIView):
    def post(self, request):
        serializer = StudentAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TotalStudentAnswerAPIView(APIView):
    def get(self, request):
        length_total_test = Question.objects.all().count()
        total_student_answers = TotalStudentAnswers.objects.filter(
            total_student_id=request.data['total_student_id'],
            total_date=request.data['total_date']
        ).values('total_student_answer', 'total_correct_answer')
        result = calculate_result(total_student_answers, length_total_test, 'total_student_answer', 'total_correct_answer')
        return Response({'result': result})

    def post(self, request):
        serializer = TotalStudentAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetStudentResultAPIView(APIView):
    def get(self, request):
        length_test = Question.objects.filter(theme_id=request.data['theme_id']).count()
        student_answers = StudentAnswers.objects.filter(
            student_id=request.data['student_id'],
            theme=request.data['theme_id'],
            date=request.data['date']
        ).values('student_answer', 'correct_answer')
        result = calculate_result(student_answers, length_test, 'student_answer', 'correct_answer')
        return Response({'result': result})
