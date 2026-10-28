# 🎬 Cinema em Pauta

O **Cinema em Pauta** é uma plataforma voltada para o universo cinematográfico, reunindo críticas, análises, notícias e conteúdos sobre filmes. O projeto tem como objetivo oferecer um espaço para quem gosta de cinema descobrir novas produções, acompanhar lançamentos e explorar diferentes perspectivas sobre obras cinematográficas.

A aplicação está sendo desenvolvida com Python e Flask, com foco na organização do código, boas práticas de desenvolvimento back-end e construção de uma aplicação web completa.

## 🚀 Funcionalidades

* **Catálogo de filmes:** exibição de informações, sinopses, gêneros e datas de lançamento.
* **Críticas cinematográficas:** avaliações e opiniões sobre filmes.
* **Análises:** conteúdos sobre histórias, personagens, direção e outros aspectos das produções.
* **Notícias:** novidades da indústria cinematográfica e informações sobre lançamentos.
* **Busca de filmes:** pesquisa de títulos disponíveis na plataforma.
* **Categorias:** organização dos conteúdos por gênero e assunto.
* **Artigos:** publicação de conteúdos relacionados ao universo do cinema.

## 🛠️ Tecnologias

* **Python:** linguagem principal do projeto.
* **Flask:** framework web para desenvolvimento da aplicação.
* **HTML5:** estrutura das páginas.
* **CSS3:** estilização e responsividade.
* **JavaScript:** interatividade da interface.
* **PostgreSQL:** banco de dados planejado para armazenar os dados da aplicação.
* **Git e GitHub:** versionamento e gerenciamento do código.

## 🏗️ Estrutura do projeto

A estrutura será organizada para separar as responsabilidades da aplicação e facilitar sua manutenção.

```text
cinema-em-pauta/
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── templates/
│   └── static/
├── tests/
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── run.py
```

## ⚙️ Instalação

### Pré-requisitos

* Python 3.10 ou superior.
* Git.
* Ambiente virtual Python.

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd cinema-em-pauta
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

No Linux:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python run.py
```

A aplicação estará disponível no endereço configurado pelo Flask, normalmente:

```text
http://127.0.0.1:5000
```

## 🎯 Objetivos do projeto

O Cinema em Pauta também funciona como projeto de estudo e portfólio, permitindo aplicar conhecimentos de desenvolvimento web e back-end, incluindo:

* Desenvolvimento de aplicações com Flask.
* Criação e organização de rotas.
* Integração com banco de dados relacional.
* Implementação de operações CRUD.
* Validação e tratamento de erros.
* Organização de código em módulos.
* Escrita de testes automatizados.
* Boas práticas de versionamento com Git.

## 📌 Status

**Em desenvolvimento.**

As funcionalidades serão implementadas gradualmente, conforme a evolução da arquitetura e das necessidades da aplicação.

## 👨‍💻 Autor

Desenvolvido por **Vitor Abreu**.

* [GitHub](https://github.com/abreu-developer)
* [LinkedIn](https://www.linkedin.com/in/vitorabreudev)
* [Portfólio](https://vitorabreuportifolio.lovable.app)

---

*Cinema em Pauta — seu espaço para descobrir, analisar e discutir cinema.*
