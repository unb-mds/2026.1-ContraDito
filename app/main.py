from fastapi import FastAPI

app = FastAPI(
    title="API Coerência Política",
    description="Back-end oficial da Squad 9 para análise de discursos parlamentares",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"status": "Servidor rodando liso na arquitetura limpa!"}

@app.get("/api/politicos/{id_parlamentar}")
def buscar_politico(id_parlamentar: int):
    return {
      "politico": {
        "id": id_parlamentar,
        "nome": "João da Silva",
        "cargo": "Deputado Federal",
        "partido": "XYZ",
        "estado": "DF"
      },
      "contexto_original": {
        "tipo_documento": "discurso",
        "data_evento": "2026-04-02",
        "texto_extraido": "Sr. Presidente, venho a esta tribuna defender a urgência da votação da PEC..."
      },
      "resultado_ia": {
        "topico_identificado": "Reforma Tributária",
        "postura_extraida_do_texto": "A Favor",
        "voto_oficial_registrado": "Contra",
        "status_coerencia": False,
        "score_coerencia": 12.5
      }
    }