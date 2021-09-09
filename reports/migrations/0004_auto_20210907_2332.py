# Generated by Django 3.2.6 on 2021-09-08 02:32

import autoslug.fields
from django.db import migrations, models
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20210907_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='escola',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='designacao', slugify=reports.models.hifenization, unique=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(blank=True, choices=[('ba', 'BA'), ('pr', 'PR'), ('ap', 'AP'), ('rs', 'RS'), ('to', 'TO'), ('ro', 'RO'), ('ce', 'CA'), ('al', 'AL'), ('am', 'AM'), ('rr', 'RR'), ('pa', 'PA'), ('es', 'ES'), ('sp', 'SP'), ('mg', 'MG'), ('go', 'GO'), ('rj', 'RJ'), ('ac', 'AC'), ('sc', 'SC'), ('mt', 'MT'), ('ma', 'MA'), ('pe', 'PE'), ('rn', 'RN'), ('ms', 'MS'), ('df', 'DF'), ('se', 'SE'), ('pb', 'PB')], max_length=2),
        ),
        migrations.AlterField(
            model_name='statusdebaixa',
            name='motivo',
            field=models.CharField(choices=[('desuso', 'Desuso'), ('alienação', 'Alienação'), ('imprestabilidade', 'Imprestabilidade'), ('extravio', 'Extravio'), ('consumo', 'Consumo'), ('dano', 'Dano'), ('transferência', 'Transferência'), ('obsolescência', 'Obsolescência')], default='Imprestabilidade', max_length=20),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(choices=[('residencial', 'Residencial'), ('fixo', 'Fixo'), ('comercial', 'Comercial'), ('celular', 'Celular')], max_length=20),
        ),
    ]
