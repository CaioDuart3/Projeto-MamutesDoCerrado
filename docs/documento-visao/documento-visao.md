
# 1. Visão Geral do Produto e Projeto

<div style="text-align: justify;">

Este documento será usado como guia para registrar as informações gerais do produto e projeto. Ele será refinado e atualizado ao longo do ciclo de vida do desenvolvimento, conforme o padrão ABNT para documentos técnicos.

</div>

---

## 1.1 Problema

### 1.1.1 Contexto do Problema

<div style="text-align: justify;">

A equipe de competição <strong>Mamutes do Cerrado</strong>, da Universidade de Brasília (UnB) - FCTE, enfrenta desafios significativos em dois pilares centrais: <strong>divulgação externa</strong> e <strong>gestão interna</strong>. Como uma equipe acadêmica e técnica que busca representar a instituição em competições de alto nível, é crucial manter uma forte presença pública para atrair novos membros, patrocinadores e reconhecimento institucional. Simultaneamente, a organização interna é essencial para otimizar processos, garantir transparência e alcançar um desempenho competitivo.

Atualmente, a equipe carece de ferramentas integradas que unifiquem a gestão de seus recursos (como estoque e finanças), tarefas (calendários e reuniões) e documentos essenciais.

</div>

---

### 1.1.2 Problema Encontrado

<div style="text-align: justify;">

O principal problema enfrentado pela equipe <strong>mamutes</strong> é a falta de uma <strong>plataforma centralizada</strong> que conecte as necessidades de <strong>divulgação externa</strong> e <strong>gestão interna</strong>. Isso resulta em:

</div>

| Problema Encontrado          | Descrição                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------|
| **Baixa visibilidade externa** | Falta de uma identidade visual unificada e dificuldade em atrair novos membros e patrocinadores. |
| **Desorganização interna**    | Ausência de ferramentas adequadas para gerenciar tarefas, compromissos, recursos materiais e financeiros, gerando atrasos, retrabalho e perda de eficiência. |
| **Risco de perda de informações** | Armazenamento descentralizado de documentos e atas compromete a transparência e dificulta o acesso às informações essenciais. |
| **Solução Proposta**          | Desenvolvimento de um software para otimizar processos internos e fortalecer a presença externa da equipe. |

---

### 1.1.3 Diagrama de Ishikawa (Espinha de Peixe)

<div style="text-align: justify;"> 

A equipe de competição <strong>Mamutes do Cerrado</strong>, da Universidade de Brasília (UnB) - FCTE, enfrenta desafios em dois pilares fundamentais: <strong>divulgação externa</strong> e <strong>gestão interna</strong>. Como um grupo acadêmico e técnico que representa a instituição em competições de alto nível, é essencial conciliar uma forte presença pública com uma organização interna eficiente para alcançar seus objetivos estratégicos. <br> <br>

Atualmente, a equipe carece de ferramentas integradas que unifiquem a gestão de recursos (estoque e finanças), tarefas (calendários e reuniões) e documentos essenciais. Isso gera uma série de dificuldades, conforme detalhado na tabela abaixo: <br> <br>

</div>

| **Aspecto**               | **Problemas Identificados**                                                                                      | **Impactos**                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Visibilidade Externa**   | Falta de identidade visual unificada e dificuldade em atrair novos membros e patrocinadores.                    | Baixa captação de talentos e financiamentos, além de menor reconhecimento institucional.    |
| **Gestão Interna**         | Ausência de ferramentas adequadas para organizar tarefas, compromissos, materiais e finanças.                   | Atrasos, retrabalho, perda de eficiência e dificuldade em planejar ações estratégicas.       |
| **Armazenamento de Dados** | Armazenamento descentralizado de documentos e atas.                                                            | Compromete a transparência, dificulta o acesso à informação e aumenta o risco de perda de dados. |

<div style="text-align: justify;"> 

Esses problemas apontam para a urgência de implementar um software que centralize e integre as funcionalidades necessárias. A plataforma deverá:  

</div>

1. **Fortalecer a presença externa** com uma identidade visual consolidada e ferramentas para atrair novos membros e patrocinadores.  
2. **Otimizar a gestão interna**, promovendo organização, eficiência e transparência nos processos da equipe.  
3. **Garantir segurança de dados** com armazenamento centralizado e fácil acesso a informações essenciais.  

<div style="text-align: justify;"> 

A adoção dessa solução tecnológica é crucial para superar os gargalos atuais, fortalecer a equipe e maximizar seu desempenho competitivo.

</div>

| Categoria       | Causas Identificadas                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------|
| **Pessoas**     | Falta de integração entre os membros; dificuldade em acompanhar tarefas e reuniões.                   |
| **Processos**   | Gestão manual ou uso de ferramentas dispersas; ausência de um padrão de operação.                     |
| **Tecnologia**  | Inexistência de uma plataforma de integração única e dedicada às necessidades específicas da equipe.                 |
| **Comunicação** | Divulgação fragmentada, impactando o alcance do público-alvo e a captação de recursos.                |

<div style="text-align: justify;">

