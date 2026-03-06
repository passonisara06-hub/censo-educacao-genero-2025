#!/bin/bash

# Script de configuração do ambiente Python para o projeto
# Uso: bash setup.sh

echo "🔹 Atualizando pacotes do sistema..."
sudo apt update

echo "🔹 Instalando python3-venv e pip (se necessário)..."
sudo apt install -y python3-venv python3-pip

echo "🔹 Criando ambiente virtual..."
python3 -m venv venv

echo "🔹 Ativando ambiente virtual..."
source venv/bin/activate

echo "🔹 Instalando dependências do projeto..."
pip install --upgrade pip
pip install pandas numpy dask scikit-learn seaborn matplotlib plotly geopandas folium notebook

echo "✅ Ambiente configurado com sucesso!"
echo "Para ativar o ambiente em novas sessões, use:"
echo "source venv/bin/activate"
echo "E para rodar o notebook, use:"
echo "jupyter notebook"