# Generated by Django 4.2.3 on 2023-07-30 12:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_projects_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('is_to_everyone', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_category_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('first_name', models.CharField(max_length=120)),
                ('middle_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('work_email', models.EmailField(max_length=254)),
                ('work_phone', models.CharField(max_length=120)),
                ('work_location', models.CharField(max_length=120)),
                ('employment_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('employment_status', models.CharField(max_length=120)),
                ('employee_number', models.CharField(max_length=120)),
                ('skills', models.CharField(max_length=120)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.clients')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.company')),
                ('direct_mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_as_direct_mentor', to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('address_1', models.CharField(max_length=120)),
                ('address_2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('nationality', models.CharField(max_length=120)),
                ('home_phone', models.CharField(max_length=120)),
                ('mobile_phone', models.CharField(max_length=120)),
                ('personal_email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=120)),
                ('marital_status', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRolePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=120)),
                ('position_code', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_allocation_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('priority_range', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=120)),
                ('total_hours', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.projects')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_as_reporter', to='database.employee')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_as_resource', to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_status', models.CharField(max_length=120)),
                ('original_estimate', models.IntegerField()),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_as_assignee', to='database.employee')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.taskpriority')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_as_reporter', to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Payslips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_hours', models.IntegerField()),
                ('number_of_days', models.IntegerField()),
                ('status', models.CharField(max_length=120)),
                ('notes', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payslip_as_reporter', to='database.employee')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payslip_as_resource', to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeavePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('allocated_days', models.IntegerField()),
                ('working_hours', models.IntegerField()),
                ('do_carry_over', models.BooleanField(default=False)),
                ('is_shown_in_employee_calender', models.BooleanField(default=False)),
                ('allocated_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.leaveallocation')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.clients')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=120)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_of_days', models.IntegerField()),
                ('approved_status', models.CharField(max_length=120)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
                ('policy_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.leavepolicy')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visa_number', models.CharField(max_length=120)),
                ('visa_type', models.CharField(max_length=120)),
                ('country_of_issue', models.CharField(max_length=120)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('issuing_authority', models.CharField(max_length=120)),
                ('purpose_of_travel', models.CharField(max_length=120)),
                ('remarks', models.CharField(max_length=120)),
                ('attachment', models.FileField(upload_to='')),
                ('current_active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('current_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('employees', models.ManyToManyField(to='database.employee')),
                ('position_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employeerolepolicy')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(max_length=120)),
                ('country_of_issue', models.CharField(max_length=120)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('issuing_authority', models.CharField(max_length=120)),
                ('place_of_birth', models.CharField(max_length=120)),
                ('nationality', models.CharField(max_length=120)),
                ('attachment', models.FileField(upload_to='')),
                ('current_active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=120)),
                ('institution', models.CharField(max_length=120)),
                ('major', models.CharField(max_length=120)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('grade', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('institution', models.CharField(max_length=120)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=120)),
                ('sort_code', models.CharField(max_length=120)),
                ('bank_name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('primary_account', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_personal_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.employeepersonalinfo'),
        ),
        migrations.AddField(
            model_name='employee',
            name='onboarding_mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_as_onboarding_mentor', to='database.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.projects'),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.teams'),
        ),
        migrations.CreateModel(
            name='EmergencyContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('relationship', models.CharField(max_length=120)),
                ('home_phone', models.CharField(max_length=120)),
                ('mobile_phone', models.CharField(max_length=120)),
                ('work_phone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=120)),
                ('address_1', models.CharField(max_length=120)),
                ('address_2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=120)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('asset_number', models.CharField(max_length=120)),
                ('serial_number', models.CharField(max_length=120)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('asset_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.assetcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('attachments', models.FileField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_as_author', to='database.employee')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.clients')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_as_employee', to='database.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.projects')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.teams')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.announcementtopic')),
            ],
        ),
    ]
