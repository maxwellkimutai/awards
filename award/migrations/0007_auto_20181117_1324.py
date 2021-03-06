# Generated by Django 2.0 on 2018-11-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0006_project_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='award.Profile'),
        ),
        migrations.AddField(
            model_name='vote',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='award.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='profile_projects', to='award.Project'),
        ),
    ]
