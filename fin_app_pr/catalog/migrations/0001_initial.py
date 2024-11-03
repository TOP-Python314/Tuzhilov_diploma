# Generated by Django 5.1.1 on 2024-10-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('products', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('lunch', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('cloth', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('sport', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('petrol', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('service', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('home', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('leisure', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('mobile', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('internet', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]
