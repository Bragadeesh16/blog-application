from django.db import models
from chats.manager import ThreadManager
from account.models import CustomUser


class CreateCommunity(models.Model):
    Group_name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.Group_name


class GroupMessage(models.Model):
    group = models.ForeignKey(CreateCommunity, on_delete=models.CASCADE)
    auther = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="send_request"
    )
    receiver_in = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="receiver_request"
    )
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return (
            f"{self.sender.username} sent {self.receiver_in.username} a friend request "
        )


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Thread(TrackingModel):
    THREAD_TYPE = (("personal", "Personal"), ("group", "Group"))

    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(
        max_length=15, choices=THREAD_TYPE, default="personal"
    )
    users = models.ManyToManyField(CustomUser)

    objects = ThreadManager()

    def __str__(self) -> str:
        if self.thread_type == "personal" and self.users.count() == 2:
            return f"{self.users.first()} and {self.users.last()}"
        return f"{self.name}"


class Message(TrackingModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f"From <Thread - {self.thread}>"
