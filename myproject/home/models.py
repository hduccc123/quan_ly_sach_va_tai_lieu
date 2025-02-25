from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 200,null = True)
    isbook = models.BooleanField(default = False,null = True,blank = False)
    image = models.ImageField(null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    description = models.TextField(default='Mô tả đang được cập nhật...', null=False, blank=True)
    author = models.CharField(max_length = 200, null= True)
    def __str__(self):
        return self.name
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    @property
    def books_pdf_url(self):
        try:
            url = self.pdf.url
        except:
            url = ''
        return url    
class Doc(models.Model):
    name = models.CharField(max_length = 200,null = True)
    image = models.ImageField(null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
def upload_to_pdfs(instance, filename):
    return f'pdfs/{filename}'

