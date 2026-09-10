# -*- coding: utf-8 -*-
"""
Análise Docência × Gestão — Índice de Feminização Relativa (IFR)
================================================================
Reenquadramento da tese central do projeto (v2.1):

    IFR = % mulheres gestoras ÷ % mulheres docentes

A gestão escolar recruta a partir da docência — comparar gestão com ALUNADO
(como fazia o índice 1.61x) usa a base errada. IFR = 1.00 significa que a
gestão espelha a feminização da docência; > 1.00 indica sobre-representação
feminina na gestão; < 1.00 indica sub-representação (possível barreira).

Saídas:
- data/processed/docentes_analise.csv   (nível escola, para notebooks)
- outputs/docencia_gestao_por_rede.csv
- outputs/docencia_gestao_por_regiao.csv
- outputs/docencia_gestao_por_uf.csv
- outputs/indices_feminizacao.csv       (consolidado p/ notebooks 03-05)
"""
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH, OUTPUTS_PATH, DEPENDENCIA, LOCALIZACAO

# ----------------------------------------------------------------------
# 1. Escolas ativas (chaves e dimensões)
# ----------------------------------------------------------------------
COLS_ESCOLA = [
    'CO_ENTIDADE', 'NO_REGIAO', 'SG_UF',
    'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'TP_SITUACAO_FUNCIONAMENTO'
]

COLS_DOCENTE = [
    'CO_ENTIDADE',
    'QT_DOC_BAS', 'QT_DOC_BAS_FEM', 'QT_DOC_BAS_MASC', 'QT_DOC_BAS_ND',
    # raça/cor: disponível para a análise interseccional (próxima fase)
    'QT_DOC_BAS_BRANCA', 'QT_DOC_BAS_PRETA', 'QT_DOC_BAS_PARDA',
    'QT_DOC_BAS_AMARELA', 'QT_DOC_BAS_INDIGENA',
]

print('🏫 Carregando escolas...')
escolas = pd.read_csv(
    RAW_DATA_PATH + 'Tabela_Escola_2025.csv',
    sep=';', encoding='latin1', usecols=COLS_ESCOLA, low_memory=False
)
escolas = escolas[escolas['TP_SITUACAO_FUNCIONAMENTO'] == 1].copy()
escolas['TP_DEPENDENCIA'] = escolas['TP_DEPENDENCIA'].map(DEPENDENCIA)
escolas['TP_LOCALIZACAO'] = escolas['TP_LOCALIZACAO'].map(LOCALIZACAO)
print(f'   {len(escolas):,} escolas ativas')

# ----------------------------------------------------------------------
# 2. Docentes por escola (agregados do INEP)
# ----------------------------------------------------------------------
print('👩‍🏫 Carregando docentes...')
docentes = pd.read_csv(
    RAW_DATA_PATH + 'Tabela_Docente_2025.csv',
    sep=';', encoding='latin1', usecols=COLS_DOCENTE, low_memory=False
)

doc = docentes.merge(escolas, on='CO_ENTIDADE', how='inner')
print(f'   {len(doc):,} linhas de docentes vinculadas a escolas ativas')

doc.to_csv(PROCESSED_DATA_PATH + 'docentes_analise.csv', index=False, encoding='utf-8')
print(f'💾 {PROCESSED_DATA_PATH}docentes_analise.csv')

# ----------------------------------------------------------------------
# 3. Gestoras por escola (do arquivo processado existente)
# ----------------------------------------------------------------------
gest = pd.read_csv(
    PROCESSED_DATA_PATH + 'escolas_analise.csv',
    encoding='utf-8',
    usecols=['CO_ENTIDADE', 'QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC']
)

# ----------------------------------------------------------------------
# 4. Índice de Feminização Relativa por rede / região / UF
# ----------------------------------------------------------------------
def tabela_ifr(dim):
    """Agrega docentes e gestoras pela dimensão e calcula o IFR."""
    d = doc.groupby(dim)[['QT_DOC_BAS_FEM', 'QT_DOC_BAS_MASC']].sum()
    g = gest.merge(
        escolas[['CO_ENTIDADE', dim]], on='CO_ENTIDADE', how='left'
    ).groupby(dim)[['QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC']].sum()

    t = pd.DataFrame(index=d.index)
    t['n_docentes'] = d['QT_DOC_BAS_FEM'] + d['QT_DOC_BAS_MASC']
    t['pct_doc_fem'] = d['QT_DOC_BAS_FEM'] / t['n_docentes'] * 100
    t['n_gestores'] = g['QT_GEST_BAS_FEM'] + g['QT_GEST_BAS_MASC']
    t['pct_gest_fem'] = g['QT_GEST_BAS_FEM'] / t['n_gestores'] * 100
    t['ifr'] = t['pct_gest_fem'] / t['pct_doc_fem']
    return t.round(2).reset_index()

por_rede = tabela_ifr('TP_DEPENDENCIA')
por_regiao = tabela_ifr('NO_REGIAO')
por_uf = tabela_ifr('SG_UF')

por_rede.to_csv(OUTPUTS_PATH + 'docencia_gestao_por_rede.csv', index=False, encoding='utf-8')
por_regiao.to_csv(OUTPUTS_PATH + 'docencia_gestao_por_regiao.csv', index=False, encoding='utf-8')
por_uf.to_csv(OUTPUTS_PATH + 'docencia_gestao_por_uf.csv', index=False, encoding='utf-8')

# Consolidado: linha Brasil + por rede (usado nos notebooks 03/04/05)
nacional = {
    'TP_DEPENDENCIA': 'Brasil',
    'n_docentes': [por_rede['n_docentes'].sum()],
    'pct_doc_fem': [(doc['QT_DOC_BAS_FEM'].sum() / (doc['QT_DOC_BAS_FEM'].sum() + doc['QT_DOC_BAS_MASC'].sum())) * 100],
    'n_gestores': [por_rede['n_gestores'].sum()],
    'pct_gest_fem': [(gest['QT_GEST_BAS_FEM'].sum() / (gest['QT_GEST_BAS_FEM'].sum() + gest['QT_GEST_BAS_MASC'].sum())) * 100],
    'ifr': [None],
}
nacional['ifr'] = [nacional['pct_gest_fem'][0] / nacional['pct_doc_fem'][0]]
consolidado = pd.concat(
    [pd.DataFrame({k: (v if isinstance(v, list) else [v]) for k, v in nacional.items()}),
     por_rede],
    ignore_index=True
).round(2)
consolidado.to_csv(OUTPUTS_PATH + 'indices_feminizacao.csv', index=False, encoding='utf-8')

print()
print('📊 Índice de Feminização Relativa (IFR = %gestoras ÷ %docentes):')
print(consolidado.to_string(index=False))
print()
print('✅ Análise docência × gestão concluída!')