# Generated by Django 3.1.4 on 2021-02-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_auto_20210202_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'CREATE'), (1, 'REQUEST'), (2, 'DESIGN'), (3, 'WRITE'), (4, 'REVIEW'), (5, 'TESTING'), (6, 'DONE'), (7, 'HIDDEN')], default=1),
        ),
        migrations.AlterField(
            model_name='taskupdate',
            name='new_status',
            field=models.IntegerField(choices=[(0, 'CREATE'), (1, 'REQUEST'), (2, 'DESIGN'), (3, 'WRITE'), (4, 'REVIEW'), (5, 'TESTING'), (6, 'DONE'), (7, 'HIDDEN')]),
        ),
        migrations.AlterField(
            model_name='taskupdate',
            name='old_status',
            field=models.IntegerField(choices=[(0, 'CREATE'), (1, 'REQUEST'), (2, 'DESIGN'), (3, 'WRITE'), (4, 'REVIEW'), (5, 'TESTING'), (6, 'DONE'), (7, 'HIDDEN')]),
        ),
    ]