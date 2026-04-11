# 📔 Diário de Bordo: Processo de Modelação do Portfólio

## 1. Modelação Inicial e Levantamento de Requisitos
O processo de modelação começou com a análise do enunciado para identificar as entidades fundamentais de um percurso académico e profissional. O objetivo foi criar uma estrutura que interligue a aprendizagem teórica (Unidades Curriculares) com a aplicação prática (Projetos e Tecnologias).

### 📸 Prova de Conceito (Rascunho no Papel)
![Listagem de Entidades e Atributos](media/makingof/image.png)

---

## 2. Definição de Entidades, Atributos e Justificações

### A. Licenciatura
* **Atributos:** Nome, Apresentação, Competências, ECTS.
* **Justificação 1:** A inclusão de 'Apresentação' permite contextualizar o curso para visitantes externos.
* **Justificação 2:** O campo 'Competências' resume o perfil de saída do aluno.

### B. Unidades Curriculares (UC)
* **Atributos:** Nome, Ano, Semestre, ECTS, Imagem, Link.
* **Justificação 1:** O 'Link' serve para referenciar o programa oficial na página da Lusófona.
* **Justificação 2:** A 'Imagem' ajuda na identificação visual rápida de cada cadeira no portfólio.

### C. Docente
* **Atributos:** Nome, Biografia.
* **Justificação 1:** Decidi criar uma entidade própria para Docentes para evitar redundância, permitindo que um docente esteja associado a várias UCs.
* **Justificação 2:** A 'Biografia' permite destacar o percurso dos orientadores e professores.

### D. Projeto
* **Atributos:** Título, Descrição, Conceitos Aplicados, Tecnologias, Imagem, Vídeo, Link Github.
* **Justificação 1:** O campo 'Conceitos Aplicados' é crucial para mostrar ao professor (e futuros empregadores) a ligação entre a teoria da UC e a prática.
* **Justificação 2:** O 'Link Github' é obrigatório para demonstrar transparência e competência técnica.

### E. Tecnologias
* **Atributos:** Nome, Logótipo, Link, Classificação.
* **Justificação 1:** A 'Classificação' (nível de preferência/domínio) permite destacar as áreas onde tenho maior especialização.
* **Justificação 2:** O 'Logótipo' confere um aspeto profissional e moderno à interface.

### F. TFCs (Trabalho de Fim de Curso)
* **Atributos:** Título, Autores, Orientador, Sumário, Tecnologias, Link, Classificação.
* **Justificação 1:** Embora semelhante a um projeto, o TFC tem atributos específicos como 'Autores' e 'Orientador' que justificam uma entidade dedicada.
* **Justificação 2:** A 'Classificação' destaca a relevância do tema no contexto atual.

### G. Competências & Formações
* **Atributos (Competências):** Nome, Descrição, Categoria (ex: Soft Skill / Hard Skill).
* **Atributos (Formações):** Instituição, Nome, Data Início, Data Fim.
* **Justificação:** A separação permite distinguir o que sei fazer (Competências) de onde aprendi (Formações/Cursos).

### H. Making Of (Entidade de Documentação)
* **Atributos:** Data, Etapa, Descrição, Imagem, Decisões, Erros.
* **Justificação:** Essencial para cumprir o requisito de documentar o processo evolutivo da aplicação.

---

## 3. Relações Identificadas

Para garantir a coerência dos dados, foram definidas as seguintes relações:

1.  **Licenciatura (1) : (N) Unidades Curriculares:** Um curso é composto por várias cadeiras.
2.  **Unidade Curricular (N) : (M) Docente:** Uma cadeira pode ter vários professores e um professor pode lecionar várias cadeiras.
3.  **Unidade Curricular (1) : (N) Projeto:** Geralmente, um projeto é desenvolvido no âmbito de uma cadeira específica.
4.  **Projeto (N) : (M) Tecnologia:** Um projeto utiliza várias tecnologias e uma tecnologia é usada em vários projetos.
5.  **TFC (N) : (M) Tecnologia:** Semelhante aos projetos, para identificar o stack tecnológico do trabalho final.

---

## 4. Evolução e Decisões Críticas
* **Mudança de Rota:** Inicialmente pensei em colocar as competências dentro da Licenciatura, mas percebi que ganhei competências fora da faculdade (em Formações externas), por isso criei uma entidade independente.
* **Uso de IA:** O Gemini foi utilizado para estruturar este documento Markdown.

---