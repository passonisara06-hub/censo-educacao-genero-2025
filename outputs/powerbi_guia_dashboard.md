# 📊 Guia Completo: Dashboards Power BI - Censo Escolar 2025

**Autora:** Sara - Mestra em Educação
**Data:** 06 de março de 2026
**Objetivo:** Criar 5 painéis interativos no Power BI

---

## 📋 Estrutura dos Arquivos

```
outputs/
├── powerbi_panacional.csv          # Dados panorama nacional
├── powerbi_por_rede.csv            # Dados por rede de ensino
├── powerbi_por_regiao.csv          # Dados por região
├── powerbi_por_uf.csv              # Dados por UF (para mapa)
├── powerbi_urbano_rural.csv        # Dados urbano vs rural
├── powerbi_inversao_genero.csv     # Dados inversão de gênero
└── powerbi_estatisticas.csv        # Dados estatísticos
```

---

## 🎨 Paleta de Cores (Power BI)

Copie e cole estas cores Custom no Power BI:

```
Feminino: #E67E22 (Laranja)
Masculino: #3498DB (Azul)
Neutro/Paridade: #2ECC71 (Verde)
Destaque: #E74C3C (Vermelho)
Total: #95A5A6 (Cinza)
```

**No Power BI:** → View → Themes → Customize colors → Adicionar as cores acima

---

## 📌 PAINEL 1: Panorama Nacional (Visão Executiva)

### Objetivo
Visão executiva dos principais indicadores de gênero na educação brasileira.

### Passo a Passo

#### 1. Carregar Dados
```
Home → Get Data → Text/CSV → Selecionar "powerbi_panacional.csv"
```

#### 2. Criar Cartões (Cards)

**Cartão 1 - Total de Matrículas:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "Total de Matrículas")
- Título: "Total de Matrículas"
- Formatação: Font Size 20pt, Bold

**Cartão 2 - % Meninas:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "% Meninas")
- Título: "Meninas"
- Cor: #E67E22 (Laranja)
- Formatação: Font Size 32pt, Bold

**Cartão 3 - Total de Gestores:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "Total de Gestores")
- Título: "Total de Gestores"
- Formatação: Font Size 20pt, Bold

**Cartão 4 - % Gestoras:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "% Gestoras")
- Título: "Gestoras"
- Cor: #E74C3C (Vermelho - cor de destaque)
- Formatação: Font Size 32pt, Bold

**Cartão 5 - Índice de Representação:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "Índice de Representação")
- Título: "Índice de Representação"
- Cor: #2ECC71 (Verde)
- Formatação: Font Size 24pt, Bold

**Cartão 6 - Diferença:**
- Visual: Card
- Campo: Valor (filtrar por Indicador = "Diferença (pp)")
- Título: "Diferença Gestoras - Meninas"
- Cor: #E74C3C
- Formatação: Font Size 24pt, Bold

#### 3. Criar Gráficos de Pizza

**Gráfico 1 - Matrículas por Gênero:**
- Visual: Pie chart
- Legenda: Meninas, Meninos
- Valores: 49.4%, 50.6%
- Cores: #E67E22 (Meninas), #3498DB (Meninos)
- Título: "Matrículas Educação Básica"
- Detalhes: Mostrar porcentagem e valores
- Posição: Topo esquerdo

**Gráfico 2 - Gestores por Gênero:**
- Visual: Donut chart
- Legenda: Gestoras, Gestores
- Valores: 79.5%, 20.5%
- Cores: #E74C3C (Gestoras - destaque), #3498DB (Gestores)
- Título: "Gestores Escolares"
- Detalhes: Mostrar porcentagem e valores
- Posição: Topo direito

#### 4. Layout Sugerido

