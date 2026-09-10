# Proposta de Melhorias — Análise de Gênero no Censo Escolar 2025

**Base da verificação:** dados brutos conferidos por md5 (todos OK), pipeline reexecutado do zero
em streaming (sem venv), comparação com os números dos notebooks e do CHECKPOINT_FINAL.md.

---

## 1. O que está correto (verificado)

| Verificação | Resultado |
|---|---|
| md5 das 6 tabelas INEP | ✅ todos OK |
| Escolas ativas (180.540) consistentes entre Escola/Matrícula/Gestor/Docente | ✅ 0 linhas órfãs |
| `QT_MAT_BAS_FEM + QT_MAT_BAS_MASC = QT_MAT_BAS` em todas as linhas | ✅ 0 divergências |
| 46.018.380 matrículas; 49,4% meninas | ✅ reproduzido |
| 190.641 gestores; 79,5% gestoras | ✅ reproduzido |
| Federal 26,3% gestoras; Urbana 82,6% vs Rural 71,4% | ✅ reproduzido |

O pipeline e os números do CHECKPOINT_FINAL estão tecnicamente corretos. Os problemas são
**conceituais e de cobertura**, não de cálculo.

---

## 2. Achados — o mais importante primeiro

### 2.1 🔴 A tese central ("inversão de gênero", índice 1.61x) compara com a base errada

O índice 1.61x divide **% gestoras (79,5%) por % de alunas (49,4%)**. Mas a carreira de gestão
escolar se alimenta do **docentado**, não do alunado. Usando a tabela de docentes (que está em
`data/` e **nunca foi aberta** em nenhum notebook):

| Rede | % mulheres docentes | % mulheres gestoras | razão gest/doc |
|---|---|---|---|
| Federal | 40,3% | 26,3% | **0,65x** |
| Estadual | 63,7% | 65,6% | 1,03x |
| Municipal | 83,0% | 82,1% | 0,99x |
| Privada | 76,2% | 83,9% | 1,10x |
| **Total** | **75,8%** | **79,5%** | **1,05x** |

**Leitura revisada:** a gestão escolar espelha a feminização da docência (1,05x, não 1,61x). A
verdadeira exceção continua sendo a Federal — mas com explicação provável: o corpo docente
federal é atípico (institutos federais, áreas técnicas/STEM, professor do ensino superior
compartilhado) e é o **único do país com docência majoritariamente masculina (40% FEM)**. A
gestão federal (26,3%) é proporcional à base da qual sai (0,65x) — ou seja, não é uma barreira
de promoção, é composição da base. Isso **muda a recomendação de política**: "auditoria por
teto de vidro" → "investigar a composição do docentado federal e as trajetórias de contratação".

