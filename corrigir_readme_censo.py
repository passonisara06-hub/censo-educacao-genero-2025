#!/usr/bin/env python3
"""Corrige erros verificáveis no repositório censo-educacao-genero-2025.

Três problemas, todos conferidos antes de mexer:

1. **DOI falso.** O README traz o badge `10.5281/zenodo.XXXXXXX` — placeholder de
   template, nunca foi DOI real. DOI inexistente em repositório público é erro
   verificável: quem clicar recebe 404. Removido.
2. **Titulação errada.** "Mestra em Educação" não é o título dela. O diploma
   (IFES) diz *Mestrado Profissional em Ensino de Humanidades*. A forma errada
   aparecia no README, em outputs/, em scripts/ e em notebooks/.
3. **Estrutura do projeto descrita errada** no README: listava `1_dados/`,
   `2_notebooks/`, `3_outputs/`, `4_scripts/` e uma pasta `docs/` que não
   existem. O repositório real usa `data/`, `notebooks/`, `outputs/`, `scripts/`.

Também remove `README (2).md`, duplicata byte-a-byte de `README.md`.

Uso:
    python3 corrigir_readme_censo.py --aplicar
    python3 corrigir_readme_censo.py            # dry-run (só mostra o que mudaria)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# Ordem importa: padrões mais longos primeiro, senão o curto come antes.
TROCAS = [
    ("Sara - Mestra em Educação",
     "Sara Abreu Passoni - Mestra em Ensino de Humanidades (IFES)"),
    ("Mestra em Educação | Análise de Dados Educacionais",
     "Mestra em Ensino de Humanidades (IFES) | Análise de Dados Educacionais"),
    ("Mestra em Educação", "Mestra em Ensino de Humanidades (IFES)"),
]

# Linha do badge DOI falso — removida inteira.
DOI_FALSO = re.compile(
    r"^\[!\[DOI\]\(https://zenodo\.org/badge/DOI/10\.5281/zenodo\.XXXXXXX\.svg\)\]"
    r"\(https://doi\.org/10\.5281/zenodo\.XXXXXXX\)\s*$\n?",
    re.MULTILINE,
)

ESTRUTURA_RE = re.compile(
    r"censo_genero_2025/.*?README\.md\s*#\s*Este arquivo",
    re.DOTALL,
)

ESTRUTURA_CORRETA = """```
censo-educacao-genero-2025/
├── data/                          # Dados do INEP (não versionados)
├── notebooks/                     # Análises em Jupyter Notebook
│   ├── 01_carregamento_e_limpeza.ipynb
│   ├── 02_analise_matriculas_por_genero.ipynb
│   ├── 03_analise_gestao_escolar.ipynb
│   ├── 04_sintese_e_visualizacoes.ipynb
│   ├── 05_analise_interseccional.ipynb
│   └── 06_funil_e_rigor.ipynb
├── outputs/                       # Resultados gerados
│   ├── figures/                   # Gráficos em PNG
│   ├── relatorio_sintese.md       # Relatório completo
│   ├── apresentacao_resultados.md # Apresentação executiva
│   ├── resumo_executivo.csv       # Métricas principais
│   └── *_guia_dashboard.md        # Guias de Tableau e Power BI
├── scripts/                       # Códigos auxiliares
│   └── config.py                  # Configurações e cores
├── requirements.txt               # Dependências
└── README.md                      # Este arquivo
```"""


def arquivos_alvo() -> list[Path]:
    """Tudo que é texto versionado e pode conter os erros."""
    exts = {".md", ".py", ".ipynb", ".txt", ".sh"}
    ignorar = {".git", "venv", ".venv", ".ipynb_checkpoints", "data", "__pycache__"}
    achados = []
    for p in RAIZ.rglob("*"):
        if not p.is_file() or p.suffix not in exts:
            continue
        if any(part in ignorar for part in p.parts):
            continue
        # NUNCA editar este script: ele contém os próprios termos de busca.
        if p.name == Path(__file__).name:
            continue
        achados.append(p)
    return sorted(achados)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true", help="grava as mudanças")
    a = ap.parse_args()

    mudancas: list[tuple[Path, list[str]]] = []

    for arq in arquivos_alvo():
        original = arq.read_text(encoding="utf-8")
        texto = original
        notas: list[str] = []

        # 1) DOI falso
        novo, n = DOI_FALSO.subn("", texto)
        if n:
            texto = novo
            notas.append(f"removeu badge de DOI falso ({n}x)")

        # 2) estrutura incorreta (só no README)
        if arq.name.startswith("README"):
            texto, n = ESTRUTURA_RE.subn(ESTRUTURA_CORRETA, texto, count=1)
            if n:
                notas.append("corrigiu a árvore de pastas (não correspondia ao repositório)")

        # 3) titulação
        for antigo, novo_txt in TROCAS:
            if antigo in texto:
                c = texto.count(antigo)
                texto = texto.replace(antigo, novo_txt)
                notas.append(f"titulação: {c}x “{antigo}” → “{novo_txt}”")

        if texto != original:
            # .ipynb precisa continuar sendo JSON válido
            if arq.suffix == ".ipynb":
                try:
                    json.loads(texto)
                except json.JSONDecodeError as e:
                    print(f"  ! {arq.name}: a edição quebraria o JSON ({e}) — PULADO",
                          file=sys.stderr)
                    continue
            mudancas.append((arq, notas))
            if a.aplicar:
                arq.write_text(texto, encoding="utf-8")

    if not mudancas:
        print("Nada a corrigir — nenhum erro encontrado.")
        return 0

    print(("APLICADO" if a.aplicar else "DRY-RUN — nada foi gravado") + ":\n")
    for arq, notas in mudancas:
        print(f"  {arq.relative_to(RAIZ)}")
        for n in notas:
            print(f"      • {n}")

    # duplicata
    dup = RAIZ / "README (2).md"
    if dup.exists():
        print(f"\n  {dup.name}: duplicata byte-a-byte de README.md")
        if a.aplicar:
            dup.unlink()
            print("      • arquivo removido (usar `git rm` para tirar do versionamento)")

    print(f"\n{len(mudancas)} arquivo(s) afetado(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
