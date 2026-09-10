# 📊 Relatório de Síntese: Desigualdades de Gênero na Educação Básica Brasileira

**Data:** Setembro de 2026 (v2.3)
**Autora:** Sara - Mestra em Educação
**Fonte:** Censo Escolar 2025 - INEP

---

## 🎯 Resumo Executivo

Esta análise investigou as disparidades de gênero na educação básica brasileira usando os microdados do Censo Escolar 2025, abrangendo **180.540 escolas ativas**, **46.018.380 matrículas** e, na v2.1, **2.992.045 docentes**.

### 📊 Principais Métricas Nacionais

| Indicador | Valor |
|-----------|-------|
| Total de matrículas | 46.018.380 |
| % Meninas | 49.4% |
| % Meninos | 50.6% |
| Total de docentes | 2.992.045 |
| % Docentes mulheres | **75.8%** |
| Total de gestores | 190.641 |
| % Gestoras | **79.5%** |
| **IFR (gestão ÷ docência)** | **1.05x** |

---

## 🔍 Descobertas Principais

### 1. **Paridade de Gênero nas Salas de Aula** ✅

A educação básica brasileira apresenta **praticamente paridade de gênero**:
- Meninas: 49.4%
- Meninos: 50.6%
- Diferença: apenas 0.6 pontos percentuais

**Teste Estatístico (Qui-quadrado):**
- A diferença é estatisticamente significativa (p < 0.001)
- No entanto, a magnitude é pequena (< 1%), limitando sua relevância prática para políticas públicas

**Implicação:** Não há necessidade urgente de políticas públicas para corrigir disparidades de gênero no acesso à educação básica.

---

### 2. **Docência × Gestão: o Índice de Feminização Relativa (IFR)** 🔄

**Reenquadramento metodológico (v2.1):**

O comparativo correto para a gestão não é o alunado — é a **docência**, profissão da qual
a gestão recruta. A tabela de docentes do Censo (agora integrada à análise) permite o
**Índice de Feminização Relativa**:

$$\text{IFR} = \frac{\%\ \text{mulheres na gestão}}{\%\ \text{mulheres na docência}}$$

| Rede | % docentes mulheres | % gestoras | IFR |
|------|--------------------:|-----------:|----:|
| **Brasil** | 75.8% | 79.5% | **1.05** |
| Privada | 76.2% | 83.9% | 1.10 |
| Estadual | 63.7% | 65.6% | 1.03 |
| Municipal | 83.0% | 82.1% | 0.99 |
| **Federal** | **40.3%** | **26.3%** | **0.65** |

**Leitura revisada:** a gestão escolar brasileira **espelha a feminização da docência**
(IFR 1.05). O antigo "Índice de Representação 1.61x" comparava % gestoras com % de
**alunas** (49.4%) — base errada, pois os(as) alunos(as) de hoje não são o banco de
candidatas à gestão. O teto de vidro clássico (docência feminina → gestão masculina)
**não aparece no agregado nacional**.

**A exceção Federal, relida:** a rede Federal é a **única do país com docência
majoritariamente masculina** (40.3% mulheres — institutos federais, áreas técnicas/STEM,
docente do ensino superior compartilhado). Sua gestão (26.3%, n=754) é **proporcional à
base docente da qual recruta** (IFR 0.65). A pergunta de pesquisa muda: não "por que
mulheres não ascendem na Federal", mas **"por que a docência federal é majoritariamente
masculina?"** — contratação, áreas de concurso, composição das carreiras.

**Caso mais forte de barreira real: Amazonas (IFR 0.80)** — gestão feminina (49.7%) muito
abaixo da própria docência estadual (62.3%). Candidato a estudo de caso qualitativo.
No topo, PB (1.16), RJ (1.15), PE (1.14): gestão acima da docência.

**Implicação para políticas:** a recomendação de "auditoria por teto de vidro na Federal"
evolui para **investigar a composição do docentado federal** (recrutamento, áreas,
trajetórias) — a barreira, se existir, está na base da carreira, não só no topo.

---

### 3. **A Exceção Federal: Base Docente, Não Teto de Promoção** ⚠️

Embora as mulheres dominem a gestão escolar em números absolutos, a análise por rede de ensino revela um padrão importante:

