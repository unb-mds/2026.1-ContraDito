import asyncio
from sentence_transformers import SentenceTransformer

class MotorNLP:
    def __init__(self, modelo_nome: str = 'paraphrase-multilingual-mpnet-base-v2'):
        self.modelo = SentenceTransformer(modelo_nome)
        
    async def gerar_embedding(self, texto_limpo: str) -> list[float]:
        """
        Recebe um texto limpo e gera um vetor denso de 768 dimensões.
        Usa to_thread para não bloquear o event loop do ETL.
        """
        if not texto_limpo:
            return []
        
        vetor = await asyncio.to_thread(self.modelo.encode, texto_limpo)
        return vetor.tolist()