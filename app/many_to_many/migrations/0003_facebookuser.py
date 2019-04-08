# Generated by Django 2.2 on 2019-04-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_auto_20190408_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(related_name='_facebookuser_friends_+', to='many_to_many.FacebookUser')),
            ],
        ),
    ]
