from django.contrib import admin
from .models import Contato
from django.utils.html import format_html

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'mensagem', 'whatsapp_link')
    list_display_links = ('nome',)
    search_fields = ('nome', 'telefone', 'email')

    def whatsapp_link(self, obj):
        # Limpa o número — tira espaços e caracteres
        tel = ''.join(filter(str.isdigit, obj.telefone))
        # Se começar por 0, troca por +244 (código de Angola)
        if tel.startswith('0'):
            tel = '+244' + tel[1:]
        # Cria o link direto do WhatsApp
        mensagem = f"Olá {obj.nome}! Recebemos a tua mensagem pelo site. 😊"
        link = f"https://wa.me/{tel}?text={mensagem.replace(' ', '%20')}"
        return format_html(
            '<a href="{}" target="_blank" style="background:#25D366; color:white; padding:6px 12px; '
            'border-radius:6px; text-decoration:none; font-weight:bold;">💬 WhatsApp</a>',
            link
        )
    
    whatsapp_link.short_description = "Responder"

admin.site.register(Contato, ContatoAdmin)
