# CLAUDE.md - Contexto do Projeto Censo25

## 👤 Perfil da Usuária

**Nome:** Sara
**Formação:** Mestra em Educação, com especialização em Gênero e Desigualdades
**Background:** Educação, História, análise de dados educacionais
**Objetivo:** Analisar desigualdades de gênero na educação básica brasileira usando dados do Censo Escolar 2025

---

## 🎯 Visão Geral do Projeto

### Título
**Desigualdades de Gênero na Educação Básica Brasileira**
Uma análise dos microdados do Censo Escolar 2025 para proposição de políticas públicas

### Objetivo Principal
Investigar disparidades de gênero na trajetória educacional brasileira, desde a Educação Infantil até o Ensino Médio, identificando padrões de desigualdade que possam orientar políticas públicas.

### Perguntas Norteadoras
1. **Onde estão as meninas?** - Evasão diferencial por gênero em determinadas etapas?
2. **Quem são as gestoras?** - Mulheres dirigem escolas, mas em que proporção e em quais redes?
3. **Educação Infantil: responsabilidade feminina?** - Bebês e crianças pequenas são cuidados majoritariamente por mulheres?
4. **Ensino Médio: que futuro se desenha?** - Jovens mulheres e homens estão se preparando para quê?
5. **Docência: profissão feminina, gestão masculina?** - Há teto de vidro na carreira educacional?

---

## 🗂️ Estrutura do Projeto

```
Censo25/
├── data/                              # Dados do INEP
│   ├── *.csv                          # Arquivos CSV originais do Censo
│   └── processed/                     # Dados processados
│
├── notebooks/                         # Análises Jupyter
│   ├── 01_carregamento_e_limpeza.ipynb
│   ├── 02_analise_matriculas_por_genero.ipynb
│   ├── 03_analise_gestao_escolar.ipynb
│   └── 04_sintese_e_visualizacoes.ipynb
│
├── outputs/                           # Resultados
│   ├── figures/                       # Gráficos gerados
│   ├── resumo_executivo.csv
│   ├── recomendacoes_politicas.csv
│   └── relatorio_final.md
│
├── scripts/                           # Código Python
│   ├── config.py                      # Configurações centralizadas
│   └── utils.py                       # Funções auxiliares
│
├── venv/                              # Ambiente virtual Python
├── requirements.txt
├── README.md
├── setup.sh
└── .gitignore
```

---

## 📊 Fontes de Dados

### Microdados do Censo Escolar 2025 - INEP
- **Localização:** `data/`
- **Separador:** ponto e vírgula (`;`)
- **Encoding:** Latin-1

### Tabelas Principais

1. **Tabela_Escola_2025.csv** (~164 MB)
   - Dados das escolas (localização, dependência, infraestrutura)
   - Inclui dados agregados de matrículas por gênero
   - Colunas de gênero: `QT_MAT_BAS_FEM`, `QT_MAT_BAS_MASC`, etc.

2. **Tabela_Matricula_2025.csv** (~95 MB)
   - Matrículas individuais dos alunos
   - Variável `TP_SEXO`: 1=Feminino, 2=Masculino

3. **Tabela_Gestor_Escolar_2025.csv** (~25 MB)
   - Dados dos gestores escolares
   - Variável `TP_SEXO`: 1=Feminino, 2=Masculino
   - Variável `TP_CARGO_GESTOR`: Cargo do gestor

4. **Tabela_Docente_2025.csv** (~59 MB)
   - Dados dos docentes
   - Variável `TP_SEXO`: 1=Feminino, 2=Masculino
   - Variável `TP_ESCOLARIDADE`: Escolaridade

---

## 🎨 Convenções de Código

### Paleta de Cores (Sensível a Gênero)
```python
CORES = {
    'feminino': '#E67E22',  # laranja (evita estereótipos rosa/azul)
    'masculino': '#3498DB', # azul
    'neutro': '#2ECC71',    # verde (para referências/paridade)
    'destaque': '#E74C3C',  # vermelho (para alertas)
    'total': '#95A5A6'      # cinza (para totais)
}
```

**Importante:** Evitar usar rosa para feminino e azul para masculino (estereótipos de gênero)

### Mapeamentos Padrão

```python
# Dependência administrativa
DEPENDENCIA = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Localização
LOCALIZACAO = {
    1: 'Urbana',
    2: 'Rural'
}

# Sexo
SEXO = {
    1: 'Feminino',
    2: 'Masculino',
    0: 'Não declarado'
}
```

---

## 🐍 Comandos Úteis

### Ambiente Virtual
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar Jupyter
jupyter notebook

# Desativar ambiente
deactivate
```

### Comandos de Análise (Python)
```python
# Importar configurações
import sys
sys.path.append('scripts')
from config import RAW_DATA_PATH, CORES
from utils import carregar_dados_otimizado

# Carregar dados CSV do Censo
df = pd.read_csv(
    RAW_DATA_PATH + 'Tabela_Escola_2025.csv',
    sep=';',
    encoding='latin1',
    low_memory=False
)