```
┌─────────────────────────────────────────────────┐
│  TÍTULO: Panorama Nacional - Censo Escolar 2025 │
├─────────────────────────────────────────────────┤
│                                                 │
│  [Total Matrículas]  [% Meninas]  [Total Gest]  │
│     46.018.380         49.4%        190.641      │
│                                                 │
│  [% Gestoras]    [Índice Rep]    [Diferença]    │
│      79.5%          1.61x          +30.1 pp      │
│                                                 │
│  📊 Pizza Matrículas        🍩 Donut Gestores   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📌 PAINEL 2: Análise por Rede de Ensino

### Objetivo
Comparar distribuição de gênero por rede (Federal, Estadual, Municipal, Privada).

### Passo a Passo

#### 1. Carregar Dados
```
Home → Get Data → Text/CSV → Selecionar "powerbi_por_rede.csv"
```

#### 2. Gráfico de Barras - % Meninas por Rede

- Visual: Clustered bar chart
- Eixo X: Rede de Ensino
- Eixo Y: Pct_Meninas
- Título: "% Meninas por Rede de Ensino"
- Cor: #E67E22 (Laranja)
- Linha de referência: 50% (cor #2ECC71)
- Rótulos de dados: Mostrar porcentagem
- Ordenação: Crescente por % Meninas

#### 3. Gráfico de Barras Empilhadas - Gestão por Rede

- Visual: Stacked column chart (100%)
- Eixo X: Rede de Ensino
- Eixo Y: Pct_Gestoras, Pct_Gestores
- Título: "Composição de Gênero na Gestão por Rede"
- Cores: #E74C3C (Gestoras), #3498DB (Gestores)
- Destaque: Federal (com apenas 26.3% gestoras)
- Rótulos de dados: Mostrar porcentagem

#### 4. Cartões de Destaque

**Cartão - Rede Federal Alerta:**
- Título: "⚠️ Rede Federal"
- Valor: "26.3% Gestoras"
- Cor de fundo: #FFF3E6 (Amarelo claro)
- Cor do texto: #E67E22
- subtítulo: "Possível teto de vidro"

#### 5. Layout Sugerido

```
┌─────────────────────────────────────────────────┐
│  TÍTULO: Análise por Rede de Ensino             │
├─────────────────────────────────────────────────┤
│                                                 │
│  [% Meninas por Rede]     [⚠️ Federal: 26.3%]   │
│  Barras horizontais         Cartão de alerta     │
│                                                 │
│  [Composição Gestão por Rede - Barras Empilhadas] │
│  Federal (26% | 74%)  Estadual  Municipal  Privada │
│                                                 │
│  Tabela Detalhada por Rede                      │
│  | Rede | % Meninas | % Gestoras | Escolas |    │
│                                                 │
└─────────────────────────────────────────────────┘
```

#### 6. DAX Measures (Opcional)

```
% Meninas Total =
CALCULATE(
    SUM(powerbi_por_rede[Pct_Meninas]),
    ALL(powerbi_por_rede)
)

% Gestoras Total =
CALCULATE(
    SUM(powerbi_por_rede[Pct_Gestoras]),
    ALL(powerbi_por_rede)
)

Diferenca_Gestoras_Meninas =
[% Gestoras Total] - [% Meninas Total]
```

---

## 📌 PAINEL 3: Disparidades Regionais

### Objetivo
Visualizar distribuição de gestoras por região e estados brasileiros.

### Passo a Passo

#### 1. Carregar Dados
```
Home → Get Data → Text/CSV → Selecionar:
• powerbi_por_regiao.csv
• powerbi_por_uf.csv
```

#### 2. Mapa Coroplético do Brasil

- Visual: Shape map (precisa do shape file do Brasil)
- OU usar: Filled map (requer conexão com Bing Maps)
- Localização: Estado (UF)
- Cor: Pct_Gestoras
- Título: "% de Gestoras por Estado"
- Paleta: Divergindo (verde para vermelho)
- Data labels: Mostrar sigla do estado e porcentagem

**Cores sugeridas:**
- 60-70%: #3498DB (Azul)
- 70-80%: #2ECC71 (Verde)
- 80-90%: #E67E22 (Laranja)
- 90%+: #E74C3C (Vermelho)

#### 3. Gráfico de Barras Horizontais - Regiões

- Visual: Clustered bar chart (horizontal)
- Eixo Y: Regiao
- Eixo X: Pct_Gestoras
- Título: "Gestoras por Região Brasileira"
- Cor: #E74C3C (Vermelho para destaque)
- Rótulos de dados: Mostrar porcentagem
- Ordenação: Decrescente por Pct_Gestoras

#### 4. Indicadores de Destaque

**Máxima:**
- Título: "🏆 Maior %"
- Valor: "Sul - 85.8%"
- Cor: #E74C3C

**Mínima:**
- Título: "📉 Menor %"
- Valor: "Norte - 63.9%"
- Cor: #3498DB

**Variação:**
- Título: "📊 Variação"
- Valor: "21.9 pp"
- Cor: #2ECC71

#### 5. Layout Sugerido

```
┌─────────────────────────────────────────────────┐
│  TÍTULO: Disparidades Regionais                │
├─────────────────────────────────────────────────┤
│                                                 │
│  [Mapa do Brasil]      [Barras Horizontais]    │
│  Coroplético           Regiões ordenadas        │
│  por % gestoras          decrescentemente        │
│                                                 │
│  [🏆 Sul: 85.8%]  [📉 Norte: 63.9%]  [21.9 pp] │
│                                                 │
│  Tabela por Região (opcional)                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📌 PAINEL 4: Urbano vs Rural

