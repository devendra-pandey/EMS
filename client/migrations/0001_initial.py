# Generated by Django 3.1.2 on 2020-11-13 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=30, null=True)),
                ('linkedln_profile', models.CharField(blank=True, max_length=500, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=12, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default='1')),
            ],
            options={
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Company_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('project_type', models.CharField(choices=[('Android', 'Android'), ('Ecommerce', 'Ecommerce'), ('ERP', 'ERP'), ('CMS', 'CMS'), ('Webapp', 'webapp'), ('Desktop_App', 'Desktop_App')], max_length=50)),
                ('project_files', models.FileField(blank=True, null=True, upload_to='static/Uploads/projects/')),
                ('advance_amount', models.IntegerField(default=0)),
                ('received_amount', models.IntegerField(default=0)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default='0')),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=10)),
                ('tax_value', models.IntegerField()),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Total_expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('total', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Project_income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('received_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer')], max_length=50)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('company_received_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.company_profile')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('actual_end_date', models.DateField()),
                ('completed', models.BooleanField(default='0')),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('employe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_income_id', models.IntegerField(unique=True)),
                ('payment_method', models.CharField(max_length=50)),
                ('amount_received', models.IntegerField(default='0')),
                ('tax', models.IntegerField(default='18')),
                ('discount', models.FloatField(default='10.0')),
                ('total_amount', models.IntegerField(default='0')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('by_company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.company_profile')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project')),
            ],
        ),
        migrations.CreateModel(
            name='Followup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(blank=True, max_length=10000, null=True)),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Extra_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.CharField(blank=True, max_length=100, null=True)),
                ('expense_amount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_date', models.DateField()),
                ('proposal_file', models.FileField(null=True, upload_to='static/Uploads/proposals/')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
