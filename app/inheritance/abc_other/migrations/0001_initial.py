# Generated by Django 2.2 on 2019-04-10 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abstract_base_classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abc_other_photopost_set', related_query_name='abc_other_photopost', to='abstract_base_classes.RelatedUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
