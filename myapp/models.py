from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=20,null=True)
    profile_photo = models.FileField(null=True)
    joined_rooms = models.ManyToManyField('Room', related_name='users')


    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=15)
    likes = models.ManyToManyField(Signup, related_name="liked", null=True, blank=True)
    dislikes = models.ManyToManyField(Signup, related_name="disliked", null=True, blank=True)
    qr_code = models.FileField(null=True)
    def __str__(self):
        return self.user.username+" "+self.status

# Model for OTP
class OTPModel(models.Model):
    user = models.EmailField(max_length=127)
    timestamp = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField()

    class Meta:
        verbose_name = 'OTP'

# Model for JoinDate
class JoinDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " " + self.room.name



# Model for Room
class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    room_code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
