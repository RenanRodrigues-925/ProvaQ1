from django.contrib import admin
from .models import Despesa

class DespesaAdmin(admin.ModelAdmin):
        list_display = ('data_criacao','descricao','vencimento','quitado')

admin.site.register(Despesa, DespesaAdmin)
