
from django.contrib import admin
from segundo_app.models import Autor, Categoria, Livro, Usuario, Endereco


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ...

@admin.register(Endereco)
class EnderencoAdmin(admin.ModelAdmin):
    ...