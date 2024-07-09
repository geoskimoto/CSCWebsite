from django.db import models
# from django.db.models.signals import post_save, pre_delete
# from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

class Locker(models.Model):
    number = models.CharField(max_length=10, unique=True)
    price_per_year = models.DecimalField(max_digits=10, decimal_places=2, default=75.00)
    rental_start_date = models.DateField(null=True, blank=True)
    rental_end_date = models.DateField(null=True, blank=True)
    members_assigned = models.ManyToManyField('Member', related_name='lockers', blank=True)

    def __str__(self):
        return self.number

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import User, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50)
    skills = models.CharField(max_length=400, blank=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='USA')
    primary_phone = models.CharField(max_length=30, blank=True)
    secondary_phone = models.CharField(max_length=30, blank=True)
    website_url = models.URLField(max_length=100, blank=True)
    joining_comments = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    is_family_member = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_committee_member = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Linking Member to auth.User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='member_set',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='member_set',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    # Specify the required fields for the Member model
    # REQUIRED_FIELDS: Added the REQUIRED_FIELDS attribute to the Member model. This specifies the fields that are
    # required when creating a Member instance using the createsuperuser management command.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'occupation', 'address_line_1', 'city', 'state',
                       'zip_code', 'emergency_contact', 'emergency_contact_phone']
    USERNAME_FIELD = 'user'  # Define the username field for the Member model
    EMAIL_FIELD = 'user'  # Define the email field if you want to use email for user identification

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.user.username

    def update_balance(self):
        total_paid = self.payments.aggregate(total=models.Sum('amount'))['total'] or 0
        total_invoiced = self.invoices.aggregate(total=models.Sum('amount_due'))['total'] or 0
        self.balance = total_paid - total_invoiced
        self.save()

# Signal to create a User when a Member is created
# Creating User Instance: The save method in the commented out Members class below creates a User instance if one
# doesn't exist. However, the User instance created in this way may lack other essential fields like email or password.
# It's more robust to handle User creation separately.
# Using Signals: Instead of overriding the save method, use Django signals to create a User instance whenever a Member
# instance is created.
@receiver(post_save, sender=Member)
def create_user_for_member(sender, instance, created, **kwargs):
    if created and not instance.user_id:
        user = User.objects.create(username=instance.username)
        instance.user = user
        instance.save()


class Invoice(models.Model):
    member = models.ForeignKey(Member, related_name='member_invoices', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return f'Invoice {self.id} for {self.member}'

class Payment(models.Model):
    member = models.ForeignKey(Member, related_name='member_payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Payment {self.id} for {self.member}'



#KEEP THIS!! There's some good reference notes from when you were trying to inherit user instead of linking user and
#member using a OneToOneField.
# class Member(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)  #AbstractUser classes uses this field, so HAS to be unique,
#     #or else will throw an error.
#     date_of_birth = models.DateField()
#     occupation = models.CharField(max_length=50)
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
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     status = models.CharField(max_length=20)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
#     emergency_contact = models.CharField(max_length=100)
#     emergency_contact_phone = models.CharField(max_length=15)
#     is_family_member = models.BooleanField(default=False)
#     is_employee = models.BooleanField(default=False)
#     is_committee_member = models.BooleanField(default=False)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#
#     #---------------------
#     # Linking Member to auth.User
#
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True)
#
#     # Django handles authentication in the AbstractUser class which Member inherits. It creates a User that's separate
#     # from any table (i.e. Member), so you have to link them with OneToOne relationship.
#     # NOTE! : setting null=True.  Member must have a User and User must have a Member but I think this will just set
#     # user to null until one is created with the save method????  Dunno this seems jenky.
#
#     #Maybe try this?
#     # https://stackoverflow.com/questions/39527289/associating-users-with-models-django
#     # --------------------
#
#     groups = models.ManyToManyField(
#         Group,
#         related_name='member_set',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='member_set',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )
#
#     class Meta:
#         # model = User #I think you can use the Meta class to combine User and Member
#         #go to 47min in this video https://www.youtube.com/watch?v=WuyKxdLcw3w
#         #Think the above video shows how to put Member info into the User table.
#         # Because the User table is a bit obscure/abstract think you still would rather
#         # just link it to a Member table.  Just need to figure out why there are two
#         # passwords with both tables and if they are actually linked.
#         verbose_name = 'member'
#         verbose_name_plural = 'members'
#
#     # Every Member instance needs a corresponding auth.User instance from the moment it's created, so  create a default
#     # auth.User instance if one doesn't exist.
#     def save(self, *args, **kwargs):
#         if not self.user_id:
#             # Create a default auth.User instance if not already assigned
#             self.user = User.objects.create(username=self.username)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.username
#
#
#     def update_balance(self):
#         total_paid = self.payments.aggregate(total=models.Sum('amount'))['total'] or 0
#         total_invoiced = self.invoices.aggregate(total=models.Sum('amount_due'))['total'] or 0
#         self.balance = total_paid - total_invoiced
#         self.save()


class FamilyMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='family_members')
    relation = models.CharField(max_length=50)  # e.g., spouse, child

    def __str__(self):
        return f"{self.relation} of {self.member.name}"

class MemberApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50)
    skills = models.CharField(max_length=400, blank=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='USA')
    phone_number = models.CharField(max_length=30, blank=True) #make this with more appropriate constraints/formating.
    website_url = models.URLField(max_length=100, blank=True)
    joining_comments = models.TextField(max_length=1000, blank=True)
# Django handles the relationship between Member and Locker internally when you use a ManyToManyFields, so don't need
# to use signals when it's set up this way!

# @receiver(post_save, sender=Member)
# def update_locker_on_member_save(sender, instance, **kwargs):
#     if instance.assigned_locker:
#         locker = instance.assigned_locker
#         if locker.member_assigned_to != instance:
#             locker.member_assigned_to = instance
#             locker.save()
#
# @receiver(pre_delete, sender=Member)
# def clear_locker_on_member_delete(sender, instance, **kwargs):
#     if instance.assigned_locker:
#         locker = instance.assigned_locker
#         locker.member_assigned_to = None
#         locker.save()
#