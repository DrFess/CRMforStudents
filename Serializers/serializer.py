from rest_framework import serializers
from students.models import Profile, Group, Geolocation
from tests.models import Question, Category, StudentAnswers, TotalStudentAnswers


class GeolocationSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    telegram_id = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        return Geolocation.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_number', 'id')


class ProfileSerializer(serializers.ModelSerializer):
    group_number = GroupSerializer()

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'group_number', 'telegram_id')

    def create(self, validated_data):
        group_number = validated_data.pop('group_number')['group_number']
        group = Group.objects.get(group_number=group_number)
        return Profile.objects.create(group_number=group, **validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class QuestionSerializer(serializers.ModelSerializer):
    theme = CategorySerializer()

    class Meta:
        model = Question
        fields = ('text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer', 'theme')

    def create(self, validated_data):
        theme = validated_data.pop('theme')['title']
        title = Category.objects.get(title=theme)
        return Question.objects.create(theme=title, **validated_data)


class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswers
        fields = ('student_id', 'date', 'theme', 'correct_answer', 'student_answer', 'text')

    def create(self, validated_data):
        return StudentAnswers.objects.create(**validated_data)


class TotalStudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalStudentAnswers
        fields = ('total_student_id', 'total_date', 'total_theme', 'total_correct_answer', 'total_student_answer', 'total_text')

    def create(self, validated_data):
        return TotalStudentAnswers.objects.create(**validated_data)
