from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from app.rotas import politicos, logs


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando o Cache em Memória...")
    FastAPICache.init(InMemoryBackend())
    yield
    print("Desligando a API...")


tags_metadata = [
    {
        "name": "Políticos",
        "description": "Operações de listagem, paginação, perfil detalhado e busca semântica vetorial.",
    },
    {
        "name": "Monitoramento",
        "description": "Rotas internas de observabilidade e registro de falhas do Motor NLP.",
    },
]

app = FastAPI(
    title="API ContraDito - Raio-X do Parlamentar",
    description="""
    Back-end oficial da Squad 9 para análise de discursos parlamentares.
    Esta API gerencia a listagem de políticos, o cálculo de coerência e o pipeline de checagem de fatos via RAG.
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

app.include_router(politicos.router)
app.include_router(logs.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def home():
    return {"status": "Servidor rodando liso na arquitetura limpa!"}