A tabela resume as principais causas da ineficiência na gestão e divulgação da equipe. Entre elas, a falta de integração entre os membros dificulta o acompanhamento de tarefas e reuniões, enquanto a ausência de um padrão nos processos e o uso de ferramentas dispersas tornam a gestão desorganizada. <br> <br>

Além disso, a inexistência de uma plataforma única que atenda às necessidades específicas da equipe agrava os problemas tecnológicos. Por fim, a divulgação fragmentada impacta negativamente o alcance do público-alvo e dificulta a captação de recursos. Esses fatores evidenciam a urgência de uma solução centralizada para melhorar a organização interna e fortalecer a comunicação externa.

O digrama abaixo identifica as causas do problema central: Ineficiência na gestão e divulgação da equipe: <br> <br>

</div>

(colocar diagrama aqui.)

![Diagrama de Ishikawa](/docs/view/img/Diagrama%20de%20Ishikawa%20da%20Mamute.jpg)

---

### 1.1.3 Solução Proposta

<div style="text-align: justify;">

A solução proposta é a criação de um aplicativo web unificado que aborda os principais desafios da equipe. Na dimensão de Divulgação Externa, o sistema oferecerá uma página inicial atraente que fortaleça a identidade visual dos Mamutes do Cerrado, com informações relevantes sobre os integrantes, competições e o processo seletivo. Na dimensão de Gestão Interna, incluirá módulos para organizar tarefas e eventos com ferramentas visuais como Kanban e calendário, controlar o estoque de materiais e peças, registrar atas de reuniões e gerenciar documentos de forma centralizada e acessível. Essa abordagem visa melhorar tanto a organização interna quanto a presença externa da equipe. <br> <br>

A seguinte tabela demonstra a dimensão do problema analoga a sua proposta de solucão aliada a funcionalidade:

</div>

| Dimensão             | Funcionalidade                                                                                    |
|----------------------|---------------------------------------------------------------------------------------------------|
| **Divulgação Externa** | Página inicial atraente com identidade visual, informações sobre integrantes, competições e processo seletivo. |
| **Gestão Interna**    | **Calendário e Tarefas**: Organização visual com Kanban e calendário consolidado.                |
|                      | **Estoque**: Controle de materiais e peças.                                                       |
|                      | **Reuniões**: Registro de atas e controle de presença.                                            |
|                      | **Documentos**: Centralização e fácil acesso a arquivos importantes.                              |

---

### 1.1.4 Justificativa da Solução

<div style="text-align: justify;">

A justificativa para a criação do aplicativo está nos benefícios que ele traz para a equipe. A centralização das operações permitirá maior eficiência operacional, reduzindo o tempo gasto com tarefas administrativas e permitindo mais foco nas competições. Além disso, a solução promove transparência e organização, com dados acessíveis e bem estruturados para todos os membros. Na dimensão externa, o aplicativo fortalecerá o engajamento, aumentando a visibilidade da equipe e atraindo talentos e recursos estratégicos. Por fim, ao oferecer um ambiente mais estruturado e motivador, o aplicativo contribuirá diretamente para o sucesso da equipe, resolvendo os problemas atuais. <br> <br>

Podendo ser analisados com mais detalhes na tabela seguinte: <br> 

</div>

| Benefício                   | Descrição                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------|
| **Eficiência Operacional**  | Redução do tempo gasto em tarefas administrativas, permitindo maior foco nas competições.   |
| **Transparência e Organização** | Centralização de dados, garantindo acesso fácil e claro para os membros da equipe.           |
| **Engajamento Externo**     | Aumento da visibilidade, atração de novos talentos e captação de recursos estratégicos.      |
| **Ambiente Estruturado**    | Proporciona maior motivação e organização, contribuindo para o sucesso da equipe.            |

---

### 1.2 Declaração de Posição do Produto

<div style="text-align: justify;">

O <strong>produto</strong> proposto oferece ferramentas de organização interna, como o controle de tarefas, agendamento de compromissos e gestão de documentos, além de facilitar a <strong>divulgação externa</strong> com recursos para promover a equipe, aumentar sua visibilidade e atrair novos membros e patrocinadores. Dessa forma, ele aborda tanto as necessidades internas quanto as externas de forma prática e eficiente. <br> <br>

Ao contrário das soluções dispersas ou inexistentes que dificultam a comunicação e a organização, o <strong>nosso produto</strong> integra todas essas funcionalidades em um único ambiente digital, acessível a todos os membros da equipe, proporcionando uma experiência mais fluida, organizada e profissional para os Mamutes do Cerrado. Todos esses pontos podem ser visualizados com detalhes no quadro abaixo:

</div>

| **Para**       | Mamutes do Cerrado           |
|---------|--------------------------------|
| **Necessidade**       | Centralizar a gestão e melhorar a visibilidade da equipe. |
| **O Produto**       | Uma aplicação web.     | 
| **Que**       | Oferece ferramentas de organização interna e divulgação externa.     | 
| **Ao Contrário**       | De soluções dispersas ou inexistentes.     | 
| **Nosso Produto**       | Integra gestão e divulgação em um único ambiente acessível.     | 

