# Generated by Django 5.1.4 on 2024-12-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('current_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_relationship', models.CharField(max_length=100)),
                ('emergency_contact_number', models.CharField(max_length=15)),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('employment_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract'), ('IN', 'Intern')], max_length=2)),
                ('work_location', models.CharField(max_length=100)),
                ('reporting_manager', models.CharField(max_length=255)),
                ('highest_qualification', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=255)),
                ('year_of_passing', models.IntegerField()),
                ('certifications', models.TextField(blank=True, null=True)),
                ('bank_account_number', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_branch_address', models.CharField(max_length=255)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('pan_card_number', models.CharField(max_length=10)),
                ('aadhar_number', models.CharField(max_length=12)),
                ('blood_group', models.CharField(max_length=3)),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('health_insurance_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('health_insurance_policy_number', models.CharField(blank=True, max_length=20, null=True)),
                ('visa_details', models.CharField(blank=True, max_length=255, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=20, null=True)),
                ('visa_expiry_date', models.DateField(blank=True, null=True)),
                ('reference_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('reference_relationship', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
