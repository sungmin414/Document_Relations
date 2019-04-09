# Generated by Django 2.2 on 2019-04-09 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_base_classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_base_classes_photopost_set', related_query_name='abstract_base_classes_photopost', to='inheritance.abstract_base_classes.RelatedUser'),
        ),
        migrations.AlterField(
            model_name='textpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_base_classes_textpost_set', related_query_name='abstract_base_classes_textpost', to='inheritance.abstract_base_classes.RelatedUser'),
        ),
    ]
