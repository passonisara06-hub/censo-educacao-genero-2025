# 📊 Guia Completo: Dashboards Tableau - Censo Escolar 2025

**Autora:** Sara - Mestra em Educação
**Data:** 06 de março de 2026
**Plataforma:** Tableau Desktop / Tableau Public
**Objetivo:** Criar 5 painéis interativos no Tableau

---

## 📋 Arquivos para Tableau

```
outputs/
├── tableau_dados_consolidados.csv    ← DADOS PRINCIPAIS (use este!)
├── tableau_por_uf.csv                ← Para mapa do Brasil
└── tableau_escolas_amostra.csv       ← Para drill-down (opcional)
```

**DICA:** Comece com `tableau_dados_consolidados.csv` - ele contém tudo o que você precisa!

---

## 🎯 Estrutura dos Dados (Tableau)

### Formato "Tidy" (Organizado)

O arquivo principal `tableau_dados_consolidados.csv` tem 4 colunas:

```
Categoria      | Subcategoria  | Indicador      | Valor  | Unidade      | Contexto
---------------|---------------|----------------|--------|--------------|----------
Nacional       | Matrículas    | Total_Matri... | 46M    | quantidade   | Brasil
Nacional       | Matrículas    | PctMeninas     | 49.4   | porcentagem  | Brasil
Federal        | Matriculas    | PctMeninas     | 51.1   | porcentagem  | Brasil
Sul            | Regional      | PctGestoras    | 85.8   | porcentagem  | Brasil
Urbana         | Localizacao   | PctMeninas     | 49.5   | porcentagem  | Brasil
```

**Vantagens deste formato:**
- ✅ Formato "long" (Tableau prefere)
- ✅ Fácil de fazer pivôs
- ✅ Permite filtros dinâmicos
- ✅ Hierarquias naturais

---

## 🚀 Início Rápido (10 Minutos)

### Passo 1: Conectar aos Dados

1. **Abrir Tableau Desktop**
2. **Text File Connection:**
   - Connect → To a File → Text File
   - Selecionar: `outputs/tableau_dados_consolidados.csv`
   - Open

