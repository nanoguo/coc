# Generated by Django 4.1.3 on 2022-11-21 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClanMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(db_index=True, max_length=15, unique=True)),
                ('name', models.CharField(max_length=63)),
                ('in_clan', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'clan_members',
            },
        ),
        migrations.CreateModel(
            name='UserInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(max_length=10, verbose_name='角色')),
                ('capital_contributions', models.IntegerField(default=0, verbose_name='当前总贡献')),
                ('date', models.CharField(max_length=6, verbose_name='年月')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.clanmembers')),
            ],
            options={
                'db_table': 'users_info',
            },
        ),
        migrations.CreateModel(
            name='CapitalLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('attacks', models.SmallIntegerField(default=0)),
                ('capital_resource_looted', models.IntegerField(default=0, verbose_name='每周进攻获取')),
                ('date', models.CharField(max_length=6, verbose_name='年月')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.clanmembers')),
            ],
            options={
                'db_table': 'capital_attack_logs',
            },
        ),
        migrations.CreateModel(
            name='CapitalCalculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('delta', models.IntegerField(default=0, verbose_name='当月实际贡献')),
                ('date', models.CharField(max_length=6, verbose_name='年月')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.clanmembers')),
            ],
            options={
                'db_table': 'capital_calculate',
            },
        ),
    ]