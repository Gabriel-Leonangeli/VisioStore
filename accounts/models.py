from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.png', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"



@receiver(post_save, sender=User)
def crear_o_guardar_usuario_perfil(sender, instance, created, **kwargs):
    if created:
       
        Usuario.objects.create(user=instance)
    else:
        
        try:
            instance.usuario.save()
        except Usuario.DoesNotExist:

            Usuario.objects.create(user=instance)


@property
def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/avatar/default.png'