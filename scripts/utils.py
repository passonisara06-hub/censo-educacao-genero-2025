# utils.py
# Funções auxiliares para o projeto
# Autor: Sara - Análise de Gênero na Educação Básica Brasileira

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from config import CORES, SEXO, DEPENDENCIA

def carregar_dados_otimizado(caminho_arquivo, colunas=None, chunksize=None):
    """
    Carrega dados CSV de forma otimizada para grandes arquivos.

    Parâmetros:
    -----------
    caminho_arquivo : str
        Caminho completo para o arquivo CSV
    colunas : list, opcional
        Lista de colunas para carregar. Se None, carrega todas.
    chunksize : int, opcional
        Tamanho do chunk para leitura em partes

    Retorna:
    --------
    pd.DataFrame
        DataFrame com os dados carregados
    """
    try:
        if colunas:
            df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1',
                            usecols=colunas, low_memory=False)
        else:
            df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1',
                            low_memory=False)
        return df
    except Exception as e:
        print(f"❌ Erro ao carregar {caminho_arquivo}: {e}")
        return None


def calcular_porcentagem(df, coluna_valor, coluna_grupo):
    """
    Calcula porcentagens agrupadas por uma coluna.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    coluna_valor : str
        Coluna de valores (1/0 para contagem)
    coluna_grupo : str
        Coluna para agrupar

    Retorna:
    --------
    pd.DataFrame
        DataFrame com porcentagens calculadas
    """
    df_grouped = df.groupby(coluna_grupo)[coluna_valor].agg(['sum', 'count'])
    df_grouped['porcentagem'] = (df_grouped['sum'] / df_grouped['count']) * 100
    return df_grouped


def criar_grafico_barras_comparativo(dados, x, y, hue, titulo,
                                     xlabel='', ylabel='Porcentagem (%)',
                                     salvar_caminho=None):
    """
    Cria um gráfico de barras comparativo com cores sensíveis a gênero.

    Parâmetros:
    -----------
    dados : pd.DataFrame
        DataFrame com os dados
    x, y, hue : str
        Colunas para eixos x, y e agrupamento
    titulo : str
        Título do gráfico
    xlabel, ylabel : str
        Labels dos eixos
    salvar_caminho : str, opcional
        Caminho para salvar o gráfico
    """
    plt.figure(figsize=(12, 6))

    ax = sns.barplot(data=dados, x=x, y=y, hue=hue,
                     palette=[CORES['feminino'], CORES['masculino']])

    plt.title(titulo, fontweight='bold', pad=20)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.legend(title='Gênero', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Adicionar valores nas barras
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.1f}%',
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center', xytext=(0, 5),
                   textcoords='offset points', fontsize=9)

    if salvar_caminho:
        plt.savefig(salvar_caminho, dpi=300, bbox_inches='tight')
        print(f"💾 Gráfico salvo: {salvar_caminho}")

    plt.show()


def criar_grafico_pizza(dados, labels, valores, titulo, cores=None,
                        salvar_caminho=None):
    """
    Cria um gráfico de pizza com cores personalizadas.

    Parâmetros:
    -----------
    dados : pd.DataFrame
        DataFrame com os dados
    labels : list
        Labels para as fatias
    valores : str
        Coluna com os valores
    titulo : str
        Título do gráfico
    cores : list, opcional
        Lista de cores
    salvar_caminho : str, opcional
        Caminho para salvar o gráfico
    """
    if cores is None:
        cores = [CORES['feminino'], CORES['masculino'], CORES['neutro']]

    plt.figure(figsize=(10, 8))
    values = dados[valores]

    plt.pie(values, labels=labels, colors=cores, autopct='%1.1f%%',
            startangle=90, textprops={'fontsize': 12})
    plt.title(titulo, fontweight='bold', pad=20, fontsize=14)
    plt.axis('equal')

    if salvar_caminho:
        plt.savefig(salvar_caminho, dpi=300, bbox_inches='tight')
        print(f"💾 Gráfico salvo: {salvar_caminho}")

    plt.show()


def criar_grafico_funil(dados, etapas, titulo, salvar_caminho=None):
    """
    Cria um gráfico de funil mostrando a proporção de meninas em cada etapa.

    Parâmetros:
    -----------
    dados : pd.DataFrame
        DataFrame com os dados
    etapas : dict
        Dicionário com nome da etapa e códigos correspondentes
    titulo : str
        Título do gráfico
    salvar_caminho : str, opcional
        Caminho para salvar o gráfico
    """
    plt.figure(figsize=(10, 6))

    porcentagens = []
    nomes_etapas = list(etapas.keys())

    for etapa in nomes_etapas:
        # Filtrar dados da etapa
        df_etapa = dados[dados['TP_ETAPA_ENSINO'].isin(etapas[etapa])]
        total = len(df_etapa)
        mulheres = len(df_etapa[df_etapa['TP_SEXO'] == 1])
        pct = (mulheres / total * 100) if total > 0 else 0
        porcentagens.append(pct)

    # Criar gráfico de barras horizontais
    bars = plt.barh(nomes_etapas, porcentagens, color=CORES['feminino'])

    plt.title(titulo, fontweight='bold', pad=20)
    plt.xlabel('Porcentagem de Meninas (%)', fontsize=12)
    plt.xlim(0, 100)
    plt.grid(axis='x', alpha=0.3)

    # Adicionar valores nas barras
    for bar, pct in zip(bars, porcentagens):
        plt.text(pct + 1, bar.get_y() + bar.get_height()/2,
                f'{pct:.1f}%', va='center', fontsize=11, fontweight='bold')

    plt.tight_layout()

    if salvar_caminho:
        plt.savefig(salvar_caminho, dpi=300, bbox_inches='tight')
        print(f"💾 Gráfico salvo: {salvar_caminho}")

    plt.show()


def resumo_estatistico(df, coluna_grupo, coluna_valor):
    """
    Gera um resumo estatístico por grupo.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    coluna_grupo : str
        Coluna para agrupar
    coluna_valor : str
        Coluna de valores

    Retorna:
    --------
    pd.DataFrame
        DataFrame com resumo estatístico
    """
    resumo = df.groupby(coluna_grupo)[coluna_valor].agg([
        ('Contagem', 'count'),
        ('Média', 'mean'),
        ('Mediana', 'median'),
        ('Desvio_Padrão', 'std'),
        ('Mínimo', 'min'),
        ('Máximo', 'max')
    ]).round(2)

    return resumo


def formatar_numero(valor, unidade=''):
    """
    Formata números para exibição (milhares, milhões).

    Parâmetros:
    -----------
    valor : float ou int
        Valor a formatar
    unidade : str
        Unidade de medida

    Retorna:
    --------
    str
        Valor formatado
    """
    if valor >= 1_000_000:
        return f"{valor/1_000_000:.1f}M {unidade}"
    elif valor >= 1_000:
        return f"{valor/1_000:.1f}K {unidade}"
    else:
        return f"{valor} {unidade}"


print("✅ Funções auxiliares carregadas!")
