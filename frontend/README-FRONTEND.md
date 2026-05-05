# Documentação de Frontend e Design System - ContraDito
## Arquitetura Base
[cite_start]O frontend foi construído utilizando Next.js com React e estilizado via Tailwind CSS[cite: 1057]. [cite_start]A estrutura de pastas segue o padrão App Router[cite: 1058]:

* **Tela Inicial:** O arquivo `app/page.tsx` abriga a capa principal, a barra de busca, os filtros e o ranking. [cite_start]Ele consome a rota `GET /api/politicos`[cite: 1059].
* [cite_start]**Dossiê do Político (Rota Dinâmica):** O arquivo `app/politico/[id]/page.tsx` abriga a tela detalhada e as contradições do parlamentar escolhido, consumindo a rota `GET /api/politicos/{id_parlamentar}`[cite: 1060].

##  Guia de Estilos (Tailwind CSS)
Para manter a identidade visual do projeto padronizada para toda a equipe, utilizamos as seguintes regras baseadas nas classes do Tailwind CSS:

* [cite_start]**Cores Principais:** O fundo padrão do sistema é predominantemente escuro (`bg-slate-900`) para transmitir seriedade jornalística e um tom investigativo[cite: 1061].
* [cite_start]**Tipografia:** Utilizamos fontes clean e modernas, representadas pelo padrão `font-sans`[cite: 1062].
* **Score de Coerência (Cores Semânticas):** Utilizamos cores com significado direto. [cite_start]Notas altas recebem obrigatoriamente a cor verde (`text-green-600`), enquanto notas baixas recebem a cor vermelha (`text-red-600`)[cite: 1064].
* [cite_start]**Componentes Visuais:** Os cards de informação e as tabelas utilizam bordas suaves (`border-slate-300`) e fundos brancos (`bg-white`) para garantir o contraste ideal na leitura dos dados[cite: 1065].