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

class Member(AbstractUser):
    # name = models.CharField(max_length=100)
    # username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
    emergency_contact = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    is_family_member = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_committee_member = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    #---------------------
    # Linking Member to auth.User
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True)
    # Django handles authentication in the AbstractUser class which Member inherits. It creates a User that's separate
    # from any table (i.e. Member), so you have to link them with OneToOne relationship.
    # NOTE! : setting null=True.  Member must have a User and User must have a Member but I think this will just set
    # user to null until one is created with the save method????  Dunno this seems jenky.

    #Maybe try this?
    # https://stackoverflow.com/questions/39527289/associating-users-with-models-django
    # --------------------

    groups = models.ManyToManyField(
        Group,
        related_name='member_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='member_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        # model = User #I think you can use the Meta class to combine User and Member
        #go to 47min in this video https://www.youtube.com/watch?v=WuyKxdLcw3w
        #Think the above video shows how to put Member info into the User table.
        # Because the User table is a bit obscure/abstract think you still would rather
        # just link it to a Member table.  Just need to figure out why there are two
        # passwords with both tables and if they are actually linked.
        verbose_name = 'member'
        verbose_name_plural = 'members'

    # Every Member instance needs a corresponding auth.User instance from the moment it's created, so  create a default
    # auth.User instance if one doesn't exist.
    def save(self, *args, **kwargs):
        if not self.user_id:
            # Create a default auth.User instance if not already assigned
            self.user = User.objects.create(username=self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


    def update_balance(self):
        total_paid = self.payments.aggregate(total=models.Sum('amount'))['total'] or 0
        total_invoiced = self.invoices.aggregate(total=models.Sum('amount_due'))['total'] or 0
        self.balance = total_paid - total_invoiced
        self.save()


class FamilyMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='family_members')
    relation = models.CharField(max_length=50)  # e.g., spouse, child

    def __str__(self):
        return f"{self.relation} of {self.member.name}"


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
