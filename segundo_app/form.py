from django.forms import ModelForm
from .models import Livro

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "descricao", "categoria", "isbn", "genero", "edicao", "valor"]