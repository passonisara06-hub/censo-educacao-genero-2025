# 🚀 Início Rápido: Tableau Dashboard

## ⚡ Comece em 10 Minutos!

### Passo 1: Conectar aos Dados (2 min)

```
1. Abra Tableau Desktop
2. Connect → Text File
3. Selecione: outputs/tableau_dados_consolidados.csv
4. Open
```

### Passo 2: Entender a Estrutura (1 min)

**Arquivo: tableau_dados_consolidados.csv**

```
Categoria    | Subcategoria | Indicador    | Valor  | Unidade
-------------|--------------|--------------|--------|----------
Nacional     | Matrículas   | PctMeninas   | 49.4   | porcentagem
Federal      | Matrículas   | PctMeninas   | 51.1   | porcentagem
Sul          | Regional     | PctGestoras  | 85.8   | porcentagem
```

**4 Colunas Principais:**
- `Categoria` = Agrupamento (Nacional, Federal, Sul, etc.)
- `Subcategoria` = Tipo (Matrículas, Gestão, Regional, Localizacao)
- `Indicador` = Métrica (PctMeninas, PctGestoras, Total...)
- `Valor` = Número

### Passo 3: Criar Primeira Visualização (5 min)

**Sheet 1: Matrículas por Gênero**

```
1. Arraste Categoria para Filters → Marque "Nacional"
2. Arraste Indicador para Filters → Marque "PctMeninas", "PctMeninos"
3. Arraste Indicador para Columns
4. Arraste Valor para Rows
5. Mude para: Horizontal Bar Chart
6. Color: Edit Colors → PctMeninas = #E67E22, PctMeninos = #3498DB
7. Adicione título: "Matrículas por Gênero - Brasil"
```

**Pronto!** Você tem seu primeiro gráfico!

---

## 📊 Estrutura dos 5 Painéis Tableau

### 📍 Painel 1: Panorama Nacional

**Sheets:**
- Sheet 1: KPI Cards (4 cards grandes)
- Sheet 2: Matrículas por Gênero
- Sheet 3: Gestores por Gênero

**Criar KPI Cards:**
```
Card 1: Total Matrículas
- Filter: Indicador = "Total_Matriculas"
- Mark: Text
- Size: 24pt

Card 2: % Meninas
- Filter: Indicador = "PctMeninas"
- Mark: Circle
- Color: #E67E22
- Size: 32pt

Card 3: % Gestoras
- Filter: Indicador = "PctGestoras"
- Mark: Circle
- Color: #E74C3C
- Size: 32pt

Card 4: Índice (1.61x)
- Mark: Text
- Ou calculated field (ver guia completo)
- Color: #2ECC71
```

---

### 📍 Painel 2: Por Rede de Ensino

**Sheet 4: Meninas por Rede**
```
- Filter: Categoria IN ["Federal", "Estadual", "Municipal", "Privada"]
- Filter: Indicador = "PctMeninas"
- Type: Horizontal Bar Chart
- Color: #E67E22
- Sort: Descending
```

**Sheet 5: Gestoras por Rede**
```
- Filter: Categoria IN ["Federal", "Estadual", "Municipal", "Privada"]
- Filter: Indicador = "PctGestoras"
- Type: Stacked Bar (100%)
- Color: PctGestoras = #E74C3C, PctGestores = #3498DB
- Highlight: Federal (26.3%)
```

---

### 📍 Painel 3: Disparidades Regionais

**NECESSITA ARQUIVO ADICIONAL:**
```
Connect → Text File → tableau_por_uf.csv
```

**Sheet 6: Mapa do Brasil**
```
- Type: Map → Filled Map
- Location: UF
- Color: PctGestoras
- Size: NumEscolas
- Paleta: Diverging (Azul → Verde → Vermelho)
```

