# ContraDito
 
![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)
![Universidade de Brasília](https://img.shields.io/badge/MDS-UnB%20FGA-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
 
> **O que foi dito *vs.* O que foi votado.** Uma plataforma de transparência política movida a Inteligência Artificial.
 
---
 
## Sobre o Projeto
 
O **ContraDito** é um projeto universitário desenvolvido pela **Squad 09** para a disciplina de Métodos de Desenvolvimento de Software da Universidade de Brasília (UnB - FCTE).
 
O sistema atua como um portal de transparência avançado que cruza discursos proferidos por parlamentares (extraídos via API de Dados Abertos do governo) com seus respectivos votos no plenário. Utilizando uma arquitetura de IA baseada em RAG (*Retrieval-Augmented Generation*), o sistema encontra similaridades semânticas entre os discursos e as leis votadas, gerando um **Score de Coerência** matemático e auditável para que o cidadão acompanhe a postura real de seus representantes.
 
---
 
## Principais Funcionalidades
 
- **Busca Semântica com IA:** Vá além da busca por nomes. Pesquise por pautas abstratas (ex: "taxação de fortunas") e deixe o motor vetorial encontrar discursos alinhados ao tema por significado e contexto.
- **Raio-X do Parlamentar:** Perfil detalhado com o *Score de Coerência* sempre atualizado. O sistema lida ativamente com a ausência de histórico parlamentar, exibindo um estado neutro de "Sem Dados" para evitar falsas acusações de incoerência.
- **Ringue de Comparação:** Selecione 2 políticos para uma visualização "Lado a Lado", contrastando diretamente suas notas gerais e o histórico de votos nas exatas mesmas proposições (PLs/PECs).
- **Provas da Contradição:** Painel comparativo que vincula literalmente o discurso (o que foi dito) à votação oficial (o que foi feito).
- **Transparência e Rastreabilidade:** Todas as evidências geradas possuem links diretos e rotinas de *fallback* para as fontes oficiais originais (Vídeo na TV Câmara ou PDF do Diário Oficial).
---
 
## Arquitetura de Software
 
O ContraDito foi projetado com uma arquitetura de microsserviços focada em performance, isolamento de recursos e tolerância a falhas. O ecossistema opera através de grandes pilares integrados:
 
1. **Pipeline de Extração (ETL):** Rotinas automatizadas consomem as APIs governamentais, aplicam filtros rigorosos de sanitização de texto (limpeza HTML e ruídos taquigráficos) e estruturam proposições e votos.
2. **Motor Vetorial (Retrieval):** O Worker NLP isolado processa os discursos em coordenadas matemáticas (*Embeddings*). O banco de dados atua como um filtro ativo, cruzando semanticamente o escopo das leis com os discursos em milissegundos.
3. **Inferência Lógica (Augmented Generation):** O modelo de linguagem local recebe apenas as evidências validadas pelo banco vetorial e extrai o veredito final (Postura e Justificativa), eliminando os riscos de "alucinação" da IA.
4. **API Principal (Roteamento):** Uma camada leve e blindada em FastAPI serve os dados validados ao front-end, munida de paginação rápida, proteção contra abusos estruturais (*Rate Limiting*) e invalidação de cache em tempo real.
5. **Interface de Usuário:** Aplicação web responsiva e *Mobile First*, encarregada de exibir dados complexos através de velocímetros, painéis comparativos e alertas visuais de coerência.
---
 
## Tecnologias Utilizadas
 
- **Back-end:** Python, FastAPI, Pydantic, FastAPI-Cache
- **Banco de Dados Vetorial:** Supabase (PostgreSQL) com extensão `pgvector` e indexação de alta performance (HNSW)
- **Inteligência Artificial:** Worker de NLP (PyTorch/SBERT) e LLM Local (Ollama)
- **Infraestrutura:** Docker, Docker Compose, Arquitetura de Microsserviços
- **Qualidade e Documentação:** GitHub Actions (CI/CD), formatador padrão de código (Black) e Swagger/OpenAPI
---
 
## Como Rodar o Projeto Localmente
 
### Pré-requisitos
 
- [Docker](https://www.docker.com/) e Docker Compose instalados
- Git
### Passos de Instalação
 
**1. Clone o repositório:**
 
```bash
git clone https://github.com/sua-organizacao/entrelinhas-contradito.git
cd entrelinhas-contradito
```
 
**2. Configure as variáveis de ambiente:**
 
Crie um arquivo `.env` na raiz do projeto e insira suas credenciais:
 
```env
SUPABASE_URL=sua_url_do_projeto_aqui
SUPABASE_KEY=sua_chave_anon_publica_aqui
```
 
**3. Suba os contêineres da aplicação:**
 
```bash
docker-compose up --build
```
 
**4. Acesse e teste:**
 
- Front-end: [http://localhost:3000](http://localhost:3000)
- Back-end/Docs (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
---
 
## Squad 09
 
Este projeto foi construído colaborativamente por:
 
| Membro | GitHub |
|--------|--------|
| Henrique | [@henriquemendeselias](https://github.com/henriquemendeselias) |
| João Guilherme | [@jot4-ge](https://github.com/jot4-ge) |
| Luiz Henrique | [@luizhtmoreira](https://github.com/luizhtmoreira) |
| Gabriel | [@G2SBiell](https://github.com/G2SBiell) |
| Lucas | [@lucasaraujoszz](https://github.com/lucasaraujoszz) |
| Matheus | [@matheus0346](https://github.com/matheus0346) |