# Calcular porcentagem de mulheres
porc_mulheres = (df['TP_SEXO'] == 'Feminino').mean() * 100
```

---

## 📓 Estrutura dos Notebooks

### Notebook 01: Carregamento e Limpeza
- Carrega todas as tabelas do Censo
- Seleciona variáveis relevantes para análise de gênero
- Filtra escolas ativas (TP_SITUACAO_FUNCIONAMENTO == 1)
- Mapeia códigos para labels descritivos
- Salva dados processados em `data/processed/`

### Notebook 02: Análise de Matrículas
- Calcula proporção de meninas por etapa de ensino
- Cria gráfico de funil educacional
- Analisa distribuição por rede (Federal/Estadual/Municipal/Privada)
- Compara regiões brasileiras
- Identifica estados com maior/menor presença feminina

### Notebook 03: Análise de Gestão
- Calcula proporção de gestoras por rede e região
- Analisa "teto de vidro" na carreira
- Compara urbano vs rural
- Relaciona gênero do gestor com perfil da escola

### Notebook 04: Síntese
- Cria dashboard integrado
- Gera visualizações de alto impacto
- Elabora recomendações de políticas públicas
- Produz relatório final em markdown

---

## 💡 Temas e Conceitos Importantes

### Teto de Vidro na Educação
Conceito que descreve a barreira invisível que impede mulheres de alcançarem posições de liderança, apesar de serem maioria na base da carreira docente.

### Feminização do Cuidado
Tendência de que o cuidado com crianças pequenas seja predominantemente realizado por mulheres, reforçando estereótipos de gênero.

### Evasão Diferencial
Quando meninos ou meninas abandonam a escola em taxas diferentes em determinadas etapas de ensino.

### Interseccionalidade
Análise que considera múltiplas dimensões de desigualdade (gênero, raça, classe, região).

---

## 🎯 Objetivos de Análise

### Indicadores Principais
1. **Proporção de meninas na Educação Básica**
2. **Proporção de gestoras por rede de ensino**
3. **Funil educacional por gênero**
4. **Disparidades regionais**
5. **Relação urbano/rural**

### Padrões a Identificar
- Onde as meninas são maioria/minoria
- Em que redes as mulheres lideram mais
- Como a região influencia a presença feminina
- Se existe teto de vidro na gestão escolar

---

## 📝 Convenções de Output

### Gráficos
- Salvar em `outputs/figures/`
- Formato PNG, 300 DPI
- Usar paleta de cores sensível a gênero
- Incluir valores nas barras/gráficos
- Títulos descritivos e completos

### Tabelas
- Usar `display()` do pandas para melhor visualização
- Formatar números com separadores de milhar
- Arredondar porcentagens para 1 casa decimal

### Relatórios
- Usar markdown para documentação
- Incluir contexto educacional
- Propor políticas públicas baseadas em evidências
- Linguagem acessível para públicos leigos

---

## 🔍 Preferências da Usuária

### Comunicação
- Valoriza explicações didáticas
- Gosta de conectar dados com teoria educacional
- Prefere visualizações claras e profissionais
- Interessa-se por implicações para políticas públicas

### Análise
- Foco em padrões estruturais de desigualdade
- Contextualização histórica e social
- Abordagem interseccional quando possível
- Crítica feminista dos dados

### Código
- Comentários explicativos em português
- Funções reutilizáveis em `utils.py`
- Configurações centralizadas em `config.py`
- Código limpo e documentado

---

## 🚀 Próximos Passos Sugeridos

1. **Expansão com recorte racial** - Cruzar dados de gênero com raça/cor
2. **Análise temporal** - Comparar com censos anteriores (se disponíveis)
3. **Dashboard interativo** - Criar app com Plotly Dash ou Streamlit
4. **Publicação científica** - Artigo para revista de educação
5. **Apresentação para gestores** - Slides com recomendações

---

## 📚 Referências Teóricas Relevantes

- Estudos sobre gênero e educação no Brasil
- Literatura sobre teto de vidro na docência
- Pesquisas sobre evasão escolar por gênero
- Teorias feministas intersectionais

---

## ⚠️ Notas Importantes

1. **Dados sensíveis:** O projeto lida com dados educacionais que podem revelar desigualdades estruturais. Manter postura ética e crítica.

2. **Estereótipos:** Sempre evitar reforçar estereótipos de gênero nas visualizações e análises.

3. **Contextualização:** Os dados devem ser analisados considerando o contexto histórico e social brasileiro.

4. **Limitações:** Reconhecer limitações dos dados (ex: dados binários de gênero, ausência de interseccionalidade).

---

## 🔄 Atualizações

**Criado em:** Março de 2026
**Versão:** 1.0
**Última atualização:** 05/03/2026

---

**Este arquivo ajuda o Claude Code a entender o contexto e preferências da usuária para futuras interações.**
