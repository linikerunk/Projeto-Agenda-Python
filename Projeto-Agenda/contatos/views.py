from django.shortcuts import render, get_object_or_404, redirect # atalho para nao precisar digitar o try..
from django.http import Http404
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos # Chave é valor...
    })


def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)

        if not contato.mostrar:
            raise Http404()
        # get_object_or_404
        # contato = get_object_or_404(Contato, id=contato_id)
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
        request, messages.ERROR,
        'Campo termo não pode ficar vazio.'
        )
        return redirect('index')

    messages.add_message(
        request, messages.SUCCESS,
        'Existem campos na busca'
    )
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 1)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos # Chave é valor...
    })


    
