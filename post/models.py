from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username

    @property
    def num_follows(self):
        return self.follows.all().count
    
    @property
    def num_followed(self):
        return self.followed.all().count
        

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()



class Dweet(models.Model):
    user = models.ForeignKey(User,related_name="dweets",on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None , blank=True , related_name='liked')
    updated = models.DateTimeField(auto_now=True)




    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d}): "
            f"{self.body[:30]}..."
        )

    @property
    def num_likes(self):
        return self.liked.all().count()


    class Meta:
        ordering = ['-created_at']


LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),

)





class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post_save = models.ForeignKey(Dweet, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Like' , max_length=10)

    def __str__(self):
        return str(self.post)


class Posted(models.Model):
    userp = models.ForeignKey(User,related_name="posteds",on_delete=models.DO_NOTHING)
    bodyp = models.CharField(max_length=300)
    created_atp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"{self.bodyp[:30]}..."
        )
  


