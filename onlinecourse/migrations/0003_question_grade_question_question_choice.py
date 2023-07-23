from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
    ]