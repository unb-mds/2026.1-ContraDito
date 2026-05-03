from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class PoliticoBase(BaseModel):
    nome_civil: str = Field(
        ...,
        description="Nome oficial do parlamentar",
        examples=["João Batista da Silva"],
    )
    nome_urna: str = Field(
        ...,
        description="Nome utilizado na urna (usado na busca global)",
        examples=["João da Silva"],
    )
    cargo: str = Field(..., examples=["Deputado Federal"])
    partido: str = Field(..., examples=["PL"])
    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description="Sigla do Estado (ex: DF, SP)",
        examples=["SP"],
    )
    foto_url: Optional[str] = Field(None, examples=["https://camara.leg.br/foto.jpg"])
    situacao: Optional[str] = Field(None, examples=["Em Exercício"])


class PoliticoResponse(PoliticoBase):
    id: int = Field(..., examples=[74646])
    score_coerencia: Optional[float] = Field(
        None,
        description="Média de coerência de 0 a 100. Retorna Nulo se não houver dados suficientes.",
        examples=[85.5],
    )


class ContextoOriginal(BaseModel):
    tipo_documento: str = Field(..., examples=["Discurso"])
    data_evento: date = Field(..., examples=["2023-10-15"])
    texto_extraido: str = Field(
        ...,
        examples=[
            "Eu sou totalmente a favor de reduzir os impostos da cesta básica..."
        ],
    )
    link_fonte: Optional[str] = Field(
        None,
        description="Link do YouTube da TV Câmara ou PDF",
        examples=["https://youtu.be/xyz"],
    )


class ResultadoIA(BaseModel):
    topico_identificado: str = Field(..., examples=["Economia"])
    postura_extraida_do_texto: str = Field(..., examples=["A Favor"])
    voto_oficial_registrado: str = Field(..., examples=["Não"])
    status_coerencia: bool = Field(..., examples=[False])
    justificativa: Optional[str] = Field(
        None,
        examples=[
            "O parlamentar discursou a favor da isenção, mas votou contra o projeto no painel."
        ],
    )


class ProvaContradicao(BaseModel):
    id: int = Field(..., examples=[1024])
    contexto: ContextoOriginal
    resultado: ResultadoIA


class PerfilPoliticoDetalhado(BaseModel):
    politico: PoliticoResponse
    provas: List[ProvaContradicao]


class PaginaPoliticos(BaseModel):
    total_registros: int = Field(..., examples=[513])
    pagina_atual: int = Field(..., examples=[1])
    tamanho_pagina: int = Field(..., examples=[20])
    total_paginas: int = Field(..., examples=[26])
    itens: List[PoliticoResponse]


class BuscaVetorialRequest(BaseModel):
    texto_busca: str = Field(
        ...,
        description="O texto da lei ou tema para buscar similaridade",
        examples=["Aumento da carga tributária e taxação de grandes fortunas"],
    )
    id_parlamentar: Optional[int] = Field(
        None,
        description="Filtro opcional para buscar discursos de um político específico",
        examples=[74646],
    )
    limite: int = Field(
        5, ge=1, le=20, description="Quantidade de resultados a retornar", examples=[5]
    )


class ResultadoSimilaridade(BaseModel):
    id: int = Field(..., examples=[504])
    texto_extraido: str = Field(
        ..., examples=["Precisamos taxar as grandes fortunas imediatamente."]
    )
    similaridade: float = Field(
        ..., description="Score matemático de 0 a 1 (0 = idêntico)", examples=[0.12]
    )
