from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from .models import Dados, Cultivo
from .form import DadosForm 
from django.contrib.auth import authenticate, login


# Classe genérica do django para view de delete
class DadosDeleteView(DeleteView):
    model = Dados
    template_name = 'cadastro/confirmar_exclusao.html'
    success_url = reverse_lazy('dados_fazenda')


# Classe genérica do django para view de update
class DadosUpdateView(UpdateView):
    model = Dados
    form_class = DadosForm
    template_name = 'cadastro/editar_dados.html'
    success_url = reverse_lazy('dados_fazenda')



# View cadastro
def cadastro_cultivo(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        # Cria o formulário com o ModelForm
        form = DadosForm(request.POST)
        # Formulário válido
        if form.is_valid():
            form.save()
            return redirect('dados_fazenda')
        # Formulário não é válido
        else:
            print(form.errors)  # Verifica quais erros estão presentes
            # Renderiza a página do formulário com os erros
            return render(request, 'cadastro/cadastro.html', {'form': form})
    # Se a requisição da página for GET
    else:
        form = DadosForm()
    return render(request, 'cadastro/cadastro.html', {'form': form})


# View listagem
def listagem(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        form = DadosForm(request.POST)
        # Formulário válido:
        if form.is_valid():
            form.save()  # Salva os dados após validação
            return redirect('dados_fazenda')
        # Formulário não é válido:
        else:
            print(form.errors)  # Verificar quais erros estão presentes

            # Recarrega a página com os erros de validação, se houver
            return render(request, 'cadastro/cadastro.html', {'form': form})
    # Se a requisição da página for GET
    else:
        form = DadosForm()
    
    # Coloca os dados recebidos em um dicionário
    dados = {
        'dados': Dados.objects.all(),
        'form': form
    }

    # Retorna a página listagem, com os dados inseridos com sucesso no banco
    return render(request, 'cadastro/listagem.html', dados)


# View para a tela de seleção do cultivo para detalhes
def selecionar(request):
    return render(request, 'detalhes_registro/selecionar.html')


# View para tela de detalhes do cultivo
def detalhe(request):
    if request.method == 'POST':
        cultivo = request.POST.get('cultivo')
    
        # Procura o ultimo registro conforme o cultivo que o usuario passou
        try:
            ultimo_registro = Dados.objects.filter(cultivo=cultivo).latest('data')
        except Dados.DoesNotExist:
            ultimo_registro = None

        # Coloca os dados do context em um dict para renderizar as paginas com
        # as informações do dict
        dados = {
        'cultivos': Cultivo.objects.filter(nome = cultivo),
        'ultimo_registro': ultimo_registro
    }
        # Caso houver ultimo registro
        return render(request, 'detalhes_registro/detalhe.html', dados)

    # Caso não houver
    else:
        return render(request, 'detalhes_registro/detalhe.html')

# View para realizar o login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial', usuario_id=user.id)  # Passa o ID do usuário para a próxima página

        return render(request, 'login/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'login/login.html')

# View para cadastro de usuário
def cadastro_usuario(request):
    return render(request, 'login/cadastro.html')

# View Home
def home(request):
    return render(request, 'inicio/home.html')