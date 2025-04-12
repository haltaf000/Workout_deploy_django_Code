from django.db import models
from django.conf import settings

# Basic Exercise model storing details about exercises
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)
    equipment = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=20)  # e.g., Beginner, Intermediate, Advanced
    video_url = models.URLField(blank=True, null=True)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

# WorkoutPlan model for saving user-specific plans 
class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # ManyToMany to exercises through a custom through model for ordering/customization
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return f"{self.name} ({self.user.username})"

# Through model to hold extra details for each exercise in a workout plan
class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # order of the exercise in the workout plan
    custom_sets = models.PositiveIntegerField(blank=True, null=True)
    custom_reps = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('workout_plan', 'exercise')
        ordering = ['order']

    def __str__(self):
        return f"{self.exercise.name} in {self.workout_plan.name}"