---

### 1.3 Objetivos do Produto

<div style="text-align: justify;">

O objetivo <strong>principal</strong> da solução é otimizar a gestão interna da equipe e fortalecer sua presença externa, abordando as dificuldades atuais de organização e visibilidade. Para isso, a aplicação proposta busca automatizar tarefas administrativas, permitindo que a equipe se concentre mais nas atividades essenciais. Além disso, a plataforma facilita a <strong>comunicação interna e externa</strong>, proporcionando uma interação mais eficiente entre os membros da equipe e com o público-alvo. <br> <br>

Outro aspecto importante é garantir <strong>acessibilidade aos documentos e recursos</strong> da equipe, permitindo que todos os membros possam acessar informações relevantes de forma rápida e organizada. Dessa forma, a solução não só melhora a operação interna, mas também contribui para uma maior visibilidade e engajamento externo, com uma gestão mais fluida e transparente.

</div>

Podendo ser analisados com mais detalhes na tabela seguinte: <br> 

| Objetivo        | Descrição                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------|
| **Principal**   | Otimizar a gestão interna e fortalecer a presença externa da equipe.                      |
| **Secundários** |                                                                                             |
| **Automatizar tarefas administrativas** | Reduzir o tempo gasto com atividades repetitivas, permitindo mais foco nas ações principais. |
| **Facilitar a comunicação interna e externa** | Melhorar a troca de informações dentro da equipe e com o público externo, tornando-a mais eficiente. |
| **Garantir acessibilidade aos documentos e recursos** | Proporcionar fácil acesso a arquivos e materiais importantes, garantindo que todos os membros tenham as informações necessárias. |

---

### 1.4 Tecnologias a Serem Utilizadas

<div class="text-align: justify;">
    <p><em><strong></strong> Tecnologias e ferramentas utilizadas no desenvolvimento do sistema:</em></p>
</div>

| Componente             | Definição                                                                                      | Uso                                                                                       |
|------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Linguagem**: Python 🐍 | Linguagem de programação de alto nível utilizada para desenvolvimento de aplicações web e scripts. | Utilizada para o desenvolvimento do backend do sistema, garantindo flexibilidade e escalabilidade. |
| **Framework**: Django 🖥️ | Framework web de alto nível para construção de aplicações rápidas e seguras em Python.         | Facilita a criação de APIs e integração com banco de dados, além de proporcionar segurança ao sistema. |
| **Banco de Dados**: MySQL 🗄️ | Sistema de gerenciamento de banco de dados relacional que utiliza SQL para consultas.           | Utilizado para armazenar dados estruturados da aplicação, como informações de usuários e registros de atividades. |
| **Front-End**: HTML, CSS, Bootstrap 💻 | Tecnologias utilizadas para construir a interface de usuário do sistema, proporcionando um design responsivo e atraente. | Usadas para criar a estrutura, o estilo visual e tornar o sistema acessível em diversos dispositivos. |
| **Ferramentas**: Visual Studio Code 🖱️, Astah 🌐, Git e GitHub 💼 | Ferramentas utilizadas no processo de desenvolvimento e versionamento do código.                | Visual Studio Code é utilizado para programação, Astah para diagramas e Git/GitHub para controle de versões. |
| **Metodologia**: Scrum e XP 📅 | Metodologias ágeis utilizadas para organização e execução do projeto, focando na entrega contínua de valor. | Usadas para garantir entregas rápidas e melhoria contínua no processo de desenvolvimento. |

---

## 2. Visão Geral do Projeto

### 2.1 Ciclo de Vida do Projeto

<div style="text-align: justify;">

O ciclo de vida do projeto será ágil, baseado nas metodologias <strong>SCRUM</strong> e <strong>XP</strong>, visando garantir eficiência e organização no desenvolvimento. Com essa abordagem, espera-se que o projeto seja concluído dentro do prazo estipulado e atenda a todos os requisitos definidos. Para isso, será utilizado como referência o <strong>SCRUM Guide</strong> e o <strong>XP Guide</strong>, além de boas práticas amplamente discutidas na literatura técnica. <br> <br>

Entre os métodos aplicados estão <strong>pair programming</strong>, que acelera o desenvolvimento e promove a troca de conhecimento entre os desenvolvedores, e <strong>code review</strong>, garantindo maior qualidade no código. Outros métodos incluem o uso de padrões de codificação, planejamento de <strong>releases e sprints</strong>, além de execução de testes de aceitação. Essas práticas contribuem para um desenvolvimento mais controlado e de alta qualidade, atendendo às demandas do projeto. <br> <br>

Quanto às ferramentas, serão utilizados o <strong>GitHub</strong> para repositório e controle de versionamento do código, bem como o <strong>Astah</strong> para modelagem de diagramas e o <strong>Miro</strong> para organização visual e gerenciamento do backlog. 

</div>

---

### 2.2 Organização do Projeto

<div style="text-align: justify;">

