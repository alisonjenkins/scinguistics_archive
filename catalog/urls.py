from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('lessons/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('types/', views.TypeListView.as_view(), name='types'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('lesson/create/', views.LessonCreate.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/update/', views.LessonUpdate.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete/', views.LessonDelete.as_view(), name='lesson-delete'),
    path('student/create/', views.StudentCreate.as_view(), name='student-create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),
    path('teacher/create/', views.TeacherCreate.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update/', views.TeacherUpdate.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete/', views.TeacherDelete.as_view(), name='teacher-delete'),
    path('type/create/', views.TypeCreate.as_view(), name='type-create'),
    path('type/<int:pk>/update/', views.TypeUpdate.as_view(), name='type-update'),
    path('type/<int:pk>/delete/', views.TypeDelete.as_view(), name='type-delete'),
    path('tag/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
]
