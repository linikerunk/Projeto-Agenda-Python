from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin): # crio por convenção dessa maneira
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email',
     'data_criacao', 'categoria', 'mostrar') # os nomes aparecerá nas tabelas

    list_display_links = ('id', 'nome', 'sobrenome') # ter os link para clicar
    #list_filter = ('nome', 'sobrenome') # filtar os elementos
    list_per_page = 10 #  sejão exibido 10 elementos por páginas...
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('mostrar', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
