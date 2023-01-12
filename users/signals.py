from django.contrib.auth.models import User
from django.db.models.signals import post_save #signali gönderen
from django.dispatch import receiver #signali yakalayan
from rest_framework.authtoken.models import Token # işlem yapılacak nookta

@receiver(post_save,sender=User)
def create_Token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)