### Objetivo
Comparar indicadores de gênero entre áreas urbanas e rurais.

### Passo a Passo

#### 1. Carregar Dados
```
Home → Get Data → Text/CSV → Selecionar "powerbi_urbano_rural.csv"
```

#### 2. Gráficos Lado a Lado

**Gráfico 1 - Matrículas Urbano vs Rural:**
- Visual: Clustered column chart
- Eixo X: Localizacao
- Eixo Y: Pct_Meninas
- Título: "% Meninas - Urbano vs Rural"
- Cores: #E67E22 (Urbana), #3498DB (Rural)
- Rótulos de dados: Mostrar porcentagem

**Gráfico 2 - Gestoras Urbano vs Rural:**
- Visual: Clustered column chart
- Eixo X: Localizacao
- Eixo Y: Pct_Gestoras
- Título: "% Gestoras - Urbano vs Rural"
- Cores: #E74C3C (Urbana), #3498DB (Rural)
- Rótulos de dados: Mostrar porcentagem

#### 3. Indicadores de Diferença

**Cartão - Diferença Matrículas:**
- Título: "Diferença Meninas"
- Valor: "1.2 pp"
- subtítulo: "Urbana > Rural"
- Cor: #2ECC71

**Cartão - Diferença Gestoras:**
- Título: "Diferença Gestoras"
- Valor: "11.2 pp"
- subtítulo: "Urbana > Rural"
- Cor: #E74C3C (Alerta)

#### 4. Layout Sugerido

```
┌─────────────────────────────────────────────────┐
│  TÍTULO: Urbano vs Rural                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  [% Meninas]          [% Gestoras]               │
│  Barras lado a lado   Barras lado a lado         │
│  Urbana | Rural       Urbana | Rural            │
│                                                 │
│  [Dif: 1.2 pp]        [Dif: 11.2 pp]            │
│                                                 │
│  Tabela Comparativa                             │
│  | Local | % Meninas | % Gestoras | Escolas |  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📌 PAINEL 5: A Inversão de Gênero (Destaque)

### Objetivo
Destacar a principal descoberta: mulheres são mais representadas na gestão do que nas salas de aula.

### Passo a Passo

#### 1. Carregar Dados
```
Home → Get Data → Text/CSV → Selecionar "powerbi_inversao_genero.csv"
```

#### 2. Gráfico Comparativo Principal

- Visual: Clustered column chart
- Eixo X: Categoria
- Eixo Y: Porcentagem
- Título: "A Inversão de Gênero na Educação Brasileira"
- Subtítulo: "Mulheres são MAIORIA na gestão do que nas salas de aula"
- Cores: #E67E22 (Meninas), #E74C3C (Gestoras - vermelho para destaque)
- Rótulos de dados: Mostrar porcentagem e valores absolutos
- Linha de referência: 50% (cor #2ECC71)

#### 3. Indicadores de Impacto

**Cartão 1 - Índice de Representação:**
- Título: "Índice de Representação"
- Valor: "1.61x"
- subtítulo: "Mulheres estão 1.61x mais representadas na gestão"
- Cor de fundo: #E74C3C
- Cor do texto: Branco
- Font size: 28pt

**Cartão 2 - Diferença Absoluta:**
- Título: "Diferença Gestoras - Meninas"
- Valor: "+30.1 pp"
- subtítulo: "Pontos percentuais"
- Cor de fundo: #2ECC71
- Cor do texto: Branco

**Cartão 3 - Total Gestoras:**
- Título: "Total de Gestoras"
- Valor: "151.610"
- subtítulo: "Mulheres gestoras escolares"
- Cor de fundo: #E74C3C
- Cor do texto: Branco

#### 4. Caixa de Texto / Anotação

Adicionar uma caixa de texto com a interpretação:

```
🔍 DESCOBERTA CHAVE