O o seguinte quadro apresenta os principais papéis e responsabilidades dentro do projeto. O <strong>Cliente</strong> (Equipe Mamutes) é responsável por fornecer feedback contínuo e acompanhar o progresso das entregas, garantindo que o produto final atenda às suas necessidades. <br> <br>

</div>


| Papel                | Atribuições                                                 | Responsáveis                |
|----------------------|------------------------------------------------------------|-----------------------------|
| **Cliente**          | Fornecer feedback e acompanhar o progresso                 | Equipe Mamutes              |
| **Scrum Master**  | Atualizar escopo e validar entregas                        | Caio Duarte    |
| **Líderes de Squad**    | Fomentar os desenvolvedores, aliada ao squad que o compete, sendo eles: Front, Back e Testes, e atuar como reviwers quanto ao versionamento e afins. | Ludmila Aysha;	Rafael Welz e	Felipe Freire    |
| **Desenvolvedores**    | Codificar e realizar implementações                      | Equipe dev   |
| **Analistas de Qualidade** | Garantir qualidade e execuctar testes de software    | Equipe dev  |

Acesse este link para saber com detalhes cada equipe: [Integrantes Equipe](https://github.com/FGA0138-MDS-Ajax/2024.2-Aries/tree/main)


<div style="text-align: justify;">

O <strong>Scrum Master</strong> (Caio Duarte) atualiza o escopo do projeto e valida as entregas, assegurando que o time siga os processos ágeis de Scrum e que o trabalho seja entregue com qualidade. <br> <br>

Os <strong>Líderes de Squad</strong> lideram as equipes de desenvolvimento, incentivando e orientando os membros. Eles também atuam como revisores de código, garantindo que o versionamento e as práticas de desenvolvimento sejam seguidos corretamente. Os <strong>Desenvolvedores</strong> são os responsáveis por codificar e implementar as funcionalidades do sistema, transformando as necessidades em soluções práticas e operacionais. <br> <br>

Por fim, os <strong>Analistas de Qualidade</strong> executam testes de software para garantir que o produto esteja livre de erros e com a qualidade necessária. Cada papel tem uma função essencial para o sucesso do projeto, garantindo colaboração, organização e entrega de um produto confiável e bem executado.

</div>

---

### 2.3 Planejamento das Fases

As fases serão detalhadas e adaptadas em cada sprint, com priorização do backlog com entregas claras e incrementais:  

| Sprint  | Produto (Entrega)                                                                                                 | Data Início  | Data Fim      | % Conclusão |
|---------|-------------------------------------------------------------------------------------------------------------------|--------------|---------------|-------------|
| 1       | Definição do Produto                                                                                              | 10/11/2024   | 18/11/2024    | 100%          |
| 2       | Documentação de arquitetura, Criação de Banco de dados em MySql, Finalizar Documento da Visão, Página Quem Somos  | 18/11/2024   | 25/11/2024    | ?%          |
| 3       | Página de Competição, Página de Processo Seletivo, Página Configurações de Conta                                  | 25/11/2024  | 02/11/2024    | 0%          |
| 4       |Menu lateral, Aba home, Aviso, Times da equipe                                                                     | 02/12/2024   | 09/11/2024   | 0%          |
| 5       |Criação de tarefas, Calendário                                                                                     | 09/12/2024   | 16/11/2024    | 0%          |
| 6       | Rastreio de tarefas, Kanban                                                                                       | 30/12/2024  | 06/01/2025    | 0%          |
| 7       | Página Estoque                                                                                                    | 06/01/2025  | 13/01/2025      | 0%          |
| 8       | Página Registro de Acidentes, Página registro de vôo                                                              | 13/01/2025  | 20/01/2025    | 0%          |
| 9       |Página Registro de Acidentes                                                                                       | 20/01/2025   | 27/01/2025      | 0%          |
| 10      | Deploy                                                                                                            | 27/01/2025    | 02/02/2025   | 0%          |


#### 2.3.1 Detalhamento da Tabela

<div style="text-align: justify;">

As fases do projeto serão realizadas de maneira incremental, organizadas em sprints para priorizar entregas específicas e garantir progresso contínuo.  

Na <strong>Sprint 1</strong>, a equipe focará na <strong>definição do produto</strong>, alinhando objetivos e estabelecendo as bases para o desenvolvimento. Este passo inicial é essencial para assegurar que todos os membros tenham uma visão clara do escopo do projeto. <br> <br> 

A <strong>Sprint 2</strong> envolverá a produção da <strong>documentação de arquitetura</strong>, a criação do banco de dados em MySQL, a finalização do documento de visão e a entrega da página "Quem Somos". Essa etapa organizará os fundamentos técnicos do sistema. <br> <br>

As etapas seguintes, começando pela <strong>Sprint 3</strong>, irão abordar a implementação das páginas "Competição", "Processo Seletivo" e "Configurações de Conta", além de funcionalidades específicas como menus e avisos. Esse fluxo de trabalho visa manter um ritmo consistente e alinhado às prioridades do backlog. <br> <br>

</div>

---

### 2.4 Matriz de Comunicação

| Descrição                                       | Área/Envolvidos       | Periodicidade | Produtos Gerados                |
|------------------------------------------------|-----------------------|---------------|---------------------------------|
| Acompanhamento das Atividades em Andamento e situação do projeto    | Equipe do Projeto, Monitor e PO   | Semanal       | Ata de reunião|
| Acompanhamento de atividades em andamento (Stand-up meetings) | Líderes Squad, Scrum Master    | Diário     | Comunicação de alinhamento entre membros do squad       |

<div style="text-align: justify;">

O Acompanhamento das Atividades em Andamento e Situação do Projeto, realizado semanalmente pela Equipe do Projeto, Monitor e PO (Product Owner), tem como objetivo revisar o progresso das tarefas, discutir o estado atual do projeto e planejar ações para mitigar possíveis riscos. Como resultado, são gerados a Ata de Reunião, que registra as discussões e decisões. <br> <br>

Já o Acompanhamento de Atividades em Andamento (Stand-up Meetings) ocorre diariamente, sendo conduzido pelos Líderes de Squad e o Scrum Master. Esse encontro tem foco no alinhamento entre os membros do squad, promovendo a comunicação e garantindo que todos estejam cientes do progresso e dos próximos passos. A principal entrega desse acompanhamento é a Comunicação de Alinhamento, que mantém todos informados sobre o andamento das atividades e facilita a colaboração contínua.

</div>

---

### 2.5 Gerenciamento de Riscos

| Risco                      | Grau de Exposição | Mitigação                    | Plano de Contingência          |
|----------------------------|-------------------|------------------------------|--------------------------------|
| Atrasos no cronograma      | Alto              | Reorganização do backlog     | Redistribuir tarefas           |
| Perda de dados             | Médio             | Backup semanal               | Recuperação de backups         |
|Falta de comunicação eficiente na equipe |Médio |Estabelecer reuniões regulares e usar ferramentas para comunicação rápida (whatsapp) ou padronizada (teams) |Acionar o Srcum Master para centralizar informações e resolver dúvidas urgentes |
|Falta de conhecimento de membros da equipe |Alto|Identificar a deficiência e estudar|Redirecionar tarefas críticas para membros mais experientes ou buscar ajuda externa|
|Escopo mal definido ou mudanças de requisitos |Alto |Validar o escopo com o cliente antes de iniciar o desenvolvimento|Ajustar o cronograma e priorizar entregas essenciais em caso de mudanças inesperadas|
|Falta de recursos (tempo, ferramentas) |Médio |Monitorar os recursos necessários e informar problemas com antecedência|Ajustar o cronograma, buscar ferramentas gratuitas/alternativas e se necessário reavaliar o escopo do projeto|
|Problemas de compatibilidade no site |Baixo |Realizar testes em navegadores e dispositivos diferentes durante o processo|Corrigir problemas emergenciais e desativar funcionalidades que não comprometam o todo|
|Desistência de integrantes da equipe|Médio |Dividir tarefas de forma justa, manter boa comunicação e resolver  |Dividir tarefas de forma justa, manter boa comunicação e resolver|

---

### 2.6 Critérios de Replanejamento

<div style="text-align: justify;">

<strong>Mudanças nos requisitos: </strong> Sempre que houver alterações nos requisitos do projeto, seja por solicitação do cliente ou identificação de novas necessidades, o impacto dessas mudanças será avaliado. Se o impacto for significativo, será necessário ajustar o escopo e o cronograma, garantindo que os novos requisitos sejam integrados de maneira eficiente. <br> <br> 

<strong> Problemas de recursos: </strong> A indisponibilidade de recursos, como membros da equipe, ferramentas ou infraestrutura, exigirá uma reavaliação das atividades. Nessa situação, o replanejamento priorizará o uso dos recursos disponíveis para assegurar que as entregas críticas sejam concluídas. <br> <br> 

<strong> Baixa qualidade nas entregas: </strong> Caso entregas apresentem qualidade abaixo do esperado, problemas técnicos recorrentes ou as entregas planejadas não sejam cumpridas dentro do prazo acordado, será necessário revisar os processos e redefinir prazos para corrigir as falhas. <br> <br> 

<strong> Feedback do cliente: </strong> Se o cliente identificar insatisfações ou oportunidades de melhoria significativas no produto em desenvolvimento, as sugestões serão avaliadas. Caso aprovadas, o planejamento será revisado para incorporá-las, mediante a existência de período ágil.<br> <br> 

</div>

---

## 3. Processo de Desenvolvimento de Software

<div style="text-align: justify;">

O desenvolvimento do software para a equipe <strong>Mamutes do Cerrado</strong> será guiado pelas metodologias <strong>SCRUM</strong> e <strong>XP</strong>, escolhidas por sua eficácia em organizar equipes e promover práticas de programação de alta qualidade. O <strong>SCRUM</strong> será responsável por estruturar o trabalho da equipe, garantindo controle de tempo e produtividade, enquanto o <strong>XP</strong> trará suporte com técnicas específicas para o desenvolvimento do software. <br> <br>

O <strong>SCRUM</strong> será aplicado por meio de eventos como <strong>reuniões semanais de Planejamento e Entrega de Sprints</strong>, realizadas às segundas-feiras, e revisões de sprint, que permitirão avaliar o progresso e planejar melhorias. Além disso, as <strong>Stand-up Meetings diárias</strong> serão fundamentais para monitorar as atividades em andamento, identificar obstáculos e alinhar prioridades. Esses encontros irão reforçar a comunicação dentro da equipe, que é um elemento essencial para o sucesso do projeto. Sendo gerenciadas por meio dos lideres de squad. <br> <br>

Complementando, a metodologia <strong>XP</strong> será implementada com a formação de pares de programação, <strong>code review</strong>, uso de <strong>padrões de codificação</strong> e execução de <strong>testes de aceitação</strong>. Esses métodos garantirão que o software seja desenvolvido com qualidade, respeitando os prazos estabelecidos e atendendo às expectativas do cliente. Essa combinação de práticas ágeis proporcionará uma abordagem eficiente e colaborativa ao desenvolvimento do projeto. <br> <br>

</div>

---

## 4. Declaração de Escopo do Projeto

**Backlog do Produto**:  
- Requisitos obrigatórios (*Must*): Módulos de gestão e divulgação.  
- Requisitos desejáveis (*Should/Could*): Customização e integração com redes sociais.  

| Cenário   | Requisito                      | Sprint | Priorização | Tipo de Requisito   | Descrição                   |
|-----------|--------------------------------|--------|-------------|---------------------|-----------------------------|
| Gestão    | Calendário                     | 5      | Must        | Funcional           | gerenciamento de tarefas    |
| Divulgação| Página inicial                 | 1      | Must        | Funcional           | apresentar a equipe         |
| Divulgação| Página de Competição           | 3      | could       | Funcional           | seção de notícias no site   |
| Divulgação| Página de Processo Seletivo    | 3      | must        | Funcional           | informações do processo seletivo |
| Gestão    | Página Configurações de Conta | 3      | Must        | Funcional           | configuração de conta        |
| Navegação | Menu lateral (àrea restrita)   | 4      | Must        | Funcional           | Anavegação e pesquisa         |
| Divugação | Aba home                       | 4      | Must        | Funcional           | aba principal e de aviso       |
| Gestão    | Criação de tarefas             | 5      | Must        | Funcional           | criar e atribuir tarefas        |
| Gestão    | Rastreio de tarefas            | 6      | Must        | Funcional           | rastreamento do que ser feito, e do que foi        |
| Gestão    | Times da equipe                | 6      | Must        | Funcional           | destacando membros e a história da equipe         |
|Organização| Kanban                         | 6      | Must        | Funcional           | organizar, gerenciar e visualizar tarefas e projetos|
|Organização| Página Estoque                 | 7      | Must        | Funcional           | Apresentar a equipe         |
|Gestão     | Página Registro de Acidentes   | 8      | Must        | Funcional           | documentação de acidentes       |
|Gestão     | Página registro de vôo         | 8      | Must        | Funcional           | documentação de vôos        |


---

### 4.1 Backlog do Produto

<div style="text-align: justify;">

Tendo em vista o objetivo central do projeto, foram realizadas entrevistas com o cliente para compreender suas necessidades e estabelecer prioridades. Por meio de sessões de brainstorming e decisões conjuntas com o Product Owner, as funcionalidades principais foram definidas. Abaixo, estão as funcionalidades prioritárias para o sucesso do projeto:

</div>

| **Funcionalidade**                                     | **Descrição**                                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------------------------|
| **Site de Divulgação**                                 | Apresentar a identidade e atividades da equipe.                                        |
| **Cronograma e Calendário**                            | Planejamento de reuniões e eventos internos.                                           |
| **Sistema de Login**                                   | Acesso ao sistema de gerenciamento para membros e capitães.                            |
| **Sistema de Gerenciamento de Inventário**             | Controle de materiais e equipamentos da equipe.                                        |
| **Administração e Registro de Reuniões**               | Garantir a documentação de atas de reuniões.                                           |
| **Gestão de Documentos da Equipe**                     | Armazenamento de links de acesso rápido a documentos da equipe.                        |

Além dessas funcionalidades prioritárias, outras funcionalidades foram identificadas para fortalecer a divulgação externa e a organização interna da equipe. Estas incluem:

| **Funcionalidade**                                     | **Descrição**                                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------------------------|
| **Página de Apresentação**                             | Destacar membros e a história da equipe.                                               |
| **Página de Eventos Passados e Conquistas**            | Valorizar o legado e os resultados obtidos pela equipe.                               |
| **Seção de Informações sobre o Processo Seletivo**     | Atração de novos talentos para a equipe.                                               |
| **Apresentação Detalhada dos Drones**                  | Exibir os drones com os quais a equipe trabalha, destacando sua expertise técnica.     |

<div style="text-align: justify;">

Essas funcionalidades estão alinhadas com os objetivos estratégicos do projeto, focando tanto em visibilidade externa quanto em eficiência interna para os membros da equipe.

</div>

---

### 4.2 Perfis

<div style="text-align: justify;">

Os perfis de acesso do projeto foram criados para atender às necessidades específicas de cada tipo de usuário, garantindo organização e segurança. O Administrador tem o maior nível de acesso, sendo responsável por gerenciar os perfis de usuários, configurar o sistema e administrar permissões. <br> <br>

O Capitão lidera a equipe com acesso completo para gerenciar planilhas, atas, processo seletivo, presenças, estoque e a disponibilidade dos membros. Já os Membros têm permissões ajustadas às suas funções, permitindo a atualização de informações pessoais, visualização e edição de planilhas (quando autorizado), e gestão de estoques, se necessário. <br> <br>

Por fim, o Visitante pode acessar apenas o site de divulgação para conhecer a equipe, enquanto os Trainees, novos integrantes em treinamento, possuem acesso restrito às ferramentas essenciais para seu aprendizado e integração. Essa divisão garante eficiência no trabalho e um uso adequado do sistema. Pdendo ser analisados de maneira detalhada na seguinte tabela:

</div>

Tabela : Perfis de acesso

| Nome do Perfil   | Características do Perfil                                                                 | Permissões de Acesso                                                                                         |
|------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Administrador    | Responsável por manter os perfis de acesso da aplicação, criar novos usuários, alterar usuários existentes ou excluir usuários (Manter usuários). | Manter usuários, controle completo sobre configurações do sistema e acessos administrativos.                |
| Capitão          | Membro responsável pela Mamutes como um todo. Um membro é capitão (verificar capitães). | Terá login. Acesso completo a CRUD de planilhas, atas, processo seletivo, presenças, estoque e disponibilidade de membros. |
| Membro           | Membro da Mamutes de alguma das áreas existentes na equipe.                                | Terá login. Manter suas informações atualizadas, visualizar planilhas e editá-las quando permitido, gerenciar estoque (quando necessário). |
| Visitante        | Usuário interessado em obter informações sobre a Mamutes e conhecer a equipe.               | Não terá login. Acesso ao site de divulgação.                                                              |
| Treinee          | Membro em período inicial na equipe, destinado a aprendizagem e integração com a Mamutes. | Terá login. Acesso restrito para visualizar planilhas, consultar documentos e acompanhar cronogramas de tarefas. | 

---

### 4.3 Cenários

<div style="text-align: justify;">

Os <strong>cenários funcionais</strong> definidos para o sistema dos <strong>Mamutes do Cerrado</strong> abrangem desde a concepção inicial do projeto até a gestão completa de atividades e estoques, promovendo eficiência e organização. O ciclo inicia com a <strong>definição do produto</strong>, onde o backlog, identidade visual e documento de visão são estruturados, seguido pelo planejamento do <strong>MVP</strong> e organização das entregas do projeto. <br> <br> 

Funcionalidades voltadas para a interação com os usuários incluem <strong>login</strong> e <strong>cadastro de novos usuários</strong>, além da visualização de perfis. Já no âmbito operacional, o sistema permite a <strong>criação, edição e exclusão de atividades</strong>, garantindo flexibilidade na gestão das tarefas. Adicionalmente, há funcionalidades específicas para o <strong>estoque</strong>, como registro, atualização e exclusão de itens, essenciais para o controle dos recursos da equipe.  <br> <br>

Por fim, o sistema integra um <strong>calendário</strong> para gerenciamento de datas importantes, como eventos e prazos de entrega, ajudando na coordenação do time. Podem ser analisadas na seguinte tabela:

</div>

Tabela : Cenários funcionais

| Numeração do Cenário | Nome do Cenário                         | Descrição                                                                                                   |
|-----------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 1                     | Definição do produto, backlog, identidade visual, documento de visão | Definir os principais aspectos do produto, incluindo backlog inicial, identidade visual e documento de visão. |
| 2                     | MVP e planejamento do projeto          | Planejar o desenvolvimento do MVP e estruturar as entregas ao longo do projeto.                              |
| 3                     | Login de Usuário                       | Implementar funcionalidade para autenticação de usuários no sistema.                                        |
| 4                     | Cadastro de Novo Usuário               | Permitir o registro de novos usuários no sistema.                                                           |
| 5                     | Visualização de Perfil do Usuário      | Permitir aos usuários visualizar seus próprios perfis, com informações detalhadas.                          |
| 6                     | Criação de Atividade                   | Implementar a funcionalidade de adicionar novas atividades no sistema.                                      |
| 7                     | Edição de Atividade                    | Permitir a modificação de atividades existentes no sistema.                                                 |
| 8                     | Exclusão de Atividade                  | Implementar a funcionalidade para excluir atividades do sistema.                                            |
| 9                     | Criação de Estoque                     | Criar e registrar novos itens no estoque através do sistema.                                                |
| 10                    | Edição de Estoque                      | Permitir a atualização das informações de itens no estoque.                                                 |
| 11                    | Exclusão de Estoque                    | Implementar a funcionalidade de remover itens do estoque no sistema.                                        |
| 12                    | Gerenciamento de Calendário            | Implementar um calendário para marcar eventos internos como reuniões, competições e datas importantes.       |
| 13                    | Agendamento de Entregas                | Permitir aos membros definir e acompanhar datas de entrega de tarefas e projetos no calendário.             |
| 14                    | Notificações de Eventos e Prazos       | Adicionar funcionalidade de notificações automáticas para lembrar membros sobre eventos e prazos registrados. |

---

### 4.4 Tabela de Backlog do Produto


<p style="text-align: justify;">



</p>

<iframe width="768" height="432" src="https://miro.com/welcomeonboard/aGh1UkhGYkpsMGUxdUxkTE9kYnRkdlR4ZEdSYUdEQ0lQVmE5dDFwc3NnS1l0czB4VTJJNnl3TXN6cWRvRXVIU1pqSlJEc1lHUmw5Q25VNmZnZks1RVdqQ05wSHAwbEcrNTloazlNdGg2VHJNVUNPTnBmcFRLY3lGOG80VUZKbEQhZQ==?share_link_id=967577464010" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

<p style="text-align:center;">
    Figura 1 - <a href ="https://miro.com/welcomeonboard/aGh1UkhGYkpsMGUxdUxkTE9kYnRkdlR4ZEdSYUdEQ0lQVmE5dDFwc3NnS1l0czB4VTJJNnl3TXN6cWRvRXVIU1pqSlJEc1lHUmw5Q25VNmZnZks1RVdqQ05wSHAwbEcrNTloazlNdGg2VHJNVUNPTnBmcFRLY3lGOG80VUZKbEQhZQ==?share_link_id=967577464010">Backlog do Produto</a> <br />
    Fonte: Autores.
</p>

<!--
Tabela : Backlog do produto

| Numeração (Cenário / Requisito) | Sprint | Nome do Requisito | Tipo de Requisito (Funcional / Não Funcional) | Priorização do Requisito (Must, Should, Could) | Descrição Sucinta do Requisito            | User Stories (U.S.) Associadas            |
|--------------------------------|--------|-------------------|-----------------------------------------------|-----------------------------------------------|-------------------------------------------|-------------------------------------------|
| <Número>                      | <Sprint> | <Nome>            | <Funcional/Não Funcional>                     | <Must/Should/Could>                          | <Descrição breve do requisito>            | <Identifique as U.S. associadas ao requisito> |

-->

---

## Referências Bibliográficas

- **Quais são os 12 Princípios da Gestão de Projetos Ágeis?**  
  Disponível em: [https://businessmap.io/pt/metodologia-agil/principios-manifesto-agil](https://businessmap.io/pt/metodologia-agil/principios-manifesto-agil)  

- **SWEBOK - Software Engineering Body of Knowledge**  
  Disponível em: [https://www.computer.org/education/bodies-of-knowledge/software-engineering](https://www.computer.org/education/bodies-of-knowledge/software-engineering)  

- **O que é backlog do produto Scrum e como fazer um**  
  Disponível em: [https://www.lucidchart.com/blog/pt/como-fazer-um-backlog-do-produto](https://www.lucidchart.com/blog/pt/como-fazer-um-backlog-do-produto)  

- **Diagrama de Ishikawa**  
  Disponível em: [https://miro.com/pt/diagrama/o-que-e-diagrama-ishikawa/](https://miro.com/pt/diagrama/o-que-e-diagrama-ishikawa/)  

- **Documento de Visão do Produto**  
  Disponível em: [https://kb.ufla.br/books/termos-e-definicoes/page/documento-de-visao-do-produto](https://kb.ufla.br/books/termos-e-definicoes/page/documento-de-visao-do-produto)  

---

## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 25/11/2024 | Criação inicial e estrutura do artefato | Felipe Freire e Amanda Cruz Lima |
| 1.0 | 25/11/2024 | Desenvolvimento do artefato **contexto do problema**, **declaração do produto**, **objetivo do produto** e **tecnologias a serem utilizadas**   | Felipe Freire |
| 1.1 | 29/11/2024 | Evolução dos artefatos **contexto do problema**, **declaração do produto**, **objetivo do produto** e **tecnologias a serem utilizadas**   | Felipe Freire |
| 1.2 | 29/11/2024 | Desenvolvimento dos artefatos **ciclo de vida do projeto**   | Felipe Freire |
| 1.3 | 29/11/2024 | Desenvolvimento dos artefatos **backlog do produto**, **perfis** e **cenários**   | Felipe Freire e Felipe Duarte |
| 1.4 | 02/12/2024 | Desenvolvimento dos artefatos **Gerenciamento de Riscos** e **Critérios de Replanejamento**| Isaque Camargos | 
| 1.5 | 02/12/2024 | Upgrade nos artefatos **backlog do produto**, **perfis**, **cenários** e **declaração de escopo**   | Felipe Freire e Felipe Duarte | 
| 1.6 | 02/12/2024 | Ajuste no texto do **diagrama espinha de peixe** e inserção das **referencias** | Felipe Freire | 

