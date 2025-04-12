from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutExercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(), source='exercise', write_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'order', 'custom_sets', 'custom_reps', 'exercise', 'exercise_id']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(source='workoutexercise_set', many=True, required=False)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'description', 'created_at', 'exercises', 'user']
        read_only_fields = ['user']

    def validate(self, data):
        if len(data.get('name', '').strip()) < 3:
            raise serializers.ValidationError("Workout name must be at least 3 characters")
            
        exercises_data = data.get('workoutexercise_set', [])
        if not exercises_data:
            raise serializers.ValidationError("At least one exercise is required")
            
        return data

    def validate_workoutexercise_set(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("At least one exercise is required")
        return value
    
