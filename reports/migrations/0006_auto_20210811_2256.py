# Generated by Django 3.2.4 on 2021-08-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20210811_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratlaboratorio',
            old_name='foto',
            new_name='fotos',
        ),
        migrations.AlterField(
            model_name='statusdebaixa',
            name='motivo',
            field=models.CharField(choices=[('dano', 'Dano'), ('imprestabilidade', 'Imprestabilidade'), ('transferência', 'Transferência'), ('extravio', 'Extravio'), ('desuso', 'Desuso'), ('consumo', 'Consumo'), ('alienação', 'Alienação'), ('obsolescência', 'Obsolescência')], default='Imprestabilidade', max_length=20),
        ),
    ]