# Generated by Django 3.2.9 on 2021-11-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dailywork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=25, null=True)),
                ('currentdate', models.DateField()),
                ('hour1', models.CharField(max_length=200)),
                ('hour2', models.CharField(max_length=200)),
                ('hour3', models.CharField(max_length=200)),
                ('hour4', models.CharField(max_length=200)),
                ('hour5', models.CharField(max_length=200)),
                ('hour6', models.CharField(max_length=200)),
                ('hour7', models.CharField(max_length=200)),
                ('hour8', models.CharField(max_length=200)),
                ('r1', models.CharField(max_length=200)),
                ('r2', models.CharField(max_length=200)),
                ('r3', models.CharField(max_length=200)),
                ('r4', models.CharField(max_length=200)),
                ('r5', models.CharField(max_length=200)),
                ('r6', models.CharField(max_length=200)),
                ('r7', models.CharField(max_length=200)),
                ('r8', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='emailus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=14)),
                ('designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('empid', models.CharField(max_length=20)),
                ('psw', models.CharField(max_length=20)),
                ('cpsw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='suser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
