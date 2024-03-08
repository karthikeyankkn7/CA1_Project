# Generated by Django 3.0.8 on 2021-03-25 17:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moneyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200, null=True)),
                ('Bill_Date', models.DateField(auto_now_add=True, null=True)),
                ('no_of_splits', models.IntegerField(null=True)),
                ('split_members', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), size=None), size=None)),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.IntegerField(null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moneyapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Split',
            fields=[
                ('split_id', models.AutoField(primary_key=True, serialize=False)),
                ('split_amount', models.IntegerField(null=True)),
                ('reciept_paid', models.BooleanField(default=False)),
                ('expense_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moneyapp.Expense')),
                ('reciept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moneyapp.Customer')),
            ],
        ),
    ]