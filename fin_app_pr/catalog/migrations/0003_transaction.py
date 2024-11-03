# Generated by Django 5.1.1 on 2024-10-19 13:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_id_budget'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('transaction_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]