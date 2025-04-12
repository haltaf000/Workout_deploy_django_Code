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

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('user/me/', CurrentUserView.as_view(), name='current-user'),
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),
    path('workout-plans/', WorkoutPlanListCreateView.as_view(), name='workout-plan-list-create'),
    path('workout-plans/<int:pk>/', WorkoutPlanDetailView.as_view(), name='workout-plan-detail'),
]
