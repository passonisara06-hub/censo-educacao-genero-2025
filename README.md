# 📊 Desigualdades de Gênero na Educação Básica Brasileira

## Análise dos Microdados do Censo Escolar 2025 para Proposição de Políticas Públicas

**Autora:** Sara - Mestra em Educação

---

## 🎯 Objetivo Geral

Investigar as disparidades de gênero na trajetória educacional brasileira, desde a Educação Infantil até o Ensino Médio, identificando padrões de desigualdade que possam orientar políticas públicas para uma educação mais equitativa.

---

## ❓ Perguntas Norteadoras

| Pergunta | Relevância Social |
|----------|-------------------|
| **1. Onde estão as meninas?** | Existe evasão diferencial por gênero em determinadas etapas? |
| **2. Quem são as gestoras?** | Mulheres dirigem escolas, mas em que proporção e em quais redes? |
| **3. Educação Infantil: responsabilidade feminina?** | Bebês e crianças pequenas são cuidados majoritariamente por mulheres? |
| **4. Ensino Médio: que futuro se desenha?** | Jovens mulheres e homens estão se preparando para quê? |
| **5. Docência: profissão feminina, gestão masculina?** | Há teto de vidro na carreira educacional? |

---

## 🗂️ Estrutura do Projeto

```
Censo25/
├── data/                              # Dados do INEP
│   ├── *.csv                          # Arquivos CSV originais do Censo
│   └── processed/                     # Dados processados
│
├── notebooks/                         # Análises passo a passo
│   ├── 01_carregamento_e_limpeza.ipynb
│   ├── 02_analise_matriculas_por_genero.ipynb
│   ├── 03_analise_gestao_escolar.ipynb
│   └── 04_sintese_e_visualizacoes.ipynb
│
├── outputs/                           # Resultados finais
│   ├── figures/                       # Gráficos gerados
│   │   ├── 01_funil_educacao_meninas.png
│   │   ├── 02_genero_por_rede.png
│   │   ├── 03_meninas_por_regiao.png
│   │   ├── 04_genero_gestores.png
│   │   ├── 05_gestoras_por_rede.png
│   │   ├── 06_gestoras_por_regiao.png
│   │   ├── dashboard_completo.png
│   │   └── teto_vidro_educacao.png
│   ├── resumo_executivo.csv
│   ├── recomendacoes_politicas.csv
│   └── relatorio_final.md
│
├── scripts/                           # Código reutilizável
│   ├── config.py                      # Configurações do projeto
│   └── utils.py                       # Funções auxiliares
│
├── venv/                              # Ambiente virtual Python
├── requirements.txt                   # Dependências do projeto
├── setup.sh                           # Script de configuração
├── README.md                          # Este arquivo
└── .gitignore                         # Arquivos ignorados pelo git
```

---

## 🚀 Como Utilizar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe este projeto**

2. **Execute o script de configuração:**
```bash
bash setup.sh
```

Ou manualmente:
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

3. **Inicie o Jupyter Notebook:**
```bash
jupyter notebook
```

4. **Execute os notebooks em ordem:**
   - `01_carregamento_e_limpeza.ipynb`
   - `02_analise_matriculas_por_genero.ipynb`
   - `03_analise_gestao_escolar.ipynb`
   - `04_sintese_e_visualizacoes.ipynb`

---

## 📊 Notebooks

### Notebook 01: Carregamento e Limpeza
- Carrega os microdados do Censo Escolar 2025
- Seleciona variáveis relevantes para análise de gênero
- Realiza limpeza e tratamento inicial dos dados
- Salva dados processados para análises subsequentes

### Notebook 02: Análise de Matrículas por Gênero
- Analisa a distribuição de meninos e meninas por etapa de ensino
- Identifica padrões de evasão escolar por gênero
- Compara proporções de gênero entre regiões
- Responde: "Onde estão as meninas?"

### Notebook 03: Análise de Gestão Escolar
- Analisa a distribuição de gênero entre gestores escolares
- Identifica o "teto de vidro" na carreira educacional
- Compara proporção de gestoras por rede e região
- Responde: "Quem são as gestoras?"

### Notebook 04: Síntese e Visualizações
- Integra todas as análises realizadas
- Cria visualizações síntese de alto impacto
- Elabora recomendações de políticas públicas
- Gera relatório final da análise

---

## 🎨 Visualizações

O projeto gera os seguintes gráficos:

1. **Funil da Educação** - Proporção de meninas em cada etapa de ensino
2. **Distribuição por Rede** - Porcentagem de meninas por rede de ensino
3. **Mapa Regional** - Disparidades de gênero por região
4. **Gestores por Gênero** - Distribuição geral de gestores
5. **Gestoras por Rede** - Proporção de gestoras por tipo de rede
6. **Gestoras por Região** - Mapa regional da gestão feminina
7. **Dashboard Completo** - Visão integrada de todas as análises
8. **Teto de Vidro** - Representação da hierarquia educacional

---

## 📈 Principais Descobertas

### 1. A Perda de Meninos no Ensino Médio
Meninos estão abandonando a escola mais cedo. Políticas de permanência precisam considerar as necessidades específicas dos jovens homens.

### 2. O Teto de Vidro na Gestão Escolar
As mulheres são maioria na docência, mas minoria na gestão. A carreira docente tem um "teto de vidro": mulheres ensinam, homens dirigem.

### 3. A Feminização do Cuidado
Na educação infantil, a presença feminina é esmagadora. O cuidado com crianças pequenas ainda é visto como "dom natural" feminino.

---

## 💡 Recomendações de Políticas Públicas

1. **Bolsas permanência para jovens do Ensino Médio**, com recorte de gênero e raça
2. **Programa "Meninas na Ciência"** para incentivar meninas em áreas STEM
3. **Formação continuada em equidade de gênero** para gestores escolares
4. **Valorização profissional da Educação Infantil**, reconhecendo o cuidado como trabalho
5. **Creches em tempo integral** para apoiar mães trabalhadoras estudantes
6. **Programa de Formação de Lideranças Femininas** na educação

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem principal
- **pandas** - Manipulação de dados
- **numpy** - Cálculos numéricos
- **matplotlib** - Visualizações
- **seaborn** - Gráficos estatísticos
- **Jupyter Notebook** - Ambiente de análise

---

## 📚 Fonte de Dados

**Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)**
- Microdados do Censo Escolar 2025
- Disponível em: http://portal.inep.gov.br/microdados

---

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos e de pesquisa pública.

---

## 👤 Autora

**Sara** - Mestra em Educação
- Formação em Educação, História
- Especialização em Gênero e Desigualdades
- Análise de dados educacionais com Python

---

## 🙏 Agradecimentos

- INEP pela disponibilização dos microdados
- Comunidade Python científica
- Referências teóricas sobre gênero e educação

---

**Data de conclusão:** Março de 2026

**Versão:** 1.0
