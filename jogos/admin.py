from django.contrib import admin
from .models import Modalidade, Equipe, Tecnico, Atleta
# Register your models here.

class TecnicoInline(admin.TabularInline):
    model = Tecnico
    extra = 1

class AtletaInline(admin.TabularInline):
    model = Atleta
    extra = 1

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ["nome", "matricula", "equipe"]
    list_filter = ["equipe", "modalidade"]
    search_fields = ['nome']


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']
    inlines = [TecnicoInline, AtletaInline]

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'max_atletas']

admin.site.register(Tecnico)
