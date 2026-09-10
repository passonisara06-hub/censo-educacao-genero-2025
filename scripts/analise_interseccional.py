# -*- coding: utf-8 -*-
"""
Análise Interseccional (v2.2) — Raça/cor e Municípios
======================================================
P1 da proposta de melhorias:

1) RAÇA/COR: composição racial do alunado × docência × gestão.
   Comparar quem está na escola, quem ensina e quem dirige.
   LIMITAÇÃO declarada: os agregados do INEP não cruzam raça × gênero —
   as distribuições raciais são marginais (não é possível calcular
   "% de gestoras negras" com esses agregados).

2) IFR MUNICIPAL: ranking dos municípios por Índice de Feminização Relativa
   (gestão ÷ docência), com filtro de n para os extremos.

Saídas:
- outputs/interseccional_raca.csv
- outputs/interseccional_raca_por_rede.csv
- outputs/ifr_municipal.csv
"""
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH, OUTPUTS_PATH, DEPENDENCIA

RACAS = ['BRANCA', 'PRETA', 'PARDA', 'AMARELA', 'INDIGENA']
ROTULOS = {'BRANCA': 'Branca', 'PRETA': 'Preta', 'PARDA': 'Parda',
           'AMARELA': 'Amarela', 'INDIGENA': 'Indígena'}

# ----------------------------------------------------------------------
# 1. Dimensões das escolas (uma vez só)
# ----------------------------------------------------------------------
print('🏫 Carregando dimensões das escolas...')
escolas = pd.read_csv(
    RAW_DATA_PATH + 'Tabela_Escola_2025.csv',
    sep=';', encoding='latin1',
    usecols=['CO_ENTIDADE', 'CO_MUNICIPIO', 'NO_MUNICIPIO', 'SG_UF',
             'NO_REGIAO', 'TP_DEPENDENCIA', 'TP_SITUACAO_FUNCIONAMENTO'],
    low_memory=False
)
escolas = escolas[escolas['TP_SITUACAO_FUNCIONAMENTO'] == 1].copy()
escolas['TP_DEPENDENCIA'] = escolas['TP_DEPENDENCIA'].map(DEPENDENCIA)
dims = escolas[['CO_ENTIDADE', 'CO_MUNICIPIO', 'NO_MUNICIPIO', 'SG_UF',
                'NO_REGIAO', 'TP_DEPENDENCIA']]
print(f'   {len(dims):,} escolas ativas')

# ----------------------------------------------------------------------
# 2. Raça/cor: alunado, docentes e gestores (nacional)
# ----------------------------------------------------------------------
def distrib_raca(caminho, prefixo):
    """Soma as colunas QT_<prefixo>_<RACA> + ND e devolve dict {raca: n}."""
    cols = [f'{prefixo}_{r}' for r in RACAS] + [f'{prefixo}_ND']
    df = pd.read_csv(caminho, sep=';', encoding='latin1', usecols=cols,
                     low_memory=False)
    tot = {r: float(df[f'{prefixo}_{r}'].sum()) for r in RACAS}
    tot['ND'] = float(df[f'{prefixo}_ND'].sum())
    tot['n_declarado'] = sum(tot[r] for r in RACAS)
    return tot

print('📚 Alunado (raça/cor)...')
alunado = distrib_raca(RAW_DATA_PATH + 'Tabela_Matricula_2025.csv', 'QT_MAT_BAS')
print('👩‍🏫 Docentes (raça/cor)...')
docentes = distrib_raca(RAW_DATA_PATH + 'Tabela_Docente_2025.csv', 'QT_DOC_BAS')
print('💼 Gestores (raça/cor)...')
gestores = distrib_raca(RAW_DATA_PATH + 'Tabela_Gestor_Escolar_2025.csv', 'QT_GEST_BAS')

linhas = []
for nome, d in [('Alunado', alunado), ('Docentes', docentes), ('Gestores', gestores)]:
    linha = {'categoria': nome, 'n_declarado': d['n_declarado'], 'n_ND': d['ND']}
    for r in RACAS:
        linha[ROTULOS[r]] = round(d[r] / d['n_declarado'] * 100, 2)
    linhas.append(linha)
tabela_raca = pd.DataFrame(linhas)
tabela_raca.to_csv(OUTPUTS_PATH + 'interseccional_raca.csv', index=False, encoding='utf-8')
print('\n📊 Composição racial (% do declarado):')
print(tabela_raca.to_string(index=False))

# Índice de representatividade racial: %gest ÷ %doc e %gest ÷ %alunado
rep = pd.DataFrame({'raca': [ROTULOS[r] for r in RACAS]})
for r, rot in ROTULOS.items():
    rep.loc[rep['raca'] == rot, 'gest_por_doc'] = round(
        gestores[r] / gestores['n_declarado'] / (docentes[r] / docentes['n_declarado']), 3)
    rep.loc[rep['raca'] == rot, 'gest_por_alunado'] = round(
        gestores[r] / gestores['n_declarado'] / (alunado[r] / alunado['n_declarado']), 3)
rep.to_csv(OUTPUTS_PATH + 'representatividade_racial.csv', index=False, encoding='utf-8')
print('\n📈 Representatividade racial (razão de presença):')
print(rep.to_string(index=False))

# ----------------------------------------------------------------------
# 3. Raça/cor por rede (docentes e gestores)
# ----------------------------------------------------------------------
def raca_por_rede(caminho, prefixo, label):
    cols = [f'{prefixo}_{r}' for r in RACAS]
    df = pd.read_csv(caminho, sep=';', encoding='latin1', usecols=cols,
                     low_memory=False)
    df = df.merge(dims[['CO_ENTIDADE', 'TP_DEPENDENCIA']], left_index=True,
                  right_on='CO_ENTIDADE', how='inner') \
        if 'CO_ENTIDADE' not in df.columns else df
    return df

