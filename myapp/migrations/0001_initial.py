# Generated by Django 5.1.6 on 2025-02-13 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='exam_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='institution_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('institution_address', models.CharField(blank=True, max_length=100, null=True)),
                ('institution_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('institution_email', models.CharField(blank=True, max_length=100, null=True)),
                ('institution_accreditation', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('user_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='course_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('course_code', models.CharField(blank=True, max_length=100, null=True)),
                ('course_credit', models.CharField(blank=True, max_length=100, null=True)),
                ('dep_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.department_model')),
            ],
        ),
        migrations.CreateModel(
            name='faculty_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(blank=True, max_length=100, null=True)),
                ('faculty_name', models.CharField(blank=True, max_length=100, null=True)),
                ('faculty_email', models.CharField(blank=True, max_length=100, null=True)),
                ('faculty_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('faculty_address', models.CharField(blank=True, max_length=100, null=True)),
                ('dep_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.department_model')),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.login_model')),
            ],
        ),
        migrations.AddField(
            model_name='department_model',
            name='institution_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.institution_model'),
        ),
        migrations.CreateModel(
            name='semester_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(blank=True, max_length=100, null=True)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course_model')),
            ],
        ),
        migrations.CreateModel(
            name='student_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addmission_number', models.CharField(blank=True, max_length=100, null=True)),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_email', models.CharField(blank=True, max_length=100, null=True)),
                ('student_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('student_address', models.CharField(blank=True, max_length=100, null=True)),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.login_model')),
                ('institution_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.institution_model')),
            ],
        ),
        migrations.CreateModel(
            name='mark_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.exam_model')),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.faculty_model')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.student_model')),
            ],
        ),
        migrations.CreateModel(
            name='Grievances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grievance', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.faculty_model')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.student_model')),
            ],
        ),
        migrations.CreateModel(
            name='subject_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_credit', models.CharField(blank=True, max_length=100, null=True)),
                ('sem_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.semester_model')),
            ],
        ),
        migrations.AddField(
            model_name='exam_model',
            name='subject_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subject_model'),
        ),
    ]
