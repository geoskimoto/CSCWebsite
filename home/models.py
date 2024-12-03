from django.db import models


<<<<<<< HEAD
class MembershipApplication(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    last_logged_in = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=100)
    skills = models.CharField(max_length=400, blank=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='USA')
    home_phone = models.CharField(max_length=30, blank=True)
    work_phone = models.CharField(max_length=30, blank=True)
    mobile_phone = models.CharField(max_length=30, blank=True)
    website_url = models.URLField(max_length=100, blank=True)
    joining_comments = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
=======
# class MembershipApplication(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=80)
#     last_logged_in = models.DateTimeField(auto_now=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     date_of_birth = models.DateField()
#     occupation = models.CharField(max_length=100)
#     skills = models.CharField(max_length=400, blank=True)
#     address_line_1 = models.CharField(max_length=50)
#     address_line_2 = models.CharField(max_length=50, blank=True)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     zip_code = models.CharField(max_length=10)
#     country = models.CharField(max_length=50, default='USA')
#     home_phone = models.CharField(max_length=30, blank=True)
#     work_phone = models.CharField(max_length=30, blank=True)
#     mobile_phone = models.CharField(max_length=30, blank=True)
#     website_url = models.URLField(max_length=100, blank=True)
#     joining_comments = models.TextField(max_length=1000, blank=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
>>>>>>> origin/laptop