| Rede de Ensino | % Gestoras | % Docentes mulheres | IFR | Interpretação |
|----------------|------------|--------------------:|----:|---------------|
| **Privada** | 83.9% | 76.2% | 1.10 | Gestão acima da docência |
| **Municipal** | 82.1% | 83.0% | 0.99 | Espelha a docência |
| **Estadual** | 65.6% | 63.7% | 1.03 | Gestão acima da docência |
| **Federal** | **26.3%** | **40.3%** | **0.65** ⚠️ | Gestão proporcional à base |

**Reflexão Crítica (v2.1):**

A baixa presença de gestoras na rede Federal (26.3%) não pode ser lida isoladamente: a
**docência federal é a única do país majoritariamente masculina** (40.3% mulheres). Com
apenas 754 gestores federais (0.4% do total), o padrão federal reflete principalmente a
**composição da base docente** — não um mecanismo de promoção distinto.

**Perguntas para investigação futura (atualizadas):**
- Por que a docência federal é majoritariamente masculina? (áreas de concurso, STEM, docente do superior compartilhado)
- O IFR federal persiste quando controlado por tipo de instituição (IF vs CEFET vs colégios)?
- Por que o Amazonas tem IFR 0.80 — gestão (49.7%) muito abaixo da docência estadual (62.3%)?
- Como o IFR varia com recorte racial (dados disponíveis)?
- Gestoras têm os mesmos salários que gestores?

---

### 4. **Análise de Correlação (atualizada em v2.3)** 📈

**Correlação entre porte da escola e % de gestoras:** a versão original reportava
"não significativa" correlacionando porcentagens escolares brutas — método viciado por
escolas com 1 gestor (0% ou 100%). A análise **ponderada por número de gestores** (v2.3)
revela relação em **U invertido**: % gestoras maior no porte médio (Q2: 84.9%) e menor
nos extremos (Q1: 78.0%; Q4: 72.9%). Ver seção "Rigor Estatístico".

---

## 📊 Disparidades Regionais

### Distribuição de Meninas por Região

| Região | % Meninas | Classificação |
|--------|-----------|---------------|
| Sudeste | 49.5% | Maior presença feminina |
| Nordeste | 49.4% | Próximo à média |
| Centro-Oeste | 49.3% | Próximo à média |
| Sul | 49.3% | Próximo à média |
| Norte | 49.3% | Menor presença feminina |

**Variação regional:** Apenas 0.3 pontos percentuais

**Implicação:** Não há disparidades regionais significativas na presença de meninas na educação básica.

---

### Distribuição de Gestoras por Região

| Região | % Gestoras | Classificação |
|--------|------------|---------------|
| **Sul** | **85.8%** | Maior presença feminina |
| Sudeste | 83.5% | Acima da média |
| Nordeste | 78.5% | Próximo à média |
| Centro-Oeste | 77.2% | Abaixo da média |
| Norte | 63.9% | Menor presença feminina |

**Variação regional:** 21.9 pontos percentuais

**Implicação:** Há disparidades regionais expressivas na gestão escolar, com a região Norte apresentando uma proporção de gestoras significativamente menor.

---

## 🏫 Disparidades por Rede de Ensino

### Matrículas por Rede

| Rede | % Meninas | Interpretação |
|------|-----------|---------------|
| Federal | 51.1% | Maior presença feminina |
| Privada | 50.6% | Leve maioria feminina |
| Estadual | 49.9% | Quase paridade |
| Municipal | 48.6% | Leve maioria masculina |

### Gestoras por Rede

| Rede | % Gestoras | Interpretação |
|------|------------|---------------|
| Privada | 83.9% | Dominância feminina |
| Municipal | 82.1% | Dominância feminina |
| Estadual | 65.6% | Maioria feminina |
| Federal | **26.3%** | **MINORIA feminina** ⚠️ |

---

## 🌐 Urbano vs Rural

### Matrículas

| Localização | % Meninas | Diferença |
|-------------|-----------|-----------|
| Urbana | 49.5% | +1.2 pp |
| Rural | 48.3% | -1.2 pp |

**Implicação:** Diferença pequena (1.2 pp), sem grande relevância prática.

### Gestoras

| Localização | % Gestoras | Diferença |
|-------------|------------|-----------|
| Urbana | 82.6% | +11.2 pp |
| Rural | 71.4% | -11.2 pp |

**Implicação:** Diferença moderada (11.2 pp), sugerindo que áreas urbanas têm maior presença de gestoras.

