from django.contrib import admin
from django.urls import path
from escola.views import AlunosViewSet, CursosViewSet

#Registrar rotas
router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos),
]
