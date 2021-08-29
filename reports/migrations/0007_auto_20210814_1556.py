# Generated by Django 3.2.4 on 2021-08-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20210811_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computador',
            old_name='status',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='escola',
            old_name='status',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='fornecedordeinternet',
            old_name='status',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='linkdeinternet',
            old_name='status',
            new_name='ativo',
        ),
        migrations.AlterField(
            model_name='statusdebaixa',
            name='motivo',
            field=models.CharField(choices=[('consumo', 'Consumo'), ('desuso', 'Desuso'), ('transferência', 'Transferência'), ('alienação', 'Alienação'), ('dano', 'Dano'), ('extravio', 'Extravio'), ('obsolescência', 'Obsolescência'), ('imprestabilidade', 'Imprestabilidade')], default='Imprestabilidade', max_length=20),
        ),
    ]