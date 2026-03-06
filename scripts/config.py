# config.py
# Arquivo de configuração para padronizar o projeto
# Autor: Sara - Análise de Gênero na Educação Básica Brasileira

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "")
OUTPUTS_PATH = os.path.join(BASE_DIR, "outputs", "")
GRAPHICS_PATH = os.path.join(OUTPUTS_PATH, "figures", "")

# Cores para visualizações (paleta sensível ao gênero - evita estereótipos)
CORES = {
    'feminino': '#E67E22',  # laranja (evita rosa/azul)
    'masculino': '#3498DB',  # azul
    'neutro': '#2ECC71',     # verde
    'destaque': '#E74C3C',   # vermelho para chamar atenção
    'total': '#95A5A6'       # cinza para totais
}

# Mapeamento de dependência administrativa
DEPENDENCIA = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Mapeamento de localização
LOCALIZACAO = {
    1: 'Urbana',
    2: 'Rural'
}

# Mapeamento de sexo
SEXO = {
    1: 'Feminino',
    2: 'Masculino',
    0: 'Não declarado'
}

# Mapeamento de etapas de ensino
ETAPAS_ENSINO = {
    1: 'Creche (0-3 anos)',
    2: 'Pré-escola (4-5 anos)',
    3: 'Anos Iniciais do Fundamental (1-5)',
    4: 'Anos Finais do Fundamental (6-9)',
    5: 'Ensino Médio',
    6: 'EJA',
    7: 'Educação Especial',
    8: 'Educação Profissional'
}

# Configurações de visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette([CORES['feminino'], CORES['masculino']])
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10

# Criar diretórios se não existirem
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
os.makedirs(GRAPHICS_PATH, exist_ok=True)

print(f"✅ Configurações carregadas!")
print(f"📁 Dados brutos: {RAW_DATA_PATH}")
print(f"📁 Dados processados: {PROCESSED_DATA_PATH}")
print(f"📁 Gráficos: {GRAPHICS_PATH}")
