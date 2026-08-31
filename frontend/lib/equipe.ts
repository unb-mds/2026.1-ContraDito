// Conteúdo institucional da Home (Sobre + Equipe + números reais do projeto).

export const STORY: string[] = [
  "Transparência de verdade não é apenas disponibilizar dados na internet; é tornar a informação compreensível e acessível a qualquer cidadão. O ContraDito surge como uma ferramenta de controle social criada por estudantes de Engenharia de Software da Universidade de Brasília (UnB/FCTE) na disciplina de Métodos de Desenvolvimento de Software (MDS).",
  "Cruzamos milhares de registros oficiais extraídos diretamente da Câmara dos Deputados e do Senado Federal. Conectamos o que os parlamentares dizem no plenário com a forma como efetivamente votam em projetos de lei, tudo em uma interface limpa e sem ruídos.",
  "Apostamos na neutralidade absoluta: a plataforma não emite pareceres, não distribui notas nem rotula políticos. Entregamos a informação bruta organizada para que o eleitor exerça seu papel crítico com autonomia.",
];

export type Membro = {
  nome: string;
  papel: string;
  handle: string;
  tags: string[];
  linkedin?: string;
  email?: string;
};

export const EQUIPE: Membro[] = [
  { nome: "Henrique Mendes Elias", papel: "Scrum Master · Lead Data Engineer", handle: "henriquemendeselias", tags: ["Engenharia de Dados (ETL)", "Pipelines & Ingestão", "Arquitetura & API", "DevOps"], linkedin: "https://www.linkedin.com/in/henriquemendeselias/" },
  { nome: "Luiz Henrique Tomaz", papel: "Lead AI Engineer · Fullstack", handle: "luizhtmoreira", tags: ["Líder de IA & NLP", "Banco Vetorial (Vector DB)", "Arquitetura de Dados", "Frontend"], linkedin: "https://www.linkedin.com/in/luiz-henrique-tomaz-moreira" },
  { nome: "Matheus Rodrigues Pontes", papel: "Lead Documentação · DevOps & Testes", handle: "matheus0346", tags: ["Líder de Documentação (MkDocs)", "Docker / DevOps", "Testes Automatizados & QA", "CI/CD"], linkedin: "https://www.linkedin.com/in/matheus-pontes-566840404/" },
  { nome: "João Guilherme Amâncio", papel: "Product Owner · Fullstack", handle: "jot4-ge", tags: ["Product Owner", "Fullstack", "API", "Extração", "Frontend"], linkedin: "https://www.linkedin.com/in/joaoguiam/" },
  { nome: "Gabriel Portácio", papel: "Frontend · UI/UX", handle: "G2SBiell", tags: ["Frontend", "Interface & UI/UX", "Design System", "Documentação (MkDocs)"] },
  { nome: "Lucas Araújo Lima", papel: "Lead DevOps · Testes & Documentação", handle: "lucasaraujoszz", tags: ["Docker & Conteinerização", "DevOps", "Testes Automatizados & QA", "Documentação (MkDocs)"] },
];

// Números reais do projeto (Supabase, 2026-06-25).
export const PROJECT_STATS = [
  { value: "887", label: "parlamentares", sub: "642 Câmara · 245 Senado" },
  { value: "53.329", label: "discursos extraídos", sub: "49.731 Câmara · 3.598 Senado" },
  { value: "2.573", label: "proposições cruzadas", sub: "1.372 Câmara · 1.201 Senado" },
  { value: "51.611", label: "votos nominais", sub: "47.966 Câmara · 3.645 Senado" },
] as const;
