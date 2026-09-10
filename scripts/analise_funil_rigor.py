# -*- coding: utf-8 -*-
"""
P2+P3 (v2.3) — Funil ecológico por etapa + Rigor estatístico
=============================================================
P2) FUNIL POR ETAPA (ecológico): como gênero por etapa não existe nos agregados
    (só QT_MAT_BAS_FEM/MASC no total), classifica cada escola pela etapa que
    responde por >=90% das suas matrículas de 5 etapas regulares e calcula
    o % de meninas em cada estrato. É um PROXY: escolas multi-etapa ficam fora
    da classificação (cobertura ~30% das matrículas). Limitação declarada.

P3) RIGOR ESTATÍSTICO:
    - p-valor censitário substituído por tamanho de efeito (w)
    - IC de Wilson para % gestoras por rede (n = gestores)
    - Porte × % gestoras ponderado por nº de gestores

Saídas:
- outputs/funil_etapa.csv
- outputs/rigor_estatistico.csv
- outputs/porte_gestoras.csv
"""
import sys
import os
import numpy as np
import pandas as pd
from scipy import stats

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import PROCESSED_DATA_PATH, OUTPUTS_PATH

# ======================================================================
# P2 — FUNIL ECOLÓGICO POR ETAPA
# ======================================================================
print('📊 P2 — FUNIL ECOLÓGICO POR ETAPA')
print('=' * 60)

df = pd.read_csv(
    PROCESSED_DATA_PATH + 'escolas_analise.csv',
    usecols=['QT_MAT_BAS_FEM', 'QT_MAT_BAS_MASC', 'QT_MAT_INF_CRE', 'QT_MAT_INF_PRE',
             'QT_MAT_FUND_AI', 'QT_MAT_FUND_AF', 'QT_MAT_MED', 'TP_DEPENDENCIA',
             'TP_LOCALIZACAO', 'NO_REGIAO']
)
ETAPAS = {'QT_MAT_INF_CRE': 'Creche (0–3)',
          'QT_MAT_INF_PRE': 'Pré-escola (4–5)',
          'QT_MAT_FUND_AI': 'Fund. Anos Iniciais',
          'QT_MAT_FUND_AF': 'Fund. Anos Finais',
          'QT_MAT_MED': 'Ensino Médio'}
et_cols = list(ETAPAS)

tot5 = df[et_cols].sum(axis=1)
maxe = df[et_cols].max(axis=1)
share = (maxe / tot5.replace(0, pd.NA)).fillna(0)
dominante = df[et_cols].idxmax(axis=1).where(share >= 0.9)

pure = df.copy()
pure['etapa_dominante'] = dominante.map(ETAPAS)
pure = pure[pure['etapa_dominante'].notna()]

funil = pure.groupby('etapa_dominante').agg(
    escolas=('etapa_dominante', 'size'),
    fem=('QT_MAT_BAS_FEM', 'sum'),
    masc=('QT_MAT_BAS_MASC', 'sum'),
).reindex(list(ETAPAS.values()))
funil['total'] = funil['fem'] + funil['masc']
funil['pct_meninas'] = (funil['fem'] / funil['total'] * 100).round(2)

# salvar com índice rotulado (etapa como primeira coluna)
funil_out = funil.copy()
funil_out.index.name = 'etapa'
funil_out.to_csv(OUTPUTS_PATH + 'funil_etapa.csv', encoding='utf-8')
cobertura = pure['QT_MAT_BAS_FEM'].sum() + pure['QT_MAT_BAS_MASC'].sum()
total_nac = df['QT_MAT_BAS_FEM'].sum() + df['QT_MAT_BAS_MASC'].sum()

print(funil[['escolas', 'total', 'pct_meninas']].to_string())
print(f'\nEscolas classificadas (>=90% em 1 etapa): {len(pure):,} de {len(df):,} '
      f'({len(pure) / len(df) * 100:.1f}%)')
print(f'Cobertura de matrículas do proxy: {cobertura / total_nac * 100:.1f}%')

# ======================================================================
# P3 — RIGOR ESTATÍSTICO
# ======================================================================
print('\n📊 P3 — RIGOR ESTATÍSTICO')
print('=' * 60)

# --- 3.1 Tamanho de efeito: matrículas (censo -> efeito, não p-valor) ---
tot_f = df['QT_MAT_BAS_FEM'].sum()
tot_m = df['QT_MAT_BAS_MASC'].sum()
n = tot_f + tot_m
chisq, pval = stats.chisquare([tot_f, tot_m])
w_cramer = float(np.sqrt(chisq / n))

linha_mat = {
    'analise': 'Matrículas (censo completo)',
    'n': n,
    'estatistica': f'chi2 = {chisq:.2f}',
    'p_valor': f'{pval:.2e}',
    'tamanho_de_efeito': f'w = {w_cramer:.4f}',
    'leitura': 'Efeito desprezivel (w < 0.1) — paridade na pratica'
}

# --- 3.2 IC de Wilson para % gestoras por rede ---
def wilson(k, n, z=1.96):
    """Intervalo de confiança de Wilson para proporção."""
    if n == 0:
        return (float('nan'), float('nan'))
    phat = k / n
    denom = 1 + z**2 / n
    centro = (phat + z**2 / (2 * n)) / denom
    margem = z * np.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2)) / denom
    return centro - margem, centro + margem

gest = pd.read_csv(
    PROCESSED_DATA_PATH + 'escolas_analise.csv',
    usecols=['TP_DEPENDENCIA', 'QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC']
)
g_rede = gest.groupby('TP_DEPENDENCIA')[['QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC']].sum()

linhas = [linha_mat]
for rede in ['Federal', 'Estadual', 'Municipal', 'Privada']:
    k = float(g_rede.loc[rede, 'QT_GEST_BAS_FEM'])
    nn = k + float(g_rede.loc[rede, 'QT_GEST_BAS_MASC'])
    p_g = k / nn
    lo, hi = wilson(k, nn)
    linhas.append({
        'analise': f'Gestoras {rede}',
        'n': int(nn),
        'estatistica': f'{p_g * 100:.2f}%',
        'p_valor': '—',
        'tamanho_de_efeito': f'IC95% Wilson: [{lo * 100:.2f}%; {hi * 100:.2f}%]',
        'leitura': 'n pequeno — incerteza considerável' if rede == 'Federal' else 'IC estreito'
    })

rigor = pd.DataFrame(linhas)
rigor.to_csv(OUTPUTS_PATH + 'rigor_estatistico.csv', index=False, encoding='utf-8')
print(rigor.to_string(index=False))

# --- 3.3 Porte × % gestoras (ponderado por nº de gestores) ---
print('\n📈 PORTE x % GESTORAS (ponderado por gestores)')
print('=' * 60)
g2 = pd.read_csv(
    PROCESSED_DATA_PATH + 'escolas_analise.csv',
    usecols=['QT_MAT_BAS', 'QT_GEST_BAS_FEM', 'QT_GEST_BAS_MASC']
)
g2['n_gestores'] = g2['QT_GEST_BAS_FEM'] + g2['QT_GEST_BAS_MASC']
g2 = g2[g2['n_gestores'] > 0]
g2['faixa'] = pd.qcut(g2['QT_MAT_BAS'], q=4,
                      labels=['Q1 (menor porte)', 'Q2', 'Q3', 'Q4 (maior porte)'])

rows = []
for faixa, x in g2.groupby('faixa', observed=True):
    rows.append({
        'faixa': str(faixa),
        'escolas': len(x),
        'n_gestores': int(x['n_gestores'].sum()),
        'pct_gestoras_ponderada': round(x['QT_GEST_BAS_FEM'].sum() / x['n_gestores'].sum() * 100, 2),
        'pct_media_escolas': round((x['QT_GEST_BAS_FEM'] / x['n_gestores']).mean() * 100, 2),
    })
porte = pd.DataFrame(rows)
porte.to_csv(OUTPUTS_PATH + 'porte_gestoras.csv', index=False, encoding='utf-8')
print(porte.to_string(index=False))

dif_pond = porte['pct_gestoras_ponderada'].iloc[-1] - porte['pct_gestoras_ponderada'].iloc[0]
dif_naopond = porte['pct_media_escolas'].iloc[-1] - porte['pct_media_escolas'].iloc[0]
print(f'\nDiferença ponderada Q4-Q1: {dif_pond:.1f} pp | não-ponderada (média de escolas): {dif_naopond:.1f} pp')
print('✅ P2 + P3 concluídos!')