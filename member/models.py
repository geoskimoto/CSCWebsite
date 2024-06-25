# Entity-Relationships:
# MEMBER(memberID, name, username, email, phone_number, status, date_joined, last_login, emergency_contact, emergency_contact_phone, is_family_member, is_employee, is_committee_member, is_superuser)

# FAMILY_MEMBER(familyMemberID, memberID, relation)
#       FAMILY_MEMBER(memberID) must exist in MEMBER(memberID)
# LOCKER(lockerID, locker_number, assigned_to, price_per_year, rental_start_date, rental_end_date)
#       LOCKER(assigned_to) must exist in MEMBER(memberID)
# BUNK(bunkID, bunk_number, assigned_to, price_per_night, area)
#       BUNK(assigned_to) must exist in MEMBER(memberID)
# RESERVATION(reservationID, memberID, bunkID, start_date, end_date, total_price)
#       RESERVATION(memberID) must exist in MEMBER(memberID)
# RESERVATION(bunkID) must exist in BUNK(bunkID)
# PAYMENT(paymentID, memberID, amount, payment_date, payment_method, reservationID, lockerID)
#       PAYMENT(memberID) must exist in MEMBER(memberID)
# PAYMENT(reservationID) must exist in RESERVATION(reservationID) (nullable)
#       PAYMENT(lockerID) must exist in LOCKER(lockerID) (nullable)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, Group, Permission


class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Member(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    emergency_contact = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    is_family_member = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_committee_member = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='member_set',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='member_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'
class FamilyMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='family_members')
    relation = models.CharField(max_length=50)  # e.g., spouse, child

class Locker(models.Model):
    locker_number = models.CharField(max_length=10, unique=True)
    assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='lockers')
    price_per_year = models.DecimalField(max_digits=10, decimal_places=2, default=75.00)
    rental_start_date = models.DateField(null=True, blank=True)
    rental_end_date = models.DateField(null=True, blank=True)


#
