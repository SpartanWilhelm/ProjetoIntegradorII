# ProjetoIntegradorII
Tema: Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente, incluir análise de dados.

Framework -> Django (Python)
Banco de dados -> SQLite
Script Web -> Javascript
Nuvem -> AWS (Futuro)
API -> Artsy (https://developers.artsy.net/v2/docs/search)
Controle de versão -> Git e GitHub
Testes -> Em andamento
Acessibilidade -> Em andamento


Dicas para execução e teste.
* Necessário ter instalado Python 3.10 ou superior *

1- Navegue até o diretório do projeto:
-> cd caminho/para/seu/projeto

2 - Crie e ative um ambiente virtual:
python -m venv venv //Já criado com o nome de venv
-> venv\Scripts\activate  # Para ativar no Windows
-> deactivate # Para desativar o venv


#Em caso de problemas para rodar o venv 
Abra o PowerShell como Administrador:
Clique com o botão direito no ícone do PowerShell e selecione “Executar como administrador”.
Verifique a política de execução atual:
-> Get-ExecutionPolicy

Altere a política de execução para permitir scripts:
Para permitir a execução de scripts locais não assinados, use o comando:
-> Set-ExecutionPolicy RemoteSigned

Se você quiser permitir todos os scripts, use:
-> Set-ExecutionPolicy Unrestricted

Confirme a alteração:
Você pode ser solicitado a confirmar a alteração. Digite Y ou S e pressione Enter.
Ative o ambiente virtual no terminal novamente:
-> .\venv\Scripts\Activate.ps1

3 - Instale as dependências do projeto:
-> pip install -r requirements.txt

4 - Aplique as migrações do banco de dados:
-> python manage.py migrate

5 - Crie um superusuário (opcional, mas recomendado para acessar o admin do Django):
-> python manage.py createsuperuser

6 - Execute o servidor de desenvolvimento:
-> python manage.py runserver

7 - Acesse o projeto no navegador: Abra o navegador e vá para http://localhost:8000.