---

## ⚖️ Interseccionalidade: Raça/cor (v2.2)

> ⚠️ **Limitação estrutural:** os agregados do INEP **não cruzam raça × gênero** — as
> distribuições abaixo são marginais (% de quem declarou raça/cor em cada posição).

### Composição racial: quem aprende, quem ensina, quem dirige

| Categoria | Branca | Preta | Parda | Amarela | Indígena | ND |
|-----------|-------:|------:|------:|--------:|---------:|---:|
| Alunado | 40.4% | 5.8% | 52.5% | 0.4% | 1.0% | 13.6% |
| Docentes | 52.9% | 7.2% | 37.9% | 1.0% | 1.0% | 17.6% |
| Gestores | 52.4% | 6.7% | 38.9% | 0.8% | 1.3% | 15.8% |

**Leitura:** o "filtro racial" do sistema educacional está na **entrada na docência**:
pardos são **52.5% do alunado mas 37.9% da docência** (−14.6 pp); brancos, 40.4% do
alunado mas **52.9% da docência** (+12.5 pp). Da docência à gestão a composição fica
estável (razões de presença 0.92–1.37, próximas de 1): **a gestão espelha a raça da
docência**, assim como espelha o gênero (IFR 1.05).

### Por rede

- **Privada embranquece no topo:** docência 60.4% branca → gestão 65.5% branca.
- **Municipal** (maior rede do país): a mais negra (docência 47.7% branca, 42.7% parda)
  e a mais feminina — onde a maior parte das docentes e gestoras negras e pardas está.
- **Estadual:** única com gestoras indígenas acima da docência (3.4% vs 1.7%).

---

## 🗺️ IFR Municipal: onde a gestão descola da base (v2.2)

IFR calculado para **5.571 municípios** (extremos com filtro n_gestores ≥ 20);
mediana municipal: **1.06**.

| Faixa de IFR | Municípios |
|---|---:|
| < 0.90 (gestão abaixo da base) | 1.080 |
| 0.90–1.10 (proporcional) | 2.205 |
| > 1.10 (gestão acima da base) | 2.286 |
| **Gestoras minoria (<50%)** | **224** |

**Casos extremos (n ≥ 20):** Maraã-AM tem **IFR 0.11** — docência de 63.1% mulheres e
apenas **6.9% de gestoras**; seguem Lábrea-AM (0.16), Feijó-AC (0.19), Ladainha-MG (0.19).
No topo, Santa Isabel do Rio Negro-AM (2.34) e Atalaia do Norte-AM (2.01) — gestão quase
totalmente feminina sobre docências femininas de ~45%.

**Concentração territorial:** o Amazonas tem **54.8% dos municípios com gestoras em
minoria** (<50%) — seguido por AC (31.8%), RR (20.0%) e AP (18.8%). A sub-representação
municipal é um problema **norte-amazônico**, coerente com o IFR estadual do AM (0.80).

---

## 💡 Recomendações de Políticas Públicas

### 1. **Manutenção da Paridade de Gênero no Acesso**

✅ **Status:** Atingido
- A educação básica brasileira já apresenta paridade de gênero (49.4% vs 50.6%)
- Não são necessárias políticas urgentes de correção de acesso

### 2. **Investigação da Composição do Docentado Federal** ⚠️

🎯 **Prioridade Alta**

**Recomendações (reenquadradas em v2.1):**
- Investigar a composição do magistério federal: áreas de concurso (STEM vs humanas), tipos de instituição (IF, CEFET, colégios de aplicação) e trajetórias de contratação
- Monitorar IFR da rede Federal por tipo de instituição
- Análise de recorte racial na docência e gestão federal
- Mentoring para mulheres docentes federais em áreas com concursos majoritariamente masculinos

### 2b. **Estudo de Caso: Amazonas** 🎯

🎯 **Prioridade Alta (novo em v2.1)**

**Achado:** IFR 0.80 — gestão feminina (49.7%) muito abaixo da docência estadual (62.3%),
o maior desvio "gestão abaixo da base" do país. Em v2.2, o recorte municipal amplifica o
achado: **54.8% dos municípios amazonenses têm gestoras em minoria** (maior % do país),
incluindo Maraã (IFR 0.11: 6.9% de gestoras sobre docência de 63.1% mulheres).