**Sheet 7: Barras por Região**
```
- Filter: Categoria = Regiões (Norte, Nordeste, etc.)
- Filter: Indicador = "PctGestoras"
- Type: Horizontal Bar
- Sort: Descending
- Color: #E74C3C
```

---

### 📍 Painel 4: Urbano vs Rural

**Sheet 8: Matrículas Urb/Rural**
```
- Filter: Categoria IN ["Urbana", "Rural"]
- Filter: Indicador = "PctMeninas"
- Type: Vertical Bar Chart
- Color: #E67E22
```

**Sheet 9: Gestoras Urb/Rural**
```
- Filter: Categoria IN ["Urbana", "Rural"]
- Filter: Indicador = "PctGestoras"
- Type: Vertical Bar Chart
- Color: #E74C3C
```

---

### 📍 Painel 5: Inversão de Gênero (Destaque)

**Sheet 10: Gráfico Principal**
```
- Filter: Indicador IN ["PctMeninas", "PctGestoras"]
- Type: Bar Chart
- Color: Por Indicador
- Reference Line: 50%
- Title: "A Inversão de Gênero na Educação Brasileira"
```

**Sheet 11: KPIs**
```
Card 1: Índice de Representação
- Valor: 1.61x
- Color de fundo: #E74C3C
- Texto: Branco

Card 2: Diferença
- Valor: +30.1 pp
- Color de fundo: #2ECC71

Card 3: Total Gestoras
- Valor: 151,610
- Color de fundo: #E74C3C
```

---

## 🎨 Paleta de Cores (Tableau)

### Copie e Cole estas cores:

**Edit Colors:**
```
#E67E22 → Laranja → Feminino
#3498DB → Azul → Masculino
#2ECC71 → Verde → Paridade
#E74C3C → Vermelho → Destaque
#95A5A6 → Cinza → Total
```

### Como usar no Tableau:

```
1. Marks → Color → Edit Colors
2. Clique em "Default"
3. Clique no botão "+" para adicionar cor
4. Coloque o código HEX (ex: #E67E22)
5. Repita para todas as cores
```

---

## 📋 Calculated Fields Principais

### Criar no Data Source:

**Índice de Representação:**
```
Nome: Indice Representacao
Formula:
{ FIXED [Indicador] = "PctGestoras" : AVG([Valor])} /
{ FIXED [Indicador] = "PctMeninas" : AVG([Valor])}
```

**Alerta Federal:**
```
Nome: Alerta Federal
Formula:
IF [Categoria] = "Federal" AND
   { FIXED [Categoria] = "Federal" : AVG([Valor])} < 30
THEN "⚠️ Teto de Vidro"
ELSE "✅ OK"
END
```

**Classificação Região:**
```
Nome: Classificacao Regiao
Formula:
IF AVG([Valor]) >= 85 THEN "Muito Alta"
ELSEIF AVG([Valor]) >= 75 THEN "Alta"
ELSEIF AVG([Valor]) >= 65 THEN "Média"
ELSE "Baixa" END
```

---

## 🔗 Hierarquias

### Criar Hierarquia:

```
Data Source Pane → Clique no ícone de hierarquia (h)

Hierarquia Geográfica:
├── Brasil
│   ├── Região (Norte, Nordeste, Sul, Sudeste, Centro-Oeste)
│   │   └── Estado (UF)
│   └── Rede de Ensino (Federal, Estadual, Municipal, Privada)
│       └── Localização (Urbana, Rural)
```

**Benefícios:**
- Drill-down automático
- Filtros em cascata
- Navegação intuitiva

---

## 💡 Formatação de Números

### Configurar Automaticamente:

**Porcentagens:**
```
1. Clique no campo Valor nas Dimensions ou Measures
2. Default Properties → Number Format
3. Percentage → 1 casa decimal
4. OK
```

**Números Grandes:**
```
1. Clique no campo Valor
2. Default Properties → Number Format
3. Number (Custom)
4. Separador de milhar: Sim
5. Decimal places: 0
6. OK
```

---