3. **Configurar Conexão:**
   - Delimiter: Automatic (detecta vírgula)
   - Text Qualifier: None (ou " se necessário)
   - Sheet1: Renomear para "DadosCenso"

### Passo 2: Limpeza Inicial

**No Data Source:**
1. Mudar tipos de dados:
   - `Valor` → Number (Decimal)
   - `Unidade` → String
   - `Categoria`, `Subcategoria`, `Indicador` → String

2. Limpar nomes das colunas (se necessário):
   - Clique no ícone de lápis ao lado do nome da coluna
   - Renomear para nomes sem espaços

### Passo 3: Criar Primeira Planilha (Sheet 1)

**Painel 1: Panorama Nacional**

1. **Criar Gráfico de Barras - Matrículas:**
   - Drag `Categoria` para Filters → Marque "Nacional"
   - Drag `Indicador` para Filters → Marque "PctMeninas", "PctMeninos"
   - Drag `Indicador` para Columns
   - Drag `Valor` para Rows
   - Mostra Me: Card ou Automatic

2. **Formatar:**
   - Color: Marks → Color → Edit Colors
     - PctMeninas: #E67E22 (Laranja)
     - PctMeninos: #3498DB (Azul)
   - Labels: Show Mark Labels → Format → Number → Percentage
   - Título: "Distribuição de Gênero - Matrículas"

---

## 📌 PAINEL 1: Panorama Nacional (Visão Executiva)

### Objetivo
Visão executiva dos principais indicadores de gênero.

### Planilhas (Sheets) Criar

#### Sheet 1: KPI Cards

**4 Big Number Cards:**

1. **Total Matrículas:**
   - Filter: Indicador = "Total_Matriculas"
   - Mark Type: Automatic → Text
   - Edit Tooltip: "Total de matrículas na educação básica brasileira"
   - Size: 24pt, Bold

2. **% Meninas:**
   - Filter: Indicador = "PctMeninas"
   - Mark Type: Circle
   - Color: #E67E22
   - Label: Show Mark Labels
   - Size: 32pt

3. **% Gestoras:**
   - Filter: Indicador = "PctGestoras"
   - Mark Type: Circle
   - Color: #E74C3C (Vermelho destaque)
   - Label: Show Mark Labels
   - Size: 32pt

4. **Índice de Representação:**
   - Criar Calculated Field:
   ```
   Nome: Indice de Representacao
   Formula:
   { FIXED : SUM([Valor])} / {FIXED [Indicador] = [PctGestoras]} :
   SUM([Valor])} / {FIXED [Indicador] = [PctMeninas] : SUM([Valor])}
   ```
   - OU criar manualmente: 79.5 / 49.4 = 1.61

#### Sheet 2: Gráfico Comparativo

**Matrículas por Gênero:**
- Type: Bar Chart
- Columns: Indicador (PctMeninas, PctMeninos)
- Rows: Valor
- Color: By Indicador (#E67E22, #3498DB)
- Label: Percentagem

**Gestores por Gênero:**
- Type: Bar Chart
- Columns: Indicador (PctGestoras, PctGestores)
- Rows: Valor
- Color: By Indicador (#E74C3C, #3498DB)
- Label: Percentagem

### Dashboard 1

**Layout:**
- Arranjar os 4 KPI cards no topo
- Colocar os 2 gráficos lado a lado abaixo
- Adicionar título: "Panorama Nacional - Censo Escolar 2025"

**Filtros:**
- Adicionar Filter: Categoria = "Nacional"

---

## 📌 PAINEL 2: Análise por Rede de Ensino

### Objetivo
Comparar distribuição de gênero por rede (Federal, Estadual, Municipal, Privada).

### Planilhas Criar

#### Sheet 3: Meninas por Rede

**Gráfico:**
- Type: Horizontal Bar Chart
- Rows: Categoria (Federal, Estadual, Municipal, Privada)
- Columns: SUM([Valor]) filtrado por Indicador = "PctMeninas"
- Color: #E67E22
- Sort: Descending by Valor

**Destaques:**
- Data Highlight (Federal: 51.1% - maior %)

#### Sheet 4: Gestoras por Rede

**Gráfico:**
- Type: Stacked Bar Chart (100%)
- Columns: Categoria (Rede de Ensino)
- Rows: SUM([Valor]) para PctGestoras e PctGestores
- Color: By Measure
  - PctGestoras: #E74C3C (Vermelho)
  - PctGestores: #3498DB (Azul)
- Label: Percentagem

**Destaques:**
- Annotations: Federal = 26.3% (alerta!)
- Title Annotation: "⚠️ Federal: Apenas 26.3% Gestoras"

#### Sheet 5: Tabela Detalhada por Rede

**Tabela:**
- Rows: Categoria
- Columns:
  - SUM([Valor]) where Indicador = "PctMeninas"
  - SUM([Valor]) where Indicador = "PctGestoras"
  - SUM([Valor]) where Indicador = "TotalEscolas"

**Conditional Formatting:**
- PctGestoras < 30: Background #FFF3E6 (Amarelo claro)
- PctGestoras >= 80: Background #E8F8F5 (Verde claro)

### Dashboard 2

**Layout:**
- Topo: Gráfico Meninas por Rede
- Meio: Gráfico Gestoras por Rede
- Fundo: Tabela Detalhada

**Interatividade:**
- Filter: Use as 4 redes como filtro para todas as planilhas

---

## 📌 PAINEL 3: Disparidades Regionais

### Objetivo
Visualizar distribuição de gestoras por região e estados.

### Conectar Arquivo Adicional

```
Connect → Text File → tableau_por_uf.csv
```

**Campos disponíveis:**
- UF (sigla)
- Estado
- Regiao
- PctMeninas, PctMeninos
- PctGestoras, PctGestores
- TotalMatriculas, TotalGestores
- NumEscolas

### Planilhas Criar

#### Sheet 6: Mapa do Brasil

**Mapa Coroplético:**
- Type: Map → Filled Map
- Marks:
  - Location: UF
  - Color: AVG([PctGestoras])
  - Size: NumEscolas

**Paleta de Cores:**
- 60-70%: #3498DB (Azul)
- 70-80%: #2ECC71 (Verde)
- 80-85%: #E67E22 (Laranja)
- 85-90%: #E74C3C (Vermelho)

**Destaques:**
- Labels: Mostrar sigla UF + porcentagem
- Tooltip: Regiao, Estado, PctGestoras, NumEscolas

#### Sheet 7: Barras por Região

**Gráfico:**
- Type: Horizontal Bar Chart
- Rows: Regiao (filtrado de tabela consolidada)
- Columns: AVG([PctGestoras])
- Color: #E74C3C
- Sort: Descending by PctGestoras

**KPIs:**
- 3 Big Number Cards:
  - Máximo: "Sul 85.8%"
  - Mínimo: "Norte 63.9%"
  - Variação: "21.9 pp"

### Dashboard 3

**Layout:**
- Esquerda: Mapa do Brasil (ocupando 60%)
- Direita: Barras por região + KPIs
- Title: "Disparidades Regionais - % de Gestoras"

**Filtros:**
- Filter: Regiao (para map e barras)
- Filter: Range slider para PctGestoras

---

## 📌 PAINEL 4: Urbano vs Rural

### Objetivo
Comparar indicadores de gênero entre áreas urbanas e rurais.

### Planilhas Criar

#### Sheet 8: Matrículas Urbano vs Rural

**Gráfico:**
- Type: Grouped Bar Chart (Vertical)
- Columns: Categoria (Urbana, Rural)
- Rows: AVG([Valor]) where Indicador = "PctMeninas"
- Color: #E67E22
- Label: Percentagem

#### Sheet 9: Gestoras Urbano vs Rural

**Gráfico:**
- Type: Grouped Bar Chart (Vertical)
- Columns: Categoria (Urbana, Rural)
- Rows: AVG([Valor]) where Indicador = "PctGestoras"
- Color: #E74C3C
- Label: Percentagem

**Difference Bars:**
- Criar Calculated Field para diferença:
```
Nome: Dif Urbano Rural
Formula:
AVG(IF [Categoria] = 'Urbana' THEN [Valor] END) -
AVG(IF [Categoria] = 'Rural' THEN [Valor] END)
```

#### Sheet 10: Tabela Comparativa

**Tabela:**
- Rows: Categoria
- Columns: Metric (Matrículas, Gestão)
- Values: PctMeninas, PctGestoras

**Conditional Formatting:**
- Diferença de cor para Urbana vs Rural

### Dashboard 4

**Layout:**
- Topo: Gráfico Matrículas | Gráfico Gestoras
- Fundo: Tabela comparativa
- Title: "Urbano vs Rural - Disparidades de Gênero"

**Filtros:**
- Filter: Subcategoria = "Localizacao"

---

## 📌 PAINEL 5: A Inversão de Gênero (Destaque)

### Objetivo
Destacar a principal descoberta do estudo.

### Planilhas Criar

#### Sheet 11: Gráfico Principal - Inversão

**Gráfico de Barras:**
- Type: Bar Chart
- Data: Dados Consolidados filtrados:
  - (Indicador = "PctMeninas" AND Subcategoria = "Matriculas")
  - (Indicador = "PctGestoras" AND Subcategoria = "Gestao")
- Columns: Calculated Field "Tipo_Grafico"
- Rows: Valor
- Color: By Tipo_Grafico

**Criar Calculated Field:**
```
Nome: Tipo_Grafico
Formula:
CASE [Indicador]
  WHEN 'PctMeninas' THEN 'Meninas (Sala de Aula)'
  WHEN 'PctGestoras' THEN 'Gestoras (Gestão Escolar)'
END
```

**Cores:**
- Meninas (Sala de Aula): #E67E22
- Gestoras (Gestão Escolar): #E74C3C

**Reference Line:**
- Add Reference Line: Constant = 50%
- Label: "Paridade"
- Line: Dashed, Color #2ECC71

#### Sheet 12: KPIs Principais

**3 Cards Grandes:**

1. **Índice de Representação:**
   - Criar Calculated Field:
   ```
   Nome: Indice Rep Calculado
   Formula: 79.5 / 49.4
   Result: 1.61
   ```
   - Display como Big Number
   - Cor de fundo: #E74C3C
   - Texto: Branco, Bold

2. **Diferença Absoluta:**
   - Display: "+30.1 pp"
   - Cor de fundo: #2ECC71
   - Texto: Branco, Bold

3. **Total Gestoras:**
   - Filter: Indicador = "Gestoras"
   - Display: 151,610
   - Cor de fundo: #E74C3C
   - Texto: Branco, Bold

#### Sheet 13: Texto Informativo

**Create Worksheet:**
- Type: Text
- Adicionar texto:
```
🔍 DESCOBERTA CHAVE

Contrariando a narrativa do "teto de vidro",
as mulheres são MAIORIA na gestão escolar
brasileira.

79.5% dos gestores são mulheres vs 49.4%
das alunas são meninas.

Índice de Representação: 1.61x
```

### Dashboard 5

**Layout:**
- Topo: 3 KPI Cards (Índice, Diferença, Total)
- Centro: Gráfico Principal grande
- Fundo: Texto Informativo
- Title: "A INVERSÃO DE GÊNERO na Educação Brasileira"

**Action:**
- Adicionar botões ou filtros para interatividade

---

## 🎨 Calculated Fields (Cópia e Cola)

### No Data Source ou Worksheet

```tableau
// ========== INDICADORES PRINCIPAIS ==========

[1. Total Matrículas]
{ FIXED [Indicador] = "Total_Matriculas" : SUM([Valor])}

[2. % Meninas]
{ FIXED [Indicador] = "PctMeninas" : SUM([Valor])}

[3. % Gestoras]
{ FIXED [Indicador] = "PctGestoras" : SUM([Valor])}

[4. Índice de Representação]
[% Gestoras] / [% Meninas]

// ========== FILTROS ==========

[5. Apenas Nacional]
[Categoria] = "Nacional"

[6. Apenas Redes de Ensino]
[Categoria] IN ["Federal", "Estadual", "Municipal", "Privada"]

[7. Apenas Regiões]
[Categoria] IN ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

[8. Apenas Localização]
[Categoria] IN ["Urbana", "Rural"]

// ========== ANÁLISES ==========

[9. Diferença Gestoras Meninas]
([% Gestoras] - [% Meninas])

[10. Alerta Federal]
IF [Categoria] = "Federal" AND [Pct_Gestoras] < 30 THEN "⚠️ Teto de Vidro"
ELSEIF [PctGestoras] >= 80 THEN "✅ Alta Representação"
ELSE "➖ Média Representação" END

[11. Classificação Região]
IF [PctGestoras] >= 85 THEN "Muito Alta"
ELSEIF [PctGestoras] >= 75 THEN "Alta"
ELSEIF [PctGestoras] >= 65 THEN "Média"
ELSE "Baixa" END

// ========== VISUALIZAÇÕES ==========

[12. Cor por Gênero]
IF [Indicador] = "PctMeninas" OR [Indicador] = "Gestoras" THEN "#E74C3C"
ELSEIF [Indicador] = "PctMeninos" OR [Indicador] = "PctGestores" THEN "#3498DB"
ELSE "#95A5A6" END

[13. Tamanho por Valor]
ABS([Valor]) / {MAX([Valor])} * 100
```

---

## 🎨 Paleta de Cores no Tableau

### Criar Paleta Customizada

**Tableau Desktop:**
1. Marks → Color → Edit Colors
2. Clique em "Default" → Adicionar cores:

```
#E67E22 → Laranja (Feminino)
#3498DB → Azul (Masculino)
#2ECC71 → Verde (Paridade)
#E74C3C → Vermelho (Destaque)
#95A5A6 → Cinza (Total)
#F39C12 → Laranja Escuro
#8E44AD → Roxo (Secundário)
#27AE60 → Verde Escuro
#2980B9 → Azul Escuro
#C0392B → Vermelho Escuro
```

### Salvar como Preferência

**Tableau Desktop:**
- Book → Format → Workbook
- Salvar preferências

**Tableau Public:**
- Cores são salvas automaticamente

---

## 🔗 Hierarquias (Tableau)

### Criar Hierarquia Geográfica

**Data Source Pane:**
1. Clique no ícone de hierarquia (hierarquia)
2. Arrastar campos:
   - **Nível 1:** Contexto (Brasil)
   - **Nível 2:** Regiao (Norte, Nordeste, etc.)
   - **Nível 3:** Categoria (UF)
   - **Nível 4:** Subcategoria

**Benefícios:**
- Drill-down automático
- Filtros em cascata
- Navegação fácil

---

## 📊 Tooltips Personalizados

### Adicionar Contexto aos Tooltips

**Edit Tooltip:**
```
Indicador: <Indicador>
Valor: <Valor>%
Total: <Total de Escolas>

💡 Clique para ver detalhes por rede/estado
```

**Formatação:**
- Incluir campos calculados
- Adicionar contexto
- Emojis para destaque

---

## 🎯 Sets (Conjuntos)

### Criar Sets para Análises

**Set 1: Estados com Baixa Representação**
```
Field: PctGestoras
Condition: < 70
States: Norte, alguns estados específicos
```

**Set 2: Estados com Alta Representação**
```
Field: PctGestoras
Condition: >= 80
States: Sul, Sudeste
```

**Uso:**
- Highlighting no mapa
- Filtros dinâmicos
- Análises comparativas

---

## 🚀 Storytelling no Tableau

### Criar Story (História)

**Tableau Desktop:**
1. New Story Point
2. Arrancar sheets ou dashboards
3. Adicionar descrição (caption)

**Estrutura da Story:**

**Ponto 1 - Panorama Nacional:**
- Sheet: Dashboard 1
- Caption: "Brasil tem 46 milhões de matrículas na educação básica, com quase paridade de gênero (49.4% meninas vs 50.6% meninos)"

**Ponto 2 - Gestão Escolar:**
- Sheet: Dashboard 1 zoom em gestão
- Caption: "Mulheres são 79.5% dos gestores escolares - um inversão da proporção nas salas de aula"

**Ponto 3 - Exceção Federal:**
- Sheet: Dashboard 2 focado na Federal
- Caption: "A rede Federal apresenta apenas 26.3% de gestoras, sugerindo possível teto de vidro em contextos de maior prestígio"

**Ponto 4 - Disparidades Regionais:**
- Sheet: Dashboard 3 (mapa)
- Caption: "A região Sul tem a maior proporção de gestoras (85.8%), enquanto o Norte tem a menor (63.9%)"

**Ponto 5 - Conclusão:**
- Sheet: Dashboard 5 (Inversão de Gênero)
- Caption: "A educação brasileira apresenta uma inversão de gênero única: mulheres dominam a gestão escolar, contrariando narrativas tradicionais de teto de vidro"

---

## 📱 Publicação e Compartilhamento

### Tableau Public (Grátis)

**Passos:**
1. Server → Tableau Public
2. Criar conta gratuita (profile)
3. Publish Workbook
4. Copiar link

**Limitações Grátis:**
- Até 10GB de dados
- Até 1 workbook por vez
- Sem atualização automática

### Tableau Online (Paid)

**Recursos adicionais:**
- Atualização automática
- Mais workbooks
- Colaboração em tempo real

---

## 💡 Dicas de Ouro para Tableau

### 1. Performance

**Usar Data Extract:**
- Ao invés de Live connection
- Melhora performance
- Permite filtros rápidos

**Amostragem:**
- Se dataset for muito grande, usar amostra
- Arquivo `tableau_escolas_amostra.csv` já está pronto

### 2. Visualização

**Menos é Mais:**
- Não sobrecarregar com informações
- Usar whitespace eficientemente
- Destacar apenas o importante

**Consistência:**
- Mesmas cores em todas as views
- Mesmos tipos de gráficos para comparações
- Mesma escala para dados comparáveis

### 3. Interatividade

**Filtros:**
- Show Filter
- Ativar "Only Relevant Values"
- Usar filtros em cascata (hierarquia)

**Actions:**
- Menu → Actions → Edit Actions
- Ir para outra sheet/dashboard
- URL actions para links externos

**Highlighting:**
- Menu → Actions → Highlight
- Selecionar item para destacar
- Útil para comparações

---

## 🔧 Troubleshooting

### Problema: Mapa do Brasil não aparece

**Solução:**
- Verificar se os nomes das UFs estão corretos (siglas de 2 letras)
- Usar arquivo `tableau_por_uf.csv` que tem UF e Regiao

### Problema: Cores não ficam bonitas

**Solução:**
- Edit Colors → Custom
- Usar paleta fornecida
- Verificar se o tipo de dado está correto

### Problema: Calculated Field dá erro

**Solução:**
- Verificar sintaxe (parentheses, FIXED)
- Verificar se os campos existem
- Testar com valores simples primeiro

---

## 📊 Checklist de Implementação

### ✅ Conexão de Dados
- [ ] Carregar tableau_dados_consolidados.csv
- [ ] Carregar tableau_por_uf.csv (opcional)
- [ ] Definir tipos de dados corretos
- [ ] Criar hierarquias

### ✅ Planilhas (Sheets)
- [ ] Sheet 1: KPI Cards Nacionais
- [ ] Sheet 2: Gráfico Comparativo
- [ ] Sheet 3: Meninas por Rede
- [ ] Sheet 4: Gestoras por Rede
- [ ] Sheet 5: Tabela Detalhada Rede
- [ ] Sheet 6: Mapa Brasil
- [ ] Sheet 7: Barras Região
- [ ] Sheet 8: Matrículas Urb/Rural
- [ ] Sheet 9: Gestoras Urb/Rural
- [ ] Sheet 10: Tabela Comparativa
- [ ] Sheet 11: Gráfico Inversão
- [ ] Sheet 12: KPIs Principais
- [ ] Sheet 13: Texto Informativo

### ✅ Dashboards
- [ ] Dashboard 1: Panorama Nacional
- [ ] Dashboard 2: Por Rede de Ensino
- [ ] Dashboard 3: Disparidades Regionais
- [ ] Dashboard 4: Urbano vs Rural
- [ ] Dashboard 5: Inversão de Gênero

### ✅ Story
- [ ] Criar Story Point 1
- [ ] Criar Story Point 2
- [ ] Criar Story Point 3
- [ ] Criar Story Point 4
- [ ] Criar Story Point 5

### ✅ Finalização
- [ ] Revisar todas as visualizações
- [ ] Testar interatividade
- [ ] Adicionar tooltips personalizados
- [ ] Publicar no Tableau Public

---

## 🎯 Diferenças Tableau vs Power BI

| Aspecto | Tableau | Power BI |
|---------|---------|-----------|
| Curva de aprendizado | Mais fácil | Mais íngreme |
| Visualizações | Mais flexíveis | Mais padrão |
| Linguagem de cálculo | Simples | DAX complexa |
| Preço | Gratuito (Public) | Free + Pro |
| Compartilhamento | Tableau Public/Online | Power BI Service |
| Mapas | Melhor | Precisa complementos |
| Dashboards | Mais intuitivos | Mais configuráveis |

**Recomendação:** Tableau é excelente para análise exploratória e visualizações bonitas!

---

## 📚 Recursos Tableau

**Documentação Oficial:**
- help.tableau.com
- tableau.com/learn

**Comunidade:**
- community.tableau.com
- vizypoetry.tumblr.com

**Tutoriais:**
- YouTube: "Tableau Software"
- Tableau Public Gallery (gallery.tableau.com)

---

## ⏱️ Tempo Estimado

- Conexão de dados: 10 minutos
- Criar 5 dashboards: 2-3 horas
- Story: 30 minutos
- Revisão final: 30 minutos

**TOTAL: 3-4 horas**

---

**Autora:** Sara - Mestra em Educação
**Data:** 06 de março de 2026
**Versão:** 1.0

✨ **Aproveite a visualização bonita e intuitiva do Tableau!** ✨