# Docentes: usar o arquivo processado da v2.1 (já tem rede mapeada)
doc_p = pd.read_csv(PROCESSED_DATA_PATH + 'docentes_analise.csv',
                    usecols=['TP_DEPENDENCIA'] + [f'QT_DOC_BAS_{r}' for r in RACAS])
doc_r = doc_p.groupby('TP_DEPENDENCIA')[[f'QT_DOC_BAS_{r}' for r in RACAS]].sum()
doc_r.columns = [ROTULOS[c.replace('QT_DOC_BAS_', '')] for c in doc_r.columns]

# Gestores: carregar raw + join com dims
g_cols = [f'QT_GEST_BAS_{r}' for r in RACAS]
ges_p = pd.read_csv(RAW_DATA_PATH + 'Tabela_Gestor_Escolar_2025.csv',
                    sep=';', encoding='latin1',
                    usecols=['CO_ENTIDADE'] + g_cols,
                    low_memory=False)
ges_p = ges_p.merge(dims[['CO_ENTIDADE', 'TP_DEPENDENCIA']], on='CO_ENTIDADE', how='inner')
ges_r = ges_p.groupby('TP_DEPENDENCIA')[g_cols].sum()
ges_r.columns = [ROTULOS[c.replace('QT_GEST_BAS_', '')] for c in ges_r.columns]

por_rede = (doc_r / doc_r.sum(axis=1).values[:, None] * 100).round(2)
por_rede.columns = [f'doc_{c} (%)' for c in por_rede.columns]
gest_pct = (ges_r / ges_r.sum(axis=1).values[:, None] * 100).round(2)
gest_pct.columns = [f'gest_{c} (%)' for c in gest_pct.columns]
por_rede = por_rede.join(gest_pct).reset_index()
por_rede.to_csv(OUTPUTS_PATH + 'interseccional_raca_por_rede.csv', index=False, encoding='utf-8')
print('\n🏫 Composição racial por rede (doc_ e gest_ em %):')
print(por_rede.to_string(index=False))

# ----------------------------------------------------------------------
# 4. IFR municipal
# ----------------------------------------------------------------------
print('\n🗺️ Calculando IFR municipal...')
doc_m = doc_p = None  # liberar

gest_m = pd.read_csv(PROCESSED_DATA_PATH + 'escolas_analise.csv',
                     usecols=['CO_ENTIDADE', 'CO_MUNICIPIO', 'NO_MUNICIPIO',
                              'SG_UF', 'NO_REGIAO',
                              'QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC'])
gest_mun = gest_m.groupby('CO_MUNICIPIO').agg(
    NO_MUNICIPIO=('NO_MUNICIPIO', 'first'), SG_UF=('SG_UF', 'first'),
    gest_fem=('QT_GEST_BAS_FEM', 'sum'), gest_masc=('QT_GEST_BAS_MASC', 'sum')
).reset_index()

doc_m = pd.read_csv(PROCESSED_DATA_PATH + 'docentes_analise.csv',
                    usecols=['CO_ENTIDADE', 'QT_DOC_BAS_FEM', 'QT_DOC_BAS_MASC'])
doc_m = doc_m.merge(dims[['CO_ENTIDADE', 'CO_MUNICIPIO']], on='CO_ENTIDADE', how='inner')
doc_mun = doc_m.groupby('CO_MUNICIPIO').agg(
    doc_fem=('QT_DOC_BAS_FEM', 'sum'), doc_masc=('QT_DOC_BAS_MASC', 'sum')).reset_index()

mun = gest_mun.merge(doc_mun, on='CO_MUNICIPIO', how='outer').fillna(0)
mun['n_gestores'] = mun['gest_fem'] + mun['gest_masc']
mun['n_docentes'] = mun['doc_fem'] + mun['doc_masc']
mun['pct_gest_fem'] = (mun['gest_fem'] / mun['n_gestores'] * 100).round(2)
mun['pct_doc_fem'] = (mun['doc_fem'] / mun['n_docentes'] * 100).round(2)
mun['ifr'] = (mun['pct_gest_fem'] / mun['pct_doc_fem']).round(3)
mun = mun[mun['n_gestores'] > 0].sort_values('ifr')
mun[['CO_MUNICIPIO', 'NO_MUNICIPIO', 'SG_UF', 'n_docentes', 'pct_doc_fem',
     'n_gestores', 'pct_gest_fem', 'ifr']].to_csv(
    OUTPUTS_PATH + 'ifr_municipal.csv', index=False, encoding='utf-8')

print(f'✅ {len(mun):,} municípios com IFR calculado')
print(f'   • IFR < 0.90: {(mun["ifr"] < 0.90).sum()} municípios')
print(f'   • IFR 0.90–1.10: {mun["ifr"].between(0.90, 1.10).sum()} municípios')
print(f'   • IFR > 1.10: {(mun["ifr"] > 1.10).sum()} municípios')
print(f'   • Gestoras < 50%: {(mun["pct_gest_fem"] < 50).sum()} municípios')

filtro = mun[mun['n_gestores'] >= 20]
print('\n📍 10 MENORES IFR municipal (n_gestores >= 20):')
print(filtro.head(10)[['NO_MUNICIPIO', 'SG_UF', 'pct_doc_fem', 'pct_gest_fem', 'ifr']].to_string(index=False))
print('\n📍 10 MAIORES IFR municipal (n_gestores >= 20):')
print(filtro.tail(10)[['NO_MUNICIPIO', 'SG_UF', 'pct_doc_fem', 'pct_gest_fem', 'ifr']].to_string(index=False))