# Generated by Django 3.2.4 on 2021-08-30 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(blank=True, choices=[('pe', 'PE'), ('df', 'DF'), ('ma', 'MA'), ('pb', 'PB'), ('rr', 'RR'), ('ce', 'CA'), ('al', 'AL'), ('mg', 'MG'), ('go', 'GO'), ('es', 'ES'), ('pa', 'PA'), ('to', 'TO'), ('rj', 'RJ'), ('am', 'AM'), ('pr', 'PR'), ('rn', 'RN'), ('ba', 'BA'), ('ap', 'AP'), ('mt', 'MT'), ('se', 'SE'), ('rs', 'RS'), ('sc', 'SC'), ('ac', 'AC'), ('ms', 'MS'), ('ro', 'RO'), ('sp', 'SP')], max_length=2),
        ),
        migrations.AlterField(
            model_name='statusdebaixa',
            name='motivo',
            field=models.CharField(choices=[('extravio', 'Extravio'), ('obsolescência', 'Obsolescência'), ('imprestabilidade', 'Imprestabilidade'), ('desuso', 'Desuso'), ('alienação', 'Alienação'), ('transferência', 'Transferência'), ('consumo', 'Consumo'), ('dano', 'Dano')], default='Imprestabilidade', max_length=20),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='operadora',
            field=models.CharField(choices=[('claro', 'Claro'), ('vivo', 'Vivo'), ('tim', 'Tim'), ('oi', 'OI')], max_length=20),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('celular', 'Celular'), ('fixo', 'Fixo')], max_length=20),
        ),
    ]