## 🎯 Dicas Rápidas

### Dica 1: Usar Sets (Conjuntos)

**Para destacar estados extremos:**
```
1. Clique com botão direito em PctGestoras
2. Create → Set
3. Nome: "Estudos com Alta Representação"
4. Condition: PctGestoras >= 80
5. OK

Usar para: Highlighting nos mapas
```

### Dica 2: Tooltips Personalizados

**Melhorar informações ao passar o mouse:**
```
1. Worksheet → Tooltip
2. Arrastar campos desejados
3. Edit Tooltip para formatar
4. Adicionar emojis e contexto
```

### Dica 3: Actions (Navegação)

**Ir de um painel para outro:**
```
1. Worksheet → Actions → Edit Actions
2. Add Action → Go to Sheet
3. Selecione: Run action on → Select
4. Target Sheet: Dashboard desejado
5. OK
```

### Dica 4: Storytelling

**Criar narrativa:**
```
1. New Story Point
2. Arraste Sheet/Dashboard
3. Adicione caption (descrição)
4. Repita para cada ponto da história
5. Play Story para ver
```

---

## 📱 Publicação

### Tableau Public (Grátis)

```
1. Server → Tableau Public
2. Criar conta (ou fazer login)
3. Publish Workbook
4. Copiar link
5. Compartilhar!
```

**Link ficará assim:**
```
https://public.tableau.com/profile/sara.censo25/#/publishhash
```

---

## ✅ Checklist de 10 Minutos

- [ ] Conectar tableau_dados_consolidados.csv
- [ ] Criar primeiro gráfico (barras horizontais)
- [ ] Aplicar cores customizadas
- [ ] Adicionar 4 KPI cards
- [ ] Criar primeiro Dashboard
- [ ] Testar interatividade
- [ ] Salvar Workbook (.twb)

---

## 🚀 Próximos 30 Minutos

- [ ] Criar mais 3 gráficos
- [ ] Criar Dashboard 2 (Por Rede)
- [ ] Adicionar filtros
- [ ] Testar drill-down

---

## 🎓 1 Hora Completa

- [ ] Criar todas as planilhas (10+ sheets)
- [ ] Criar 5 dashboards
- [ ] Criar Story
- [ ] Publicar no Tableau Public

---

## 🔧 Problemas Comuns

**Problema: Mapa não aparece**
```
Solução: Verificar nomes das UFs
- Devem ser siglas de 2 letras (SP, RJ, MG, etc.)
- Arquivo tableau_por_uf.csv já está pronto
```

**Problema: Calculated Field com erro**
```
Solução: Verificar sintaxe
- Parenteses balanceados
- Nomes de campos entre colchetes [Campo]
- FIXED usage correto (ver guia completo)
```

**Problema: Cores ficam escuras**
```
Solução: Edit Colors → Custom
- Usar códigos HEX fornecidos
- Ou paleta "Tableau 20" (já vem com Tableau)
```

---

## 📚 Recursos Rápidos

**Tableau Public Gallery:**
- gallery.tableau.com
- Veja exemplos inspiradores!

**YouTube:**
- "Tableau Software" canal oficial
- Busque: "Tableau for beginners"

**Comunidade:**
- community.tableau.com
- Poste dúvidas, comunidade ajuda!

---

## ⏱️ Tempos Estimados

```
Primeiro gráfico:       5 minutos
KPIs:                  5 minutos
Primeiro Dashboard:    10 minutos
Todos os Dashboards:    2-3 horas
Story completa:        30 minutos
Publicação:            5 minutos
```

---

**Você vai adorar o Tableau!** 🎨

A visualização é intuitiva, bonita e muito fácil de criar interatividade!

**Próximo passo:** Abra o Tableau e carregue o arquivo `tableau_dados_consolidados.csv`!

---

**Autora:** Sara - Mestra em Educação
**Data:** 06 de março de 2026
**Versão:** 1.0
