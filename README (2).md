# 👩‍🏫 Análise de Gênero na Educação Básica Brasileira
## Censo Escolar 2025 - INEP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

---

## 📌 **Sobre o Projeto**

Este repositório contém uma análise exploratória dos microdados do **Censo Escolar 2025** (INEP), com foco em **desigualdades de gênero** na educação básica brasileira. A pesquisa investiga tanto a distribuição de **matrículas** por gênero quanto a **composição da gestão escolar**, revelando padrões contraintuitivos que desafiam narrativas tradicionais sobre o "teto de vidro" na educação.

**Autora:** Sara - Mestra em Educação  
**Áreas:** Educação, Gênero, Análise de Dados, Políticas Públicas  
**Fonte dos dados:** [INEP - Microdados do Censo Escolar 2025](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

---

## 🔍 **Principais Descobertas**

### 📊 **Parte 1 - Panorama Geral e Gestão Escolar**

| Descoberta | Resultado | Interpretação |
|------------|-----------|---------------|
| Paridade de gênero nas salas de aula | 49.4% meninas, 50.6% meninos | Diferença pequena (<1%), relevância prática limitada |
| **Inversão de gênero na gestão** | **79.5% gestoras** | Mulheres **1.61x mais representadas** na gestão que nas salas de aula |
| **Exceção Federal** | **26.3% gestoras** | Rede Federal foge ao padrão - "teto de vidro" em contextos de maior prestígio |
| Disparidade regional na gestão | 63.9% (Norte) vs 85.8% (Sul) | Variação de **21.9 pontos percentuais** |
| Urbano vs Rural | 82.6% (urbano) vs 71.4% (rural) | Diferença de **11.2 pp** |

### 📈 **Métricas Avançadas**

- **Índice de Representação Feminina:** 1.61x
- **Correlação porte da escola vs % gestoras:** ~0.0 (não significativa)
- **Intervalo de Confiança (95%):** [79.47%, 79.53%] - alta precisão

---

## 🗂️ **Estrutura do Projeto**


censo_genero_2025/

│

├── 1_dados/                      # Dados brutos (não versionados)

│   └── (arquivos do INEP)

│

├── 2_notebooks/                   # Análises em Jupyter

│   ├── 01_carregamento_e_limpeza.ipynb

│   ├── 02_analise_matriculas_por_genero.ipynb

│   ├── 03_analise_gestao_escolar.ipynb

│   └── 04_sintese_e_visualizacoes.ipynb

│

├── 3_outputs/                     # Resultados gerados

│   ├── figures/                   # Gráficos em PNG

│   └── resumo_executivo.csv       # Métricas principais

│

├── 4_scripts/                      # Códigos auxiliares

│   └── config.py                   # Configurações e cores

│

├── docs/                           # Documentação

│   ├── apresentacao_resultados.md  # Apresentação executiva

│   └── relatorio_sintese.md        # Relatório completo

│

├── requirements.txt                # Dependências

├── LICENSE                         # Licença MIT

└── README.md                        # Este arquivo


---

## 🚀 **Como Executar**

### Pré-requisitos
- Python 3.12+
- Jupyter Notebook
- Dados do Censo Escolar 2025 ([download](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar))

### Instalação

```bash
# Clone o repositório
git clone https://github.com/passonisara06-hub/censo-educacao-genero-2025.git
cd censo-genero-2025

# Crie e ative ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Instale dependências
pip install -r requirements.txt

# Coloque os dados na pasta 1_dados/
# Execute os notebooks em ordem
```

---

## 📊 **Visualizações**

| Gráfico | Descrição |
|---------|-----------|
| `01_distribuicao_nacional.png` | Matrículas por gênero |
| `02_genero_por_rede.png` | Matrículas por rede de ensino |
| `03_meninas_por_regiao.png` | Proporção de meninas por região |
| `04_genero_gestores.png` | Gestores por gênero |
| `05_gestoras_por_rede.png` | Gestoras por rede |
| `06_gestoras_por_regiao.png` | Gestoras por região |
| `07_alunas_vs_gestoras.png` | Comparação alunas vs gestoras |
| `dashboard_completo.png` | Dashboard integrado |
| `inversao_genero_gestao.png` | Visualização da descoberta principal |

---

## 🧪 **Metodologia e Testes Estatísticos**

| Teste | Aplicação | Resultado |
|-------|-----------|-----------|
| Qui-quadrado | Comparação matrículas por gênero | p < 0.001 (significativo) |
| Shapiro-Wilk | Normalidade da distribuição | p < 0.05 (não-normal) |
| Correlação de Pearson | Porte da escola vs % gestoras | ~0.0 (não significativa) |
| Intervalo de Confiança (95%) | Precisão da estimativa de % gestoras | ±0.03 pp |

---

## ⚠️ **Limitações e Próximos Passos**

### **Parte 1 (Atual)**
- [x] Dados binários de gênero (masculino/feminino)
- [x] Dados agregados por escola (não individuais)
- [x] Ausência de recorte racial

### **Parte 2 (Em desenvolvimento)**
- [ ] Cruzamento com dados de raça/cor
- [ ] Análise temporal (comparação com censos anteriores)
- [ ] Investigação qualitativa da rede Federal
- [ ] Dados salariais de gestores (se disponíveis)

---

## 📚 **Como Citar**

```bibtex
@misc{sara2026generoeducacao,
  author = {Sara},
  title = {Análise de Gênero na Educação Básica Brasileira: Censo Escolar 2025},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/passonisara06-hub/censo-educacao-genero-2025}}
}
```

---

## 🤝 **Contribuições**

Contribuições são bem-vindas! Especialmente nas áreas:
- ✅ Análise com recorte racial
- ✅ Modelagem preditiva
- ✅ Dashboard interativo (Plotly/Dash)
- ✅ Tradução para outros idiomas

Por favor, abra uma issue antes de enviar um pull request.

---

## 📄 **Licença**

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 📬 **Contato**

**Autora:** Sara  
**E-mail:** [passonisara06@gmail.com]  


**Dúvidas ou sugestões?** Fique à vontade para abrir uma issue!

---

**Parte 1 de uma série em andamento** 🔄  
*Análise atualizada em: Março de 2026*
```
