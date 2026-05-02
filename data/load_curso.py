import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular, Docente

# Abrir o ficheiro JSON
with open('data/files/ULHT260-PT.json', encoding='utf-8') as f:
    dados = json.load(f)

detalhe = dados['courseDetail']

# Criar a Licenciatura
licenciatura, _ = Licenciatura.objects.get_or_create(
    nome=detalhe['courseName'],
    defaults={
        'apresentacao': detalhe.get('presentation', ''),
        'competencias': detalhe.get('competences', ''),
        'ects': detalhe.get('courseECTS', 0),
    }
)
print(f"Licenciatura: {licenciatura.nome}")

# Criar os Docentes
for teacher in dados['teachers']:
    nome = teacher.get('academicName') or teacher['fullName']
    Docente.objects.get_or_create(nome=nome)
    print(f"  Docente: {nome}")

# Criar as Unidades Curriculares
for uc in dados['courseFlatPlan']:
    UnidadeCurricular.objects.get_or_create(
        nome=uc['curricularUnitName'],
        defaults={
            'ano': uc['curricularYear'],
            'semestre': uc['semester'],
            'ects': uc['ects'],
            'licenciatura': licenciatura,
        }
    )
    print(f"  UC: {uc['curricularUnitName']}")

print("\nConcluído!")