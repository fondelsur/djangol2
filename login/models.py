from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AccountData(models.Model):
    account_name = models.CharField(max_length=45)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_data'
        unique_together = (('account_name', 'var'),)


class Accounts(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    lastactive = models.BigIntegerField(default='0')
    accesslevel = models.IntegerField(db_column='accessLevel', default='0')  # Field name made lowercase.
    lastip = models.CharField(db_column='lastIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastserver = models.IntegerField(db_column='lastServer', blank=True, null=True)  # Field name made lowercase.
    pcip = models.CharField(db_column='pcIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    hop1 = models.CharField(max_length=15, blank=True, null=True)
    hop2 = models.CharField(max_length=15, blank=True, null=True)
    hop3 = models.CharField(max_length=15, blank=True, null=True)
    hop4 = models.CharField(max_length=15, blank=True, null=True)

    def __unicode__(obj):
        return obj.login

    class Meta:
        db_table = 'accounts'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accounts = models.OneToOneField(Accounts, on_delete=models.DO_NOTHING)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class AccountsIpauth(models.Model):
    login = models.CharField(max_length=45)
    ip = models.CharField(max_length=15)
    type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'accounts_ipauth'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gameservers(models.Model):
    server_id = models.IntegerField(primary_key=True)
    hexid = models.CharField(max_length=50)
    host = models.CharField(max_length=50)

    class Meta:
        db_table = 'gameservers'
