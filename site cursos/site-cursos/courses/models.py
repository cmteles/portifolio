from django.db import models

import os

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Original', blank= True, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço com Desconto', blank= True, null=True)

    image = models.ImageField(upload_to='courses/',verbose_name="Imagem",blank= True, null=True)

    description = models.TextField(verbose_name='Descrição', blank= True, null=True)

    situation = models.BooleanField(default=True, verbose_name='Ativo')

    # slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="Slug")
    slug = models.SlugField(unique=True, verbose_name="Slug")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    upadated_at = models.DateTimeField(auto_now=True, verbose_name="Data de modificação")

    def save(self, *args, **kwargs):
        #verifica se ja existe no banco
        if self.pk:
            old_image = Course.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        super().save( *args, **kwargs)

    # Sobrescrever o Método delete para Remover a Imagem
    def delete(self, *args, **kwargs):
        # Remover a imagem associada ao objeto
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        # Excluir o registro
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"

class About(models.Model):
    """Modelo que representa sobre"""
    name = models.CharField(max_length=255, verbose_name="Nome")

    image = models.ImageField(upload_to='about/', verbose_name="Imagem", blank=True, null=True)

    description = models.TextField(verbose_name="Descrição", blank=True, null=True)

    situation = models.BooleanField(default=True, verbose_name="Situação")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    # Sobrescrever o Método save no Modelo
    def save(self, *args, **kwargs):
        # Verificar se o objeto já existe no banco de dados
        if self.pk:
            # Buscar o objeto atual no banco
            old_image = About.objects.get(pk=self.pk).image
            # Comparar se a imagem foi alterada
            if old_image and old_image != self.image:
                # Remover a imagem antiga do sistema de arquivos
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        # Salvar o novo registro
        super().save(*args, **kwargs) 

    # Sobrescrever o Método delete para Remover a Imagem
    def delete(self, *args, **kwargs):
        # Remover a imagem associada ao objeto
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        # Excluir o registro
        super().delete(*args, **kwargs)

    def __str__(self):
        """Retorna: str: O nome sobre."""
        return self.name
    
    class Meta:
        verbose_name = "sobre"
        verbose_name_plural = "sobre"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField( verbose_name="E-mail")
    subject = models.CharField(max_length=255, verbose_name="Assunto")
    message = models.TextField( verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")
    
    def __str__(self):
        """Retorna: str: O assunto da mensagem"""
        return self.subject
    
    class Meta:
        verbose_name = "menssagem de contato"
        verbose_name_plural = "mensegens de contato"