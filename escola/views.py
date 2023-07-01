from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    #Exibindo todos os alunos e alunas
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer