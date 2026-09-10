# -*- coding: utf-8 -*-
"""Atualiza o notebook 04 para o reenquadramento IFR (v2.1) e o executa por completo."""
import json
import nbformat
from nbclient import NotebookClient

NB = 'notebooks/04_sintese_e_visualizacoes.ipynb'
nb = nbformat.read(NB, as_version=4)

def get_src(c):
    return ''.join(c.source)

# ------------------------------------------------------------------
# Célula 11: substituir "ANÁLISE 2" (índice vs alunado) e "ANÁLISE 3"
# ------------------------------------------------------------------
for c in nb.cells:
    if c.cell_type != 'code' or 'ÍNDICE DE REPRESENTAÇÃO FEMININA' not in get_src(c):
        continue
    src = get_src(c)
    # localizar e substituir do "ANÁLISE 2" até o fim, mantendo ANÁLISE 1
    idx = src.find('# ANÁLISE 2')
    analise1 = src[:idx]
    nova = analise1 + '''# ANÁLISE 2: Índice de Feminização Relativa (gestão × docência)
print("\\n\\n📊 ÍNDICE DE FEMINIZAÇÃO RELATIVA (IFR):")
print("=" * 60)

# Base correta: a gestão recruta da DOCÊNCIA, não do alunado.
# Tabela consolidada gerada por scripts/analise_docentes.py
import sys
sys.path.append('../scripts')
from config import OUTPUTS_PATH as _OUT

ifr_df = pd.read_csv(_OUT + 'indices_feminizacao.csv')
ordem = ['Brasil', 'Federal', 'Estadual', 'Municipal', 'Privada']
ifr_df['_o'] = ifr_df['TP_DEPENDENCIA'].apply(lambda x: ordem.index(x) if x in ordem else 9)
ifr_df = ifr_df.sort_values('_o').drop(columns='_o')
print(ifr_df[['TP_DEPENDENCIA', 'pct_doc_fem', 'pct_gest_fem', 'ifr']].to_string(index=False))

m = calcular_metricas_principais(df)
ifr_brasil = ifr_df[ifr_df['TP_DEPENDENCIA'] == 'Brasil'].iloc[0]['ifr']
print(f"\\nInterpretação:")
print(f"  • Docência nacional: {ifr_df[ifr_df['TP_DEPENDENCIA']=='Brasil'].iloc[0]['pct_doc_fem']:.1f}% mulheres")
print(f"  • Gestão nacional:   {m['pct_gestoras']:.1f}% mulheres")
print(f"  • IFR = {ifr_brasil:.2f} → a gestão espelha a feminização da docência (não uma")
print(f"    'inversão' de 1.61x: o índice antigo usava a base errada — o ALUNADO (49.4%)")
print(f"    em vez da docência (75.8%), que é o banco de candidatas à gestão.")

fed = ifr_df[ifr_df['TP_DEPENDENCIA'] == 'Federal'].iloc[0]
print(f"\\n  • Rede Federal: docência {fed['pct_doc_fem']:.1f}% mulheres (única rede com")
print(f"    docência majoritariamente MASCULINA) × gestão {fed['pct_gest_fem']:.1f}%")
print(f"    → IFR federal {fed['ifr']:.2f}: gestão proporcional à base docente.")
print(f"    Pergunta de pesquisa correta: por que a DOCÊNCIA federal é masculina?")

# ANÁLISE 3: Reflexão Crítica sobre Teto de Vidro (reenquadrada)
print("\\n\\n🔍 REFLEXÃO CRÍTICA (v2.1):")
print("=" * 60)
print("O teto de vidro clássico (docência feminina → gestão masculina) NÃO aparece")
print("no agregado nacional: IFR = 1.05. Os desvios estão em pontos específicos:")
print("  • Federal (0.65x): reflexo da composição docente masculina — investigar")
print("    contratação/áreas de concurso, não apenas 'promocão'.")
print("  • Amazonas (0.80x): gestão (49.7%) bem abaixo da própria docência (62.3%)")
print("    — o caso mais forte de barreira real no país; candidato a estudo de caso.")
print("  • Nordeste/Sul (1.07–1.16x): gestão acima da docência (PB, RJ, PE, RN, AL).")

print("\\n💡 Perguntas para investigação futura:")
print("  • Por que a docência federal é majoritariamente masculina?")
print("  • Por que o Amazonas tem gestoras muito abaixo da docência estadual?")
print("  • Como o IFR varia com recorte racial (dados disponíveis nas tabelas)?")
print("  • Há segmentação por tipo de cargo (diretor vs vice-diretor)?")
'''
    c.source = nova

