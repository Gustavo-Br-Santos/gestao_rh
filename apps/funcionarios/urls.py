from django.urls import path, include
from .views import FuncionariosList, FuncionariosEdit, FuncionarioDelete, FuncionarioNovo

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('create/', FuncionarioNovo.as_view(), name='create_funcionario'),
]
