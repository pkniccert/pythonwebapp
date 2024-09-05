from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class Agency(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "agency"
        verbose_name_plural = "agencies"

class Category(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "category"
        verbose_name_plural = "categories"

class Subcategory(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "subcategory"
        verbose_name_plural = "subcategories"

class Ministry(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "ministry"
        verbose_name_plural = "ministries"

class Department(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    ministry = models.ForeignKey(Ministry, related_name="departments", on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "department"
        verbose_name_plural = "departments"

class Location(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    ministry = models.ForeignKey(Ministry, related_name="locations", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name="locations", on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "location"
        verbose_name_plural = "locations"

class State(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "state"
        verbose_name_plural = "states"

class StateDepartment(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    state = models.ForeignKey(State, related_name="state_departments", on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "state department"
        verbose_name_plural = "state departments"

class StateLocation(models.Model):
    STATUS_CHOICES = (
        (0, 'De-Active'),
        (1, 'Active'),
    )
    state = models.ForeignKey(State, related_name="state_locations", on_delete=models.CASCADE)
    department = models.ForeignKey(StateDepartment, related_name="state_locations", on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "state location"
        verbose_name_plural = "state locations"
