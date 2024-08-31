from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(blank=True, null=True, max_length=30, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

    def get_profile(self):
        return ProfileModel.objects.get_or_create(user=self)[0]


@receiver(post_save, sender=CustomUser)
def save_username_when_user_is_created(sender, instance, created, *args, **kwargs):
    if created:
        email = instance.email
        sliced_email = email.split("@")[0]
        instance.username = sliced_email
        instance.save()


GENDER = (
    ("male", "Male"),
    ("female", "Female"),
)


class ProfileModel(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, unique=True, related_name="profile"
    )
    picture = models.ImageField(upload_to="profile_picture", null=True, blank=True)
    friends = models.ManyToManyField(CustomUser, related_name="friends", blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default="none")