Também é o único achado que responde à pergunta norteadora 5 ("docência: profissão feminina,
gestão masculina?") — hoje ela está sem resposta porque a tabela de docentes não entra na análise.

### 2.2 🔴 As perguntas norteadoras 1 e 4 (funil por etapa, Ensino Médio) ficaram sem resposta

Nos agregados do INEP, gênero só existe no total: `QT_MAT_BAS_FEM/MASC`. Não há colunas de
gênero por etapa (verificado: só 2 colunas FEM/MASC na Matrícula). Consequências:

- `utils.criar_grafico_funil()` espera `TP_ETAPA_ENSINO` e `TP_SEXO` — dados que não existem
  nesses CSVs; a função nunca pôde funcionar.
- O Notebook 02 não tem análise por etapa, apesar de o CLAUDE.md prometer o "funil educacional".

**Proposta honesta (sem inventar dados):** análise ecológica por "tipo de escola" — escolas
classificadas pela etapa que ofertam (só creche, só pré, AI, AF, médio, EJA), usando o
% de meninas da escola como proxy da etapa. Limitação declarada: escolas multi-etapa ficam de
fora ou entram em categoria própria. Complemento: docentes por etapa (existem QT_DOC por etapa,
mas só com gênero no agregado BAS — o funil docente fica por tamanho, não por gênero).

### 2.3 🟡 6,3 milhões de matrículas "não declarado" invisíveis

`QT_MAT_BAS_ND` soma 6.275.577 (≈12% de QT_MAT_BAS) e **não entra** na soma FEM+MASC
(FEM+MASC = QT_MAT_BAS exato em todas as linhas, com ND > 0 em muitas delas). O mesmo vale para
gestão: 30.044 gestores ND (13,6%). O projeto exclui esses registros silenciosamente. É preciso
**declarar essa limitação** e conferir na documentação INEP o que `QT_MAT_BAS_ND` significa
(há indício de inconsistência no próprio agregado: ND > 0 sem estar dentro de QT_MAT_BAS).

### 2.4 🟡 Testes estatísticos conceitualmente errados para dados censitários

- O χ² com p < 0,001 sobre 46 milhões de matrículas é sobre a **população inteira** — não há
  inferência a fazer; p-valor com n = 46M é trivialmente significativo e não informa nada.
  O correto é reportar **tamanho de efeito** (diferença em p.p., razão de chances).
- O IC de 95% para % gestoras usa `n = 180.540 escolas` — mas a unidade amostral são os
  **190.641 gestores**; a fórmula aplicada está sobre a base errada (e num censo, IC só faz
  sentido como medida de precisão de medição, não de inferência).

### 2.5 🟡 Correlação porte × % gestoras distorcida por escolas pequenas

`PORC_GESTORAS` de uma escola com 1 gestor é 0 ou 100 — a correlação sobre porcentagens
escolares é dominada por esse ruído (viés ecológico). O correto: faixas de porte (quartis de
QT_MAT_BAS) com % gestoras **ponderado pelo número de gestores**, ou correlação municipal
(5.570 municípios agregados).

### 2.6 🟡 "Exceção Federal" com base minúscula

754 gestores federais em 716 escolas (0,4% do total). Qualquer comparação federal vs demais
redes precisa de IC (com n = 754, 26,3% → IC95% ≈ [23,2%; 29,6%]) e da leitura do item 2.1.

### 2.7 🟢 Interseccionalidade disponível e não usada

Recorte racial existe **pronto** nas tabelas de gestores e docentes:

| Raça | Gestores(as) | Docentes |
|---|---|---|
| Branca | 52,4% | 52,9% |
| Parda | 38,9% | 37,9% |
| Preta | 6,7% | 7,2% |
| Indígena | 1,3% | 1,0% |
| Amarela | 0,8% | 1,0% |
| (ND) | 15,8% | 17,6% |

A gestão espelha a raça da docência, e ambas sobrepresentam brancos frente à população
(~43% branca). É o "próximo passo" que o próprio CHECKPOINT lista — e os dados já estão lá.

---

## 3. Problemas de reprodutibilidade (secundários, mas reais)

1. **Repositório git corrompido**: `refs/heads/main` aponta para objeto inexistente
   (`ac82b6db...`) — qualquer `git status/log` falha.
2. `data/processed/` só tem `escolas_analise.csv`; os outros 3 CSVs citados no CHECKPOINT
   sumiram. `outputs/figures/` está vazio (só checkpoints). O projeto não se reproduz do disco.
3. `venv/` quebrado: `bin/` sem executáveis Python, `pyvenv.cfg` apontando para
   `/home/sara/Censo25/venv` (caminho antigo). Sem pandas/scipy instaláveis no estado atual.
4. **CLAUDE.md descreve tabelas que não existem**: diz que Matrícula tem `TP_SEXO`
   individual ("1=Feminino, 2=Masculino") e Gestor tem `TP_CARGO_GESTOR` — nada disso existe;
   os CSVs são agregados por escola (`QT_*_FEM/MASC`). O exemplo de código do CLAUDE.md
   (`df['TP_SEXO'] == 'Feminino'`) falharia.
5. Duplicação: Notebooks 02/03/04 repetem o mesmo groupby; `utils.py` tem funções nunca
   usadas; `config.py` imprime no import (quebra uso em scripts não-interativos).

---

## 4. Plano de melhorias proposto (priorizado)

### P0 — Reenquadrar a tese central (meio dia de trabalho)
- Adicionar Tabela_Docente à análise: % mulheres docentes por rede/UF/etapa.
- Substituir "Índice de Representação Feminina 1.61x" pelo **Índice de Feminização Relativa**
  = %gestoras ÷ %docentes (1,05x nacional; Federal 0,65x; Privada 1,10x).
- Reescrever a seção "teto de vidro": a Federal não é exceção de promoção, é exceção de
  **composição docente** — nova (e mais forte) pergunta de pesquisa.
- Atualizar relatorio_sintese.md, apresentacao_resultados.md e resumo_executivo.csv.

### P1 — Interseccionalidade (1–2 dias)
- Raça × gênero em gestão e docência (tabelas já possuem as colunas).
- Análise municipal: ranking dos 5.570 municípios por % gestoras; identificar onde gestoras
  são minoria (<50%) — quase nenhum trabalho existe nesse nível.
- Porte × % gestoras ponderado por nº de gestores (corrige o achado 2.5).

### P2 — Funil por etapa honesto (1 dia)
- Classificação ecológica por tipo de escola + % de meninas como proxy de etapa, com
  limitações declaradas; comparar com docentes por etapa.

### P3 — Rigor estatístico (meio dia)
- Trocar p-valores censitários por tamanhos de efeito e ICs com n correto (gestores, não escolas).
- IC de Wilson para a Federal (n=754) antes de qualquer recomendação de "auditoria".

### P4 — Reprodutibilidade (1 dia)
- Reparar git, regenerar `data/processed/` e figuras, recriar venv com `uv`,
  corrigir CLAUDE.md (esquema real das tabelas), consolidar funções duplicadas em `scripts/`.

---

## 5. O que não recomendo

- **Análise temporal agora**: os agregados atuais não têm séries anteriores baixadas; só vale
  com Censos 2021–2023 na mão.
- **Dashboard interativo** antes de P0: visualizaria o índice 1.61x, que está metodologicamente
  frágil — primeiro o enquadramento, depois a vitrine.
- Microdados individuais: o CSV disponível já é agregado por escola; TP_SEXO individual não
  existe nessa distribuição.