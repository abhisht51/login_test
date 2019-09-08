from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address!')

        if not password:
            raise ValueError('Users must have a password!')

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.save(using = self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user      


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True) # can log in
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    # subscription_period = models.IntegerField(default=1)
    # subscription_end = models.DateTimeField(default=datetime.now)
    # created_at = models.DateTimeField(default=datetime.now)
    # updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email';
    REQUIRED_FIELDS = [] #USERNAME_FIELD and Password required by default.

    objects = UserManager();

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    # # def save(self, *args, **kwargs):
    # #     self.subscription_end = date.today() + relativedelta(months=+self.subscription_period)
    # #     super(User, self).save(*args, **kwargs) # Call the "real" save() method.

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

class Cultural_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    category=models.CharField(max_length=100,help_text='Examples: music,dance')
    club=models.CharField(max_length=100)
    rules=models.CharField(max_length=100)
    fees_snu=models.DecimalField(decimal_places=2,max_digits=4,help_text='For SNU niggas only')
    fees_amount=models.DecimalField(decimal_places=2,max_digits=4)
    prize_money=models.DecimalField(decimal_places=2,max_digits=5)
    team_size=models.CharField(max_length=100,help_text='If solo then enter 1 else no. of required team members')
    time_limit=models.CharField(max_length=100,help_text='Time limit for one performance or event if not then enter null')
    registration_link=models.CharField(max_length=200)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative')
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative')
    poster=models.CharField(max_length=200,help_text='name of poster file')

class Technical_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    club=models.CharField(max_length=100)
    rules=models.CharField(max_length=100)
    fees_snu=models.DecimalField(decimal_places=2,max_digits=4,help_text='For SNU niggas only')
    fees_amount=models.DecimalField(decimal_places=2,max_digits=4)
    prize_money=models.DecimalField(decimal_places=2,max_digits=5)
    team_size=models.CharField(max_length=100,help_text='If solo then enter 1 else no. of required team members')
    time_limit=models.CharField(max_length=100,help_text='Time limit for one event if not then enter null')
    registration_link=models.CharField(max_length=200)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative')
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative')
    poster=models.CharField(max_length=200,help_text='name of poster file')

class Sports_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    fees_amount=models.DecimalField(decimal_places=2,max_digits=4)
    rules=models.CharField(max_length=100)
    prize_money=models.DecimalField(decimal_places=2,max_digits=5)
    team_size=models.CharField(max_length=100,help_text='If solo then enter 1 else no. of required team members')
    fees_snu=models.DecimalField(decimal_places=2,max_digits=4,help_text='For SNU niggas only')
    registration_link=models.CharField(max_length=200)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative')
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative')
    poster=models.CharField(max_length=200,help_text='name of poster file')

