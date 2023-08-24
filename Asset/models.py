import os
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# To get a correct BD phone number
def validate_phone_number_length(value):
    if len(value) != 11:
        raise ValidationError('Phone number must be exactly 11 characters long.')

# Many user may have same image name. So we have to store everyone's profile picture with unique name.
# Time is the most unique thing that's why I used timestamp to give a unique name to every profile picture
def custom_image_name(instance,filename):
    timestamp=timezone.now().strftime("%Y%m%d%H%M%S")
    extension=os.path.splitext(filename)[1]
    new_filename=instance.name.replace(' ','_')+"_"+timestamp+extension
    return os.path.join('images',new_filename)

# Company model. With company code a company can track asset
class Company(models.Model):
    company_code=models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=30)

    # REQUIRED_FIELDS=[]
    # USERNAME_FIELD="company_code"
    # is_anonymous=False
    # is_authenticated=True

    def __str__(self):
        return self.title

# Gadget user whom can be added ,update,delete, retrieve by Company
class GadgetUser(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=11,validators=[validate_phone_number_length])
    email = models.EmailField(unique=True)
    profile_picture=models.ImageField(upload_to=custom_image_name,null=True,blank=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.name

# We will track gadget which is given to the user through this model
class Gadget(models.Model):
    gadget_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    checked_out_time=models.DateTimeField()
    returned_time=models.DateTimeField()
    condition=models.CharField(max_length=20)
    user=models.ForeignKey(GadgetUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.gadget_name