**Recomendações:**
- Estudo qualitativo sobre seleção de diretores no Amazonas
- Verificar critérios de indicação e carreira de gestão na rede estadual e municipal

### 3. **Ampliar o Acesso de Professores Negros e Pardos à Docência** ⚖️

🎯 **Prioridade Alta (novo em v2.2)**

**Achado:** o filtro racial está na entrada da carreira — pardos são 52.5% do alunado e
37.9% da docência. Da docência em diante, a composição racial é estável.

**Recomendações:**
- Cotas e ações afirmativas em licenciaturas (Proupli/pedagogias) monitoradas por raça
- Avaliar vieses nos processos seletivos de contratação docente
- Acompanhar a composição racial da docência por rede (Privada embranquece no topo)

### 4. **Apoio à Gestão em Áreas Rurais**

🎯 **Prioridade Média**

**Recomendações:**
- Programas de capacitação especificamente para gestoras rurais
- Investigar por que a proporção de gestoras é menor em áreas rurais (71.4% vs 82.6%)
- Infraestrutura e apoio para escolas rurais atrair retenção de gestoras qualificadas

### 5. **Investigação da Região Norte** 🌎

🎯 **Prioridade Média**

**Recomendações:**
- Estudo qualitativo sobre por que a região Norte tem menor proporção de gestoras (63.9%)
- Programas regionais de apoio à liderança feminina na educação
- Análise de fatores culturais e contextuais

---

## 🎓 Funil por Etapa: o Ensino Médio é a Única Etapa Feminina (v2.3)

**Método (ecológico, proxy declarado):** os agregados do INEP só têm gênero no total,
não por etapa. Classificamos 54.534 escolas "de etapa única" (≥90% das matrículas em
uma etapa — 30,6% do total de matrículas) e medimos o % de meninas em cada estrato.

| Etapa (escolas puras) | Escolas | Matrículas | % meninas |
|---|---:|---:|---:|
| Creche (0–3) | 14.510 | 1.575.260 | 48.1% |
| Pré-escola (4–5) | 4.982 | 789.377 | 48.8% |
| Fund. Anos Iniciais | 18.618 | 4.738.745 | 48.8% |
| Fund. Anos Finais | 7.294 | 2.849.722 | 48.8% |
| **Ensino Médio** | 9.130 | 4.122.800 | **51.2%** |

**Leitura:** o funil é suave (~3,1 pp de variação), mas o **Ensino Médio se inverte**:
única etapa com maioria feminina — coerente com evasão masculina mais alta na
adolescência (trabalho precoce, reprovação). A "feminização" do EM é leve, porém
consistente com a literatura sobre trajetórias de gênero.

---

## 📐 Rigor Estatístico (v2.3)

**1. Efeito, não p-valor:** com o censo completo (46 milhões), qualquer diferença
é "p < 0.001" — o χ² da v2.0 era estatisticamente irrelevante. O tamanho de efeito
real: **w = 0.012** (desprezível; convenção: w < 0.1). Paridade confirmada na prática.

**IC de Wilson (95%) para % gestoras, base = gestores:**

| Rede | % gestoras | n | IC95% |
|---|---:|---:|---|
| Federal | 26.3% | 754 | [23.2%; 29.5%] |
| Estadual | 65.6% | 31.609 | [65.1%; 66.1%] |
| Municipal | 82.1% | 113.963 | [81.8%; 82.3%] |
| Privada | 83.9% | 44.315 | [83.5%; 84.2%] |

Mesmo no pior cenário do IC, a Federal fica ~35 pp abaixo das demais redes:
**o achado federal é robusto à incerteza amostral** (embora o n continue pequeno
para desdobramentos internos).

**Porte × % gestoras, ponderado por gestores (corrige o viés de escolas com 1 gestor):**

| Quartil de porte | Escolas | % gestoras |
|---|---:|---:|
| Q1 (menor) | 45.367 | 78.0% |
| Q2 | 45.033 | **84.9%** |
| Q3 | 45.013 | 82.4% |
| Q4 (maior) | 45.127 | **72.9%** |

A "não correlação" da v2.0 não se sustenta: existe relação em **U invertido** —
gestoras são mais frequentes em escolas de porte médio e menos nos extremos
(pequenas: 78,0%; grandes: 72,9%). Escolas grandes (estaduais, urbanas) têm
proporcionalmente menos mulheres na direção.

