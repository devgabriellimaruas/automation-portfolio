# Portfolio Dev Gabriel Lima Ruas

Este projeto é uma aplicação web simples construída usando Flask. Serve como uma ferramenta de automação de portfólio, permitindo que usuários acessem meus trabalhos e projetos.

## Sobre Mim

Sou Gabriel Lima Ruas, desenvolvedor focado em criar soluções de automação práticas e eficientes. Transformo processos manuais em aplicações funcionais, utilizando tecnologias modernas e boas práticas de desenvolvimento.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
app
├── static
│   └── docs
│       └── README.md
│   └── images
│       └── README.md
│   └── uploads
│       └── README.md
│   └── style.css
├── templates
│   └── components
│       └── base.html
│   └── about.html
│   └── add_project.html
│   └── contact.html
│   └── habilities.html
│   └── home.html
│   └── projects.html
├── app.py
├── config.py
├── database.py
├── migrations
│   └── versions
│   └── alembic.ini
│   └── env.py
│   └── README.md
│   └── script.py.mako
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Instruções de Configuração

<blockquote>
<small>⚠️ <strong>Observação:</strong> Este projeto está testado e rodando com <strong>Python 3.13.7</strong>. Use esta versão para evitar problemas de compatibilidade.</small>
</blockquote>

1. **Clone o repositório**:
   ```
   git clone https://github.com/devgabriellimaruas/portfolio_automation.git
   cd portfolio_automation
   ```
2. **Crie um ambiente virtual** (opcional, mas recomendado):

```
    python -m venv .venv
```

3. **Ative o ambiente virtual**: - On Windows:

```
    .venv\Scripts\activate
```

- On macOS/Linux:

```
    source .venv/bin/activate
```

4. **Instale os pacotes necessários**:

```
    pip install -r requirements.txt
```

## Executando a Aplicação

Para executar a aplicação, utilize o seguinte comando:

```
    python run.py
```

A aplicação será iniciada em http://localhost:5000/. Abra esta URL em seu navegador para visualizar o portfólio.

## Funcionalidades

- 🏠 **Página Inicial**: Visão geral do portfólio, com destaque para meus projetos e habilidades.
- 🙋‍♂️ **Sobre Mim**: Informações sobre minha experiência, trajetória e especialidades.
- 💻 **Habilidades**: Lista detalhada das minhas competências técnicas e ferramentas que utilizo.
- 🚀 **Projetos**: Galeria de projetos com descrições, tecnologias usadas e links para mais detalhes.
- ➕ **Adicionar Projeto**: Formulário intuitivo para adicionar novos projetos ao portfólio de forma prática.
- ✉️ **Contato**: Formulário para enviar mensagens diretamente para mim de maneira rápida e segura.

## Tecnologias Utilizadas

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000000?style=for-the-badge&logo=sqlalchemy&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## Contato

Entre em contato para quaisquer dúvidas, informações ou mensagens:

- [![Email](https://img.shields.io/badge/Email-limaruasgabriel@gmail.com-c14438?style=for-the-badge&logo=gmail&logoColor=white)](mailto:limaruasgabriel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Gabriel_Lima_Ruas-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabriellimaruas/)

## Contribuição

**Design:** Studio **DesignbyGeo**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Geovanna_Holanda-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/geovanna-holanda/)
