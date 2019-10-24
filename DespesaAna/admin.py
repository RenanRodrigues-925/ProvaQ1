from django.contrib import admin
from .models import Despesa


class DespesaAdmin(admin.ModelAdmin):
        list_display = ('data_criacao','tipo_despesa','descricao','forma_pagamento',
                'vencimento','quitado',
                'ProximoVencimento',
        )

        list_filter = ('quitado','vencimento')
        date_hierarchy = ('vencimento')

        def ProximoVencimento(self,obj):
            return True

            ProximoVencimento.short_description = "Próximo Vencimento"
            ProximoVencimento = True

admin.site.register(Despesa, DespesaAdmin)
