from django.urls import path
from .views import (
    ExerciseListCreateView,
    ExerciseDetailView,
    WorkoutPlanListCreateView,
    WorkoutPlanDetailView,
    UserRegistrationView,
    CurrentUserView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Workout API!",
        "endpoints": [
            "token/ - Obtain JWT token",
            "token/refresh/ - Refresh JWT token",
            "register/ - Register a new user",
            "user/me/ - Get current user info",
            "exercises/ - List and create exercises",
            "exercises/<id>/ - Retrieve, update, or delete an exercise",
            "workout-plans/ - List and create workout plans",
            "workout-plans/<id>/ - Retrieve, update, or delete a workout plan"
        ]
    })

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('user/me/', CurrentUserView.as_view(), name='current-user'),
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),
    path('workout-plans/', WorkoutPlanListCreateView.as_view(), name='workout-plan-list-create'),
    path('workout-plans/<int:pk>/', WorkoutPlanDetailView.as_view(), name='workout-plan-detail'),
    path('', api_root, name='api-root'),  # Default route for 'api/'
]