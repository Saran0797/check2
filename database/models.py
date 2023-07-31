from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=120)
    description = models.TextField()
    title = models.CharField(max_length=120)
    short_title = models.CharField(max_length=120)
    logo = models.ImageField()
    contact_number = models.CharField(max_length=120)
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    email = models.EmailField()
    status = models.CharField(max_length=120)

    def __repr__(self):
        return f"{self.company_name}"


class Clients(models.Model):
    client_name = models.CharField(max_length=120)
    client_short_name = models.CharField(max_length=120)
    contact_manager = models.CharField(max_length=120)
    contact_mail = models.EmailField()
    contact_phone_number = models.CharField(max_length=120)
    contact_address = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.client_name}"


class Projects(models.Model):
    project_name = models.CharField(max_length=120)
    project_short_name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=120)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.project_name}"


class Teams(models.Model):
    team_name = models.CharField(max_length=120)
    team_short_name = models.CharField(max_length=120)
    team_manager = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.team_name}"


class EmployeePersonalInfo(models.Model):
    date_of_birth = models.DateTimeField(default=timezone.now)
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    nationality = models.CharField(max_length=120)
    home_phone = models.CharField(max_length=120)
    mobile_phone = models.CharField(max_length=120)
    personal_email = models.EmailField()
    gender = models.CharField(max_length=120)
    marital_status = models.CharField(max_length=120)

    def __repr__(self):
        return f"{self.date_of_birth}"


class EmployeeRolePolicy(models.Model):
    position_name = models.CharField(max_length=120)
    position_code = models.CharField(max_length=120)
    description = models.TextField()

    def __repr__(self):
        return f"{self.position_name}"


class Employee(models.Model):
    title = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    work_email = models.EmailField()
    work_phone = models.CharField(max_length=120)
    work_location = models.CharField(max_length=120)
    employment_start_date = models.DateTimeField(default=timezone.now)
    employment_status = models.CharField(max_length=120)
    employee_number = models.CharField(max_length=120)
    skills = models.CharField(max_length=120)
    employee_personal_info = models.OneToOneField(EmployeePersonalInfo, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    onboarding_mentor = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_as_onboarding_mentor')
    direct_mentor = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_as_direct_mentor')

    def __repr__(self):
        return f"{self.first_name}"


class EmployeePosition(models.Model):
    description = models.TextField()
    current_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    position_name = models.ForeignKey(EmployeeRolePolicy, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee)

    def __repr__(self):
        return f"{self.description}"


class EmergencyContactInfo(models.Model):
    fullname = models.CharField(max_length=120)
    relationship = models.CharField(max_length=120)
    home_phone = models.CharField(max_length=120)
    mobile_phone = models.CharField(max_length=120)
    work_phone = models.CharField(max_length=120)
    email = models.EmailField()
    country = models.CharField(max_length=120)
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=120)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.fullname}"


class EmployeeBankDetail(models.Model):
    account_number = models.CharField(max_length=120)
    sort_code = models.CharField(max_length=120)
    bank_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    primary_account = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.account_number}"


class EmployeePassport(models.Model):
    passport_number = models.CharField(max_length=120)
    country_of_issue = models.CharField(max_length=120)
    expiration_date = models.DateTimeField(default=timezone.now)
    issue_date = models.DateTimeField(default=timezone.now)
    issuing_authority = models.CharField(max_length=120)
    place_of_birth = models.CharField(max_length=120)
    nationality = models.CharField(max_length=120)
    attachment = models.FileField()
    current_active = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.passport_number}"


class EmployeeVisa(models.Model):
    visa_number = models.CharField(max_length=120)
    visa_type = models.CharField(max_length=120)
    country_of_issue = models.CharField(max_length=120)
    expiration_date = models.DateTimeField(default=timezone.now)
    issue_date = models.DateTimeField(default=timezone.now)
    issuing_authority = models.CharField(max_length=120)
    purpose_of_travel = models.CharField(max_length=120)
    remarks = models.CharField(max_length=120)
    attachment = models.FileField()
    current_active = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.visa_number}"


class EmployeeEducation(models.Model):
    degree = models.CharField(max_length=120)
    institution = models.CharField(max_length=120)
    major = models.CharField(max_length=120)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    grade = models.CharField(max_length=120)
    description = models.TextField()
    attachment = models.FileField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.degree}"


class EmployeeCertification(models.Model):
    name = models.CharField(max_length=120)
    institution = models.CharField(max_length=120)
    issued_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    attachment = models.FileField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.name}"


class AssetCategory(models.Model):
    asset_category_name = models.CharField(max_length=120)
    description = models.TextField()

    def __repr__(self):
        return f"{self.asset_category_name}"


class Assets(models.Model):
    asset_name = models.CharField(max_length=120)
    description = models.TextField()
    asset_number = models.CharField(max_length=120)
    serial_number = models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)
    comments = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    asset_category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.asset_name}"


class LeaveAllocation(models.Model):
    policy_allocation_name = models.CharField(max_length=120)
    description = models.TextField()

    def __repr__(self):
        return f"{self.policy_allocation_name}"


class LeavePolicy(models.Model):
    policy_name = models.CharField(max_length=120)
    description = models.TextField()
    allocated_days = models.IntegerField()
    working_hours = models.IntegerField()
    do_carry_over = models.BooleanField(default=False)
    is_shown_in_employee_calender = models.BooleanField(default=False)
    allocated_type = models.ForeignKey(LeaveAllocation, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.policy_name}"


class LeaveEmployee(models.Model):
    reason = models.CharField(max_length=120)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    number_of_days = models.IntegerField()
    approved_status = models.CharField(max_length=120)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy_name = models.ForeignKey(LeavePolicy, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.reason}"


class TaskPriority(models.Model):
    priority_name = models.CharField(max_length=120)
    description = models.TextField()
    priority_range = models.IntegerField()

    def __repr__(self):
        return f"{self.priority_name}"


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    task_status = models.CharField(max_length=120)
    original_estimate = models.IntegerField()
    priority = models.ForeignKey(TaskPriority, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks_as_assignee')
    reporter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks_as_reporter')

    def __repr__(self):
        return f"{self.title}"


class TimeSheet(models.Model):
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=120)
    total_hours = models.IntegerField()
    resource = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='timesheet_as_resource')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='timesheet_as_reporter')

    def __repr__(self):
        return f"{self.date}"


class Payslips(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    total_hours = models.IntegerField()
    number_of_days = models.IntegerField()
    status = models.CharField(max_length=120)
    notes = models.TextField()
    attachment = models.FileField()
    reporter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payslip_as_reporter')
    resource = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payslip_as_resource')

    def __repr__(self):
        return f"{self.start_date}"


class AnnouncementTopic(models.Model):
    topic = models.CharField(max_length=120)
    description = models.TextField()
    is_to_everyone = models.BooleanField(default=True)

    def __repr__(self):
        return f"{self.topic}"


class Announcement(models.Model):
    title = models.CharField(max_length=120)
    message = models.TextField()
    attachments = models.FileField()
    author = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='announcement_as_author')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='announcement_as_employee')
    topic = models.ForeignKey(AnnouncementTopic, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.title}"