Contrariando a narrativa do "teto de vidro", as
mulheres são MAIORIA na gestão escolar brasileira.

79.5% dos gestores são mulheres, representando uma
INVERSÃO de gênero em relação às salas de aula (49.4%).

Índice de Representação: 1.61x
```

#### 5. Layout Sugerido

```
┌─────────────────────────────────────────────────┐
│  TÍTULO: A INVERSÃO DE GÊNERO                   │
│  Subtítulo: Mulheres dominam a gestão escolar   │
├─────────────────────────────────────────────────┤
│                                                 │
│     [Índice: 1.61x]    [+30.1 pp]    [151.610]  │
│        Grandes          Diferença      Total     │
│        cartões          absoluta      gestoras   │
│                                                 │
│  📊 Gráfico Comparativo Principal               │
│  Meninas (49.4%) vs Gestoras (79.5%)            │
│  Barras lado a lado com linha de 50%            │
│                                                 │
│  📝 Caixa de texto com interpretação            │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎨 DAX Measures (Códigos para Copiar)

### Medidas Calculadas

```dax
// ========== PANORAMA NACIONAL ==========

Total Matriculas =
SUM(powerbi_panacional[Valor])

Pct Meninas =
CALCULATE(
    SUM(powerbi_panacional[Valor]),
    powerbi_panacional[Indicador] = "% Meninas"
)

Pct Gestoras =
CALCULATE(
    SUM(powerbi_panacional[Valor]),
    powerbi_panacional[Indicador] = "% Gestoras"
)

Indice Representacao =
DIVIDE([Pct Gestoras], [Pct Meninas])

// ========== ANÁLISE POR REDE ==========

Media Gestoras por Rede =
AVERAGEX(
    ALLSELECTED(powerbi_por_rede[Rede de Ensino]),
    powerbi_por_rede[Pct_Gestoras]
)

Max Gestoras por Rede =
MAXX(
    ALLSELECTED(powerbi_por_rede[Rede de Ensino]),
    powerbi_por_rede[Pct_Gestoras]
)

Min Gestoras por Rede =
MINX(
    ALLSELECTED(powerbi_por_rede[Rede de Ensino]),
    powerbi_por_rede[Pct_Gestoras]
)

// Alerta Federal
Alerta Federal =
IF(
    CALCULATE(
        SUM(powerbi_por_rede[Pct_Gestoras]),
        powerbi_por_rede[Rede de Ensino] = "Federal"
    ) < 50,
    "⚠️ Teto de Vidro",
    "✅ OK"
)

// ========== DISPARIDADES REGIONAIS ==========

Variação Regional =
[MAXX(ALL(powerbi_por_regiao), powerbi_por_regiao[Pct_Gestoras])] -
[MINX(ALL(powerbi_por_regiao), powerbi_por_regiao[Pct_Gestoras])]

Região Max Gestoras =
TOPN(
    1,
    ALL(powerbi_por_regiao),
    powerbi_por_regiao[Pct_Gestoras]
)

// ========== URBANO VS RURAL ==========

Dif Meninas UrbanoRural =
CALCULATE(
    SUM(powerbi_urbano_rural[Pct_Meninas]),
    powerbi_urbano_rural[Localizacao] = "Urbana"
) -
CALCULATE(
    SUM(powerbi_urbano_rural[Pct_Meninas]),
    powerbi_urbano_rural[Localizacao] = "Rural"
)

Dif Gestoras UrbanoRural =
CALCULATE(
    SUM(powerbi_urbano_rural[Pct_Gestoras]),
    powerbi_urbano_rural[Localizacao] = "Urbana"
) -
CALCULATE(
    SUM(powerbi_urbano_rural[Pct_Gestoras]),
    powerbi_urbano_rural[Localizacao] = "Rural"
)
```