# ------------------------------------------------------------------
# Célula 10 (figura inversão): reenquadrar anotação
# ------------------------------------------------------------------
for c in nb.cells:
    if c.cell_type != 'code' or 'inversao_genero_gestao.png' not in get_src(c):
        continue
    src = get_src(c)
    src = src.replace(
        "categorias = ['Meninas\\n(Educandos)', 'Gestoras\\n(Gestores Escolares)']",
        "categorias = ['Docentes\\n(mulheres)', 'Gestoras\\n(Gestores Escolares)']"
    )
    src = src.replace(
        "valores = [pct_fem, pct_gestoras]",
        "pct_docentes_fem = 75.76  # Tabela_Docente_2025 (scripts/analise_docentes.py)\nvalores = [pct_docentes_fem, pct_gestoras]"
    )
    src = src.replace(
        "ax.set_title('A Inversão de Gênero na Educação Brasileira\\nMulheres são MAIORIA na gestão do que nas salas de aula',",
        "ax.set_title('Da docência à gestão: a liderança espelha a base\\nGestão feminina proporcional à docência (IFR 1.05x)',"
    )
    src = src.replace(
        "'DESAFIO À NARRATIVA DO \\\"TETO DE VIDRO\\\"\\n\\nMulheres não estão sub-representadas na gestão.\\nPelo contrário, estão PROPORCIONALMENTE MAIS\\nrepresentadas em posições de liderança escolar!'",
        "'A GESTÃO ESPELHA A DOCÊNCIA (IFR 1.05x)\\n\\n79.5% das gestoras vs 75.8% de docentes mulheres.\\nExceção: rede Federal (IFR 0.65x), explicada pela\\ndocência federal majoritariamente masculina (40.3%)!'"
    )
    c.source = src

# ------------------------------------------------------------------
# Célula 8 (resumo executivo CSV): adicionar linhas de docência/IFR
# ------------------------------------------------------------------
for c in nb.cells:
    if c.cell_type != 'code' or 'resumo_executivo.csv' not in get_src(c):
        continue
    src = get_src(c)
    old = """        'Diferença (Gestoras - Meninas)'
    ],"""
    new = """        'Diferença (Gestoras - Meninas)',
        '% Mulheres na docência',
        'IFR (gestão ÷ docência)'
    ],"""
    src = src.replace(old, new)
    old2 = """        f"{pct_gestoras - pct_fem:+.1f} pp"
    ]"""
    new2 = """        f"{pct_gestoras - pct_fem:+.1f} pp",
        "75.8%",
        "1.05x"
    ]"""
    src = src.replace(old2, new2)
    c.source = src

# ------------------------------------------------------------------
# Célula markdown final: atualizar descoberta chave
# ------------------------------------------------------------------
for c in nb.cells:
    if c.cell_type != 'markdown' or 'INVERSÃO DE GÊNERO NA GESTÃO ESCOLAR' not in get_src(c):
        continue
    c.source = """## ✅ Resumo do Notebook

### 📊 Análises Concluídas:
- ✅ Panorama nacional de matrículas e gestão
- ✅ Análises por rede de ensino
- ✅ Disparidades regionais
- ✅ Comparação alunas vs gestoras
- ✅ Dashboard integrado
- ✅ Índice de Feminização Relativa (gestão × docência)

### 📁 Arquivos Gerados:
- `dashboard_completo.png` - Visão geral integrada
- `inversao_genero_gestao.png` - Docência vs gestão (reenquadrado)
- `resumo_executivo.csv` - Métricas principais

### 🔍 Descoberta Chave (v2.1):

**A GESTÃO ESPELHA A FEMINIZAÇÃO DA DOCÊNCIA (IFR 1.05x)**

As mulheres são maioria na gestão (79.5%) — mas o comparativo correto é com
a docência (75.8% mulheres), base de recrutamento da gestão. A exceção é a
rede Federal (IFR 0.65x), explicada pela docência federal majoritariamente
masculina (40.3%) — única do país. O caso mais forte de barreira real:
Amazonas (IFR 0.80x, gestão 49.7% vs docência 62.3%).

### 🚀 Recomendações para Pesquisa:

1. Investigar por que a DOCÊNCIA federal é majoritariamente masculina
2. Estudo de caso: gestão feminina no Amazonas
3. Analisar como o IFR varia com recorte racial
4. Comparar com dados de outros anos para identificar tendências

---

✨ **Notebook 04 (e projeto) concluído!** ✨

**Desenvolvido com ❤️ por Sara**"""

nbformat.write(nb, NB)
print('Notebook 04 atualizado. Executando...')

client = NotebookClient(nb, timeout=590, kernel_name='python3',
                        resources={'metadata': {'path': 'notebooks'}})
client.execute()
nbformat.write(nb, NB)
print('✅ Notebook 04 executado e salvo.')