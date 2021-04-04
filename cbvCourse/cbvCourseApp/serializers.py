from rest_framework import serializers
from cbvCourseApp.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields=['id','name','description','ratings']
