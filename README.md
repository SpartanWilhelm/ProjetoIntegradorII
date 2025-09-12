
# ProjetoIntegradorII

> Sistema web para gerenciamento e exibição de obras de arte, utilizando Django, SQLite, integração com API Artsy, scripts em Javascript, acessibilidade, controle de versão e testes automatizados. Futuramente, será integrado à nuvem AWS e terá análise de dados.

## Funcionalidades
- Cadastro e autenticação de usuários
- Upload e exibição de imagens de obras
- Integração com API Artsy para busca de obras
- Painel administrativo (Django Admin)
- Scripts web para interatividade
- Testes automatizados
- Acessibilidade em desenvolvimento
- Deploy em nuvem (futuro)

## Estrutura do Projeto

```
ProjetoIntegradorII/
├── manage.py
├── requirements.txt
├── apps/
│   ├── galeria/
│   └── usuarios/
├── setup/
├── static/
├── templates/
└── README.md
```

## Pré-requisitos
- Python 3.10 ou superior
- pip
- Git

## Instalação e Execução

1. Clone o repositório:
	```sh
	git clone https://github.com/SpartanWilhelm/ProjetoIntegradorII.git
	cd ProjetoIntegradorII
	```

2. Crie e ative o ambiente virtual:
	```sh
	python -m venv venv
	venv\Scripts\activate  # Windows
	# Para desativar:
	deactivate
	```

	> Se houver problemas para ativar o venv no PowerShell, execute como administrador e altere a política de execução:
	```sh
	Set-ExecutionPolicy RemoteSigned
	.\venv\Scripts\Activate.ps1
	```

3. Instale as dependências:
	```sh
	pip install -r requirements.txt
	```

4. Aplique as migrações do banco de dados:
	```sh
	python manage.py migrate
	```

5. Crie um superusuário (opcional):
	```sh
	python manage.py createsuperuser
	```

6. Execute o servidor de desenvolvimento:
	```sh
	python manage.py runserver
	```

7. Acesse o projeto no navegador:
	[http://localhost:8000](http://localhost:8000)

## Testes
Para rodar os testes automatizados:
```sh
python manage.py test
```

## API Utilizada
- [Artsy API](https://developers.artsy.net/v2/docs/search)

## Contribuição
Pull requests são bem-vindos! Para contribuir:
1. Fork este repositório
2. Crie uma branch (`git checkout -b feature/nome-feature`)
3. Commit suas alterações
4. Abra um Pull Request

## Contato
- Autor: SpartanWilhelm
- Email: [clguilherme3@gmail.com]

---
Projeto Integrador II
