from rest_framework import serializers 
from .models import Book, Author, Department, Student 
 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['code', 'value', 'data'] 

class DepartmentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['code', 'name', 'student']

    def get_student(self, obj):
        value_param = self.context['request'].query_params.get('value')
        if not value_param:
            return None

        student = Student.objects.filter(code=obj.code, value=value_param) 
        if student:
            return StudentSerializer(student, many = True).data
        return None 