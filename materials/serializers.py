from rest_framework.serializers import ModelSerializer, SerializerMethodField
from validators import YouTubeValidation

from materials.models import Course, Lesson, Subscription


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidation(field="video_link")]


class CourseSerializer(ModelSerializer):
    count_of_lesson = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_count_of_lesson(self, course):
        return course.lessons.count()

    def get_lessons(self, course):
        lessons_set = Lesson.objects.filter(course=course.id)
        return [lesson.name for lesson in lessons_set]

    class Meta:
        model = Course
        fields = ("name", "preview", "description", "count_of_lesson", "lessons", "owner")


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
