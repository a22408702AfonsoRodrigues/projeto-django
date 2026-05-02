import json
import sys
import os

# Configurar o Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from portfolio.models import TFC, Docente, Tecnologia

# Abrir o ficheiro JSON
with open('data/tfcs_2024_2025.json', encoding='utf-8') as f:
    dados = json.load(f)

for entrada in dados:
    # Criar ou obter o orientador
    nome_orientador = entrada['orientadores'].split('Mestrado')[0].split('Doutoramento')[0].strip().rstrip(',')
    orientador, _ = Docente.objects.get_or_create(nome=nome_orientador)

    # Criar o TFC
    tfc = TFC.objects.create(
        titulo=entrada['titulo'],
        autores=entrada['autor'],
        orientador=orientador,
        sumario=entrada['sumario'],
        classificacao=entrada['rating'],
    )

    # Adicionar tecnologias
    for nome_tec in entrada['tecnologias'].split(';'):
        nome_tec = nome_tec.strip().rstrip('.')
        if nome_tec:
            tec, _ = Tecnologia.objects.get_or_create(nome=nome_tec)
            tfc.tecnologias.add(tec)

print("TFCs carregados com sucesso!")