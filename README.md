# 📝 Mini Blog Modular com Flask

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

> Projeto prático criado como parte de uma série de conteúdos publicados no [meu LinkedIn](https://www.linkedin.com/in/seu-usuario) para ensinar Flask de forma acessível e profissional.

---

## 🧠 Sobre o Projeto

Este é um *mini blog modular* criado com Flask, seguindo uma arquitetura limpa e profissional. Ele inclui:

- ✅ App Factory (`create_app()`)
- ✅ Blueprints para modularização
- ✅ Templates com herança usando Bootstrap 5
- ✅ Estrutura escalável para futuras funcionalidades (CRUD, banco de dados, autenticação)

O objetivo é ensinar boas práticas no uso do Flask de forma simples e acessível, especialmente para quem está começando, mas já busca desenvolver com qualidade profissional.

---

## 📚 O que você vai encontrar aqui

| Módulo     | Descrição                                                     |
|------------|---------------------------------------------------------------|
| `main`     | Páginas públicas como *Home* e *Sobre*                        |
| `auth`     | Rotas de autenticação: *Login* e *Registro* (em desenvolvimento) |
| `templates`| HTML com herança e componentes reutilizáveis                  |
| `static`   | Estrutura para arquivos CSS, JS e imagens                     |

---

## 🚀 Como rodar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/mini-blog-flask.git
cd mini-blog-flask
```

---
## Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
---
## Instale as dependências:

```bash
pip install -r requirements.txt
```
---

## Rode o servidor Flask:
```bash
python run.py
```
#### Acesse no navegador: http://localhost:5000
---
🛠️ Tecnologias usadas

- Python 3.10+
- Flask
- Bootstrap 5
- Estrutura modular com Blueprints + App Factory
---

🧠 Autor
Desenvolvido por Lucas Uanderson
💻 Dev backend em formação | 🧠 Foco em código limpo, arquitetura e ensino acessível

---

## 📎 Artigo relacionado

Este projeto está relacionado a um artigo publicado no meu LinkedIn que aborda, principalmente, a arquitetura App Factory no Flask um conceito fundamental para criar aplicações escaláveis e organizadas.
Importante: O artigo não é um tutorial específico deste mini blog, mas o código aqui presente serve como apoio para exemplificar a aplicação prática do App Factory, Blueprints e modularização.
Leia o artigo completo [Texto do link](URL) para entender os conceitos e boas práticas que você pode aplicar em seus próprios projetos Flask.


