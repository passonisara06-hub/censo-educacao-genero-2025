# -*- coding: utf-8 -*-
"""Executa o notebook 03 (já com capítulo 7 injetado) e salva com saídas."""
import nbformat
from nbclient import NotebookClient

NB = 'notebooks/03_analise_gestao_escolar.ipynb'
nb = nbformat.read(NB, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3',
                        resources={'metadata': {'path': 'notebooks'}})
client.execute()
nbformat.write(nb, NB)
print('✅ Notebook 03 executado e salvo com saídas.')