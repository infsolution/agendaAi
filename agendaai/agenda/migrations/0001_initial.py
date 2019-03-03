# Generated by Django 2.1.7 on 2019-03-03 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=5)),
                ('district', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200, null=True)),
                ('zip_code', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=512, null=True)),
                ('realizado', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('site', models.CharField(max_length=200, null=True)),
                ('cnpj', models.CharField(max_length=20)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address', to='agenda.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=29)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init', models.CharField(max_length=5)),
                ('end', models.CharField(max_length=5)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day', to='agenda.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profession', to='agenda.Profession')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professional', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='agenda.Category'),
        ),
        migrations.AddField(
            model_name='business',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agenda',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimento', to='agenda.Atendimento'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horario', to='agenda.Horario'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='agenda.Professional'),
        ),
    ]
