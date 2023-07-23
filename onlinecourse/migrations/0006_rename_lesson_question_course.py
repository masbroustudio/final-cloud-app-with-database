from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_alter_choice_choice_alter_question_lesson_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
    ]