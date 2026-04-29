import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from supabase import create_client, Client

# Carrega as variáveis do .env
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def executar_poc():
    print(
        "Carregando o modelo MPNet (isso pode levar alguns segundos na primeira vez)..."
    )
    modelo = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")

    mocks = [
        "O deputado votou a favor do aumento de impostos na comissão.",
        "O parlamentar apoiou a elevação da carga tributária.",
        "A nova lei propõe a redução drástica de impostos para empresas.",
        "O projeto de infraestrutura na rodovia foi aprovado ontem.",
        "A construção de novas estradas recebeu sinal verde do congresso.",
    ]

    print("Vetorizando os mocks...")
    embeddings = modelo.encode(mocks).tolist()

    print("Injetando dados na tabela 'provas_contradicao'...")
    dados_para_inserir = [
        {
            "tipo_documento": "DISCURSO",
            "data_evento": "2026-04-25",
            "link_fonte": "https://dadosabertos.camara.leg.br/mock",
            "texto_extraido": texto,
            "embedding": vetor,
            "politico_id": 204379,
        }
        for texto, vetor in zip(mocks, embeddings)
    ]

    resposta_insert = (
        supabase.table("provas_contradicao").insert(dados_para_inserir).execute()
    )
    print(f"Inseridos {len(resposta_insert.data)} registros com sucesso.")

    print("\n--- Testando a Similaridade via RPC Homologada ---")
    frase_busca = "O político foi favorável a cobrar mais tributos."
    vetor_busca = modelo.encode(frase_busca).tolist()

    resposta_busca = supabase.rpc(
        "buscar_discursos_similares",
        {
            "query_embedding": vetor_busca,
            "match_threshold": 0.5,
            "match_count": 2,
            "p_politico_id": 204379,
        },
    ).execute()

    print(f"Buscando por: '{frase_busca}'")
    for resultado in resposta_busca.data:
        texto_retorno = resultado.get(
            "texto_extraido", resultado.get("texto", "Texto não encontrado")
        )
        similaridade = resultado.get("similaridade", "N/A")
        print(f" -> Encontrado: '{texto_retorno}' (Similaridade: {similaridade})")


if __name__ == "__main__":
    executar_poc()