---

## 📚 Limitações da Análise

1. **Dados binários de gênero:** O Censo não captura identidades de gênero não-binárias
2. **Raça × gênero não cruzável:** os agregados do INEP não permitem "% de gestoras negras" — as análises raciais (v2.2) comparam composições marginais de alunado, docência e gestão
3. **Dados agregados:** Não é possível fazer análise individual (cada escola, não cada gestor)
4. **Sem informações salariais:** Não há dados sobre remuneração de gestores
5. **Sem informação sobre tipo de cargo:** Não é possível diferenciar diretor de vice-diretor
6. **Matrículas "não declarado" (v2.1):** 6.28 milhões de matrículas (12% do total) têm sexo não declarado (`QT_MAT_BAS_ND`) e ficam fora das porcentagens FEM/MASC; idem 30 mil gestores ND
7. **IFR federal com n pequeno:** 754 gestores federais (0.4% do total) — o índice federal carrega incerteza proporcional ao n
8. **Funil por etapa é ecológico (v2.3):** proxy por escolas de etapa única; cobre ~31% das matrículas

---

## 🚀 Próximos Passos Sugeridos

### Curto Prazo (1-3 meses)
1. Publicar artigo científico sobre **docência × gestão (IFR)** e o caso Amazonas
2. Apresentar resultados em conferência de educação
3. Investigar a composição do docentado federal (áreas de concurso, tipos de instituição)

### Médio Prazo (3-6 meses)
1. Cruzar raça × gênero com microdados individuais (agregados não permitem)
2. Realizar estudo qualitativo sobre a gestão no Amazonas (IFR 0.80)
3. Investigar dados salariais de gestores (se disponíveis)

### Longo Prazo (6-12 meses)
1. Análise temporal comparando com censos anteriores
2. Dashboard interativo para visualização de dados
3. Publicação de livro ou capítulo sobre gênero e gestão educacional

---

## 📊 Visualizações Geradas

1. `01_distribuicao_nacional.png` - Matrículas por gênero
2. `02_genero_por_rede.png` - Matrículas por rede de ensino
3. `03_meninas_por_regiao.png` - Matrículas por região
4. `04_genero_gestores.png` - Gestores por gênero
5. `05_gestoras_por_rede.png` - Gestoras por rede
6. `06_gestoras_por_regiao.png` - Gestoras por região
7. `07_alunas_vs_gestoras.png` - Comparação alunas vs gestoras
8. `08_docencia_vs_gestao.png` - Docentes vs gestoras por rede (novo em v2.1)
9. `09_ifr_por_rede.png` - Índice de Feminização Relativa (novo em v2.1)
10. `dashboard_completo.png` - Dashboard integrado com 7 painéis
11. `inversao_genero_gestao.png` - Docência vs gestão (reenquadrado em v2.1)
12. `12_funil_etapa.png` - Funil ecológico por etapa (v2.3)
13. `13_porte_gestoras.png` - Porte × gestoras ponderado (v2.3)

---

## 📝 Conclusão

Esta análise revelou que a gestão escolar básica no Brasil é dominada por mulheres (79.5%) — mas, corretamente comparada à profissão da qual recruta, a **docência (75.8% mulheres)**, a gestão **espelha a feminização da carreira** (Índice de Feminização Relativa = 1.05). O teto de vidro clássico não aparece no agregado nacional.

Os desvios estão em pontos específicos: a **rede Federal** (IFR 0.65), explicada pela única docência do país majoritariamente masculina (40.3% mulheres) — o que redireciona a investigação para a **composição do docentado federal** — e o **Amazonas** (IFR 0.80), onde a gestão (49.7%) fica bem abaixo da própria docência estadual (62.3%), o caso mais forte de barreira real à ascensão feminina no país.

Esses resultados refinam as narrativas sobre o "teto de vidro" na educação: a questão não é se as mulheres ascendem da docência à gestão (ascendem, proporcionalmente à base), mas **quem chega à docência** — em especial na rede Federal — e por que em alguns territórios a gestão descola da base.

---

**Desenvolvido com ❤️ por Sara**
Mestra em Educação | Análise de Dados Educacionais

**Data:** Março de 2026
**Versão:** 2.3 (docência × gestão, interseccionalidade, IFR municipal, funil por etapa, rigor estatístico)
