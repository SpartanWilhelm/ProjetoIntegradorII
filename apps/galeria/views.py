from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms
import requests
from django.http import JsonResponse


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado!")
        return redirect ('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})

# Usar o token de acesso para fazer uma solicitação
def search_artists(token, query):
    url = f'https://api.artsy.net/api/search?q={query}&type=artist'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers)
    return response.json()

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    artists = []
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            # Filtra as fotografias pelo nome
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
            # Busca artistas na API do Artsy
            token = get_access_token()
            artists_data = search_artists(token, nome_a_buscar)
            for artist in artists_data.get('_embedded', {}).get('results', []):
                artists.append({
                    'title': artist.get('title'),
                    'permalink': artist.get('_links', {}).get('permalink', {}).get('href'),
                    'thumbnail': artist.get('_links', {}).get('thumbnail', {}).get('href')
                })
    
    return render(request, "galeria/index.html", {"cards": fotografias, "artists": artists})

def nova_obra(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado!")
        return redirect ('login')
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova obra cadastrada')
            return redirect ('index')
    return render(request, 'galeria/nova_obra.html', {'form':form})

def editar_obra(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obra editada com sucesso.')
            return redirect ('index')

    return render(request, 'galeria/editar_obra.html', {'form':form, 'foto_id':foto_id})

def deletar_obra(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Obra apagada com sucesso.')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria = categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})

# Suas credenciais
client_id = '26cb47642d27045c9f4c'
client_secret = 'bf7c7faa1426d74dbbf5b134bebea3ff'

# Obter o token de acesso
def get_access_token():
    url = 'https://api.artsy.net/api/tokens/xapp_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=data)
    token = response.json()['token']
    return token

# Usar o token de acesso para fazer uma solicitação
def get_artwork(token, artwork_id):
    url = f'https://api.artsy.net/api/artworks/{artwork_id}'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers)
    print(headers)  # Verifique os cabeçalhos
    print(response.json())  # Verifique a resposta
    return response.json()


# Visão para exibir a obra de arte
def artwork_view(request, artwork_id):
    token = get_access_token()
    artwork = get_artwork(token, artwork_id)
    return JsonResponse(artwork)

# Usar o token de acesso para fazer uma solicitação
def search_artists(token, query):
    url = f'https://api.artsy.net/api/search?q={query}&type=artist'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Visão para buscar artistas e renderizar o template
def artist_search_view(request):
    query = request.GET.get('query', '')
    token = get_access_token()
    artists_data = search_artists(token, query)
    artists = []
    for artist in artists_data.get('_embedded', {}).get('results', []):
        artists.append({
            'title': artist.get('title'),
            'permalink': artist.get('_links', {}).get('permalink', {}).get('href'),
            'thumbnail': artist.get('_links', {}).get('thumbnail', {}).get('href')
        })
    return render(request, 'galeria/artist.html', {'artists': artists})
