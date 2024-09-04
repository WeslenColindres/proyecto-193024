from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    profile_image = models.BinaryField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    codename = models.CharField(max_length=255, unique=True)


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)


class GroupPermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'permission')


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'group')


class Follower(models.Model):
    follower = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
    table_name = models.CharField(max_length=255)
    record_id = models.BigIntegerField(null=True, blank=True)
    changes = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
