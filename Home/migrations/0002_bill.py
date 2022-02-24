# Generated by Django 3.1.5 on 2021-06-05 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.TimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.property')),
            ],
        ),
    ]