---

## 🎯 Formatação Condicional

### Para Destacar Valores

**Na tabela ou matriz:**

```
Regra 1 - Alerta Federal:
Se Pct_Gestoras < 30 → Cor de fundo: #FFF3E6
Se Pct_Gestoras >= 30 → Sem formatação

Regra 2 - Destaque Alta Representação:
Se Pct_Gestoras >= 80 → Cor de fonte: #E74C3C, Bold
Se Pct_Gestoras < 80 → Cor de fonte: Preto

Regra 3 - Barras de Dados:
Campo: Pct_Gestoras
Tipo: Barra
Cor: #E74C3C
Direção: Horizontal
```

---

## 📱 Botões de Navegação

### Criar botões para alternar entre painéis

**Botão 1 - Panorama Nacional:**
- Tipo: Button
- Texto: "📊 Nacional"
- Ação: Bookmark → "PanoramaNacional"
- Ícone: Bar chart

**Botão 2 - Por Rede:**
- Tipo: Button
- Texto: "🏫 Por Rede"
- Ação: Bookmark → "PorRede"
- Ícone: Building

**Botão 3 - Regional:**
- Tipo: Button
- Texto: "🗺️ Regional"
- Ação: Bookmark → "Regional"
- Ícone: Globe

**Botão 4 - Urbano/Rural:**
- Tipo: Button
- Texto: "🏙️ Urb/Rural"
- Ação: Bookmark → "UrbanoRural"
- Ícone: City

**Botão 5 - Inversão:**
- Tipo: Button
- Texto: "🔄 Inversão"
- Ação: Bookmark → "InversaoGenero"
- Ícone: Refresh

---

## 🔧 Configurações de Página

### Todas as Páginas

**Tamanho:**
- Tipo: 16:9 (1280 x 720)
- OU: 4:3 (1024 x 768)

**Fundo:**
- Cor: #F5F5F5 (Cinza claro)
- OU: Branco

**Fontes:**
- Título: Segoe UI, 18pt, Bold
- Subtítulo: Segoe UI, 14pt, Regular
- Rótulos: Segoe UI, 10pt, Regular
- Valores: Segoe UI, 12pt, Bold

**Bordas:**
- Cor: #E0E0E0
- Espessura: 1pt

---

## 📊 Dicas Visuais

### 1. Contraste de Cores
- Usar cores fortes para valores importantes (vermelho #E74C3C)
- Usar cores suaves para contexto (cinza #95A5A6)
- Evitar usar rosa para feminino (estereótipo)

### 2. Hierarquia Visual
- Títulos grandes e em negrito (18-20pt)
- Subtítulos médios (14-16pt)
- Rótulos pequenos (10-12pt)

### 3. Espaçamento
- Padding: 8-16px entre elementos
- Margem: 16-24px nas bordas
- Alinhar elementos em grids

### 4. Consistência
- Usar mesmas cores em todos os painéis
- Mesmo estilo de fonte
- Mesmo padrão de layout

---

## 🚀 Próximos Passos

### 1. Criar o Arquivo .pbix
1. Abrir Power BI Desktop
2. Get Data → Text/CSV → Carregar todos os 7 arquivos
3. Criar os 5 painéis conforme instruções
4. Salvar como "Censo25_Dashboards.pbix"

### 2. Publicar no Power BI Service
1. Public → Workspace
2. Criar app "Censo Escolar 2025"
3. Compartilhar com stakeholders

### 3. Atualizações
- Atualizar CSVs quando houver novos dados
- Refresh no Power BI Service
- Agendar atualização automática (Pro license)

---

## 📞 Suporte

**Dúvidas sobre:**
- Modelagem de dados: Ver documentação oficial Power BI
- DAX: Usar Power BI Desktop -> Modeling -> New Measure
- Visualizações: Marketplace no Power BI

**Recursos:**
- Microsoft Learn: learn.microsoft.com/power-bi
- Comunidade: community.powerbi.com
- YouTube: Microsoft Power BI

---

**Autora:** Sara - Mestra em Educação
**Data:** 06 de março de 2026
**Versão:** 1.0

✨ **Boa criação de dashboards!** ✨
