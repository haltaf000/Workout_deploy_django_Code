from django.contrib import admin
from .models import Exercise, WorkoutPlan, WorkoutExercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty')
    search_fields = ('name', 'description', 'muscle_group')

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutPlan.exercises.through
    extra = 1

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    inlines = [WorkoutExerciseInline]

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout_plan', 'exercise', 'order')
    list_filter = ('workout_plan', 'exercise')
