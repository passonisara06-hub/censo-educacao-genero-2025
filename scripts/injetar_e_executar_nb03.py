# -*- coding: utf-8 -*-
"""
Insere o capítulo 7 (Docência × Gestão — IFR) no notebook 03 e o executa por completo.
"""
import json
import nbformat
from nbclient import NotebookClient

NB = 'notebooks/03_analise_gestao_escolar.ipynb'

nb = nbformat.read(NB, as_version=4)

# Evitar duplicação se rodar de novo
existing_md = [
    ''.join(c.source) for c in nb.cells if c.cell_type == 'markdown'
]
if any('Docência × Gestão' in s for s in existing_md):
    print('Capítulo 7 já existe — nada a inserir.')
else:
    md = nbformat.v4.new_markdown_cell(
"""## 7️⃣ Docência × Gestão: o Índice de Feminização Relativa (IFR)

### 📌 Reenquadramento metodológico

As descobertas acima comparam a gestão com o **alunado**. Mas a gestão escolar recruta a partir
da **docência**: quem chega a diretora é, antes, professora. O comparativo correto é, portanto,
gestão × docência — e a tabela de docentes do Censo (não usada até aqui) permite isso:

$$\\text{IFR} = \\frac{\\%\\ \\text{mulheres na gestão}}{\\%\\ \\text{mulheres na docência}}$$

- **IFR = 1.00** → a gestão espelha a feminização da docência
- **IFR > 1.00** → mulheres sobre-representadas na gestão em relação à base docente
- **IFR < 1.00** → mulheres sub-representadas na gestão (possível barreira de promoção)

O antigo "Índice de Representação 1.61x" dividia % gestoras por % de **alunas** — base errada,
pois os(as) alunos(as) de hoje não são o banco de candidatas à gestão.
"""
    )
    code = nbformat.v4.new_code_cell(
"""# Carregar tabela consolidada gerada por scripts/analise_docentes.py
import sys
sys.path.append('../scripts')
from config import OUTPUTS_PATH

ifr = pd.read_csv(OUTPUTS_PATH + 'indices_feminizacao.csv')
ordem = ['Brasil', 'Federal', 'Estadual', 'Municipal', 'Privada']
ifr['_o'] = ifr['TP_DEPENDENCIA'].apply(lambda x: ordem.index(x) if x in ordem else 9)
ifr = ifr.sort_values('_o').drop(columns='_o')

print("📊 DOCÊNCIA × GESTÃO — Índice de Feminização Relativa")
print("=" * 60)
print("IFR = % mulheres na gestão ÷ % mulheres na docência\\n")
print(ifr[['TP_DEPENDENCIA', 'pct_doc_fem', 'pct_gest_fem', 'ifr']].to_string(index=False))

n_brasil = ifr[ifr['TP_DEPENDENCIA'] == 'Brasil'].iloc[0]
print(f"\\n💡 LEITURA NACIONAL:")
print(f"   • Docência: {n_brasil['pct_doc_fem']:.1f}% mulheres")
print(f"   • Gestão:   {n_brasil['pct_gest_fem']:.1f}% mulheres")
print(f"   • IFR = {n_brasil['ifr']:.2f} → a gestão espelha a feminização da docência.")
print(f"   • O 'Índice de Representação 1.61x' anterior comparava com o ALUNADO")
print(f"     (49.4%); a base de recrutamento da gestão é a DOCÊNCIA (75.8%).")

# --- Gráfico: docentes vs gestoras por rede ---
ordem_plot = ifr[ifr['TP_DEPENDENCIA'] != 'Brasil']
fig, ax = plt.subplots(figsize=(12, 7))
x = np.arange(len(ordem_plot)); w = 0.38
b1 = ax.bar(x - w/2, ordem_plot['pct_doc_fem'], w, label='Docentes (% mulheres)',
            color=CORES['total'], alpha=0.85)
b2 = ax.bar(x + w/2, ordem_plot['pct_gest_fem'], w, label='Gestoras (%)',
            color=CORES['feminino'], alpha=0.9)
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1,
                f'{b.get_height():.1f}%', ha='center', fontsize=10, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(ordem_plot['TP_DEPENDENCIA'])
ax.set_ylim(0, 100)
ax.set_ylabel('Porcentagem de mulheres (%)', fontsize=12)
ax.set_title('Docência × Gestão escolar por rede de ensino\\nCenso Escolar 2025',
             fontweight='bold', pad=15)
ax.legend(loc='upper left'); ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(GRAPHICS_PATH + '08_docencia_vs_gestao.png', dpi=300, bbox_inches='tight')
print("\\n💾 Gráfico salvo: 08_docencia_vs_gestao.png")
plt.show()

# --- Gráfico: IFR por rede ---
fig, ax = plt.subplots(figsize=(12, 6))
cores_ifr = [CORES['destaque'] if v < 1 else CORES['neutro'] for v in ordem_plot['ifr']]
bars = ax.bar(ordem_plot['TP_DEPENDENCIA'], ordem_plot['ifr'], color=cores_ifr, alpha=0.85)
ax.axhline(1.0, color='#555555', linestyle='--', linewidth=1.5)
ax.text(len(ordem_plot) - 0.45, 1.02, 'paridade com a docência (1.00)',
        fontsize=9, color='#555555', ha='right')
for b, v in zip(bars, ordem_plot['ifr']):
    ax.text(b.get_x() + b.get_width()/2, v + 0.015, f'{v:.2f}x',
            ha='center', fontweight='bold', fontsize=11)
ax.set_ylim(0, 1.3)
ax.set_ylabel('Índice de Feminização Relativa\\n(% gestoras ÷ % docentes mulheres)', fontsize=11)
ax.set_title('A gestão espelha a feminização da docência — exceto na rede Federal\\nCenso Escolar 2025',
             fontweight='bold', pad=15)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(GRAPHICS_PATH + '09_ifr_por_rede.png', dpi=300, bbox_inches='tight')
print("💾 Gráfico salvo: 09_ifr_por_rede.png")
plt.show()

# --- Leitura da exceção federal, agora com a base correta ---
fed = ifr[ifr['TP_DEPENDENCIA'] == 'Federal'].iloc[0]
print("\\n🔍 A EXCEÇÃO FEDERAL, RELIDA:")
print("=" * 60)
print(f"   • Docência federal: {fed['pct_doc_fem']:.1f}% mulheres — a ÚNICA rede do")
print(f"     país com docência majoritariamente MASCULINA (institutos federais,")
print(f"     áreas técnicas/STEM, docente do ensino superior compartilhado).")
print(f"   • Gestão federal: {fed['pct_gest_fem']:.1f}% mulheres (n={fed['n_gestores']:,.0f})")
print(f"   • IFR federal = {fed['ifr']:.2f} → a gestão federal é PROPORCIONAL à")
print(f"     base docente da qual recruta (0.65x), não um 'teto de vidro' típico.")
print(f"   • A pergunta de pesquisa muda: não 'por que mulheres não ascemem'")
print(f"     na Federal, mas 'por que a DOCÊNCIA federal é majoritariamente masculina'.")

# --- IFR por UF: onde a gestão fica ABAIXO da docência ---
uf_ifr = pd.read_csv(OUTPUTS_PATH + 'docencia_gestao_por_uf.csv')
print("\\n📍 IFR POR UF — 5 menores (gestão abaixo da docência):")
print(uf_ifr.nsmallest(5, 'ifr')[['SG_UF', 'pct_doc_fem', 'pct_gest_fem', 'ifr', 'n_gestores']].to_string(index=False))
print("\\n📍 IFR POR UF — 5 maiores:")
print(uf_ifr.nlargest(5, 'ifr')[['SG_UF', 'pct_doc_fem', 'pct_gest_fem', 'ifr', 'n_gestores']].to_string(index=False))
am = uf_ifr[uf_ifr['SG_UF'] == 'AM'].iloc[0]
print(f"\\n⚠️ DESTAQUE: Amazonas (IFR {am['ifr']:.2f}) — gestoras {am['pct_gest_fem']:.1f}% vs")
print(f"   docentes {am['pct_doc_fem']:.1f}%. É o caso mais forte de SUB-representação")
print(f"   feminina na gestão do país — candidatos a estudo de caso qualitativo.")
"""
    )
    md2 = nbformat.v4.new_markdown_cell(
"""### 📝 Interpretação

- **Nacional (1.05x):** a gestão escolar brasileira não é uma "inversão" mística — ela
  acompanha a composição da profissão da qual se origina. O teto de vidro clássico
  (docência feminina → gestão masculina) **não aparece no agregado nacional**.
- **Rede Federal (0.65x):** o desvio vem principalmente da **base docente** (40.3% mulheres,
  única rede com docência masculina majoritária). Investigar a gestão federal exige antes
  investigar a composição do magistério federal — contratação, áreas de concurso, STEM.
- **Amazonas (0.80x):** único caso em que a gestão está bem abaixo até da própria base
  docente estadual (49.7% gestoras vs 62.3% docentes) — candidato a estudo de caso.
- **Limitação importante:** a rede Federal tem apenas 754 gestores (0.4% do total); o IFR
  federal carrega incerteza proporcional ao n e não deve ser generalizado sem intervalo
  de confiança.
"""
    )
    # Inserir antes da célula final (Resumo)
    resumo_idx = next(i for i, c in enumerate(nb.cells)
                      if c.cell_type == 'markdown' and 'Resumo do Notebook' in ''.join(c.source))
    nb.cells.insert(resumo_idx, md)
    nb.cells.insert(resumo_idx + 1, code)
    nb.cells.insert(resumo_idx + 2, md2)

    # Atualizar o resumo final do notebook
    for c in nb.cells:
        if c.cell_type == 'markdown' and 'Resumo do Notebook' in ''.join(c.source):
            c.source = c.source.replace(
                '- ✅ Comparação: alunas vs gestoras',
                '- ✅ Comparação: alunas vs gestoras\n- ✅ Docência × gestão (IFR) com a tabela de docentes'
            ).replace(
                '- `07_alunas_vs_gestoras.png`',
                '- `07_alunas_vs_gestoras.png`\n- `08_docencia_vs_gestao.png`\n- `09_ifr_por_rede.png`'
            ).replace(
                '- Mulheres estão mais representadas na gestão que nas salas de aula',
                '- A gestão espelha a docência (IFR 1.05x); a exceção é a Federal (0.65x),\n'
                '  explicada pela docência federal majoritariamente masculina (40.3% mulheres)'
            )

nbformat.write(nb, NB)
print('Células inseridas. Executando notebook inteiro...')

client = NotebookClient(nb, timeout=600, kernel_name='python3',
                        resources={'metadata': {'path': 'notebooks'}})
client.execute()
nbformat.write(nb, NB)
print('✅ Notebook 03 executado e salvo com saídas.')