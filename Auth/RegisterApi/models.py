from django.db import models

# Create your models here.


## Bio-fields are name, email , phone no.
## Identification-fields are username.
## Authentication-field  are password.
   
# in the place of modelserializer we can use this.


#class RegisterInfo(models.Model):
   
    ## "id" is autogenrated in django if we don't use of primary key.
    #Name = models.CharField(max_length=20)
   # Email = models.EmailField(max_length=50)
   # phone_number = models.CharField(max_length=12)
   # Username = models.CharField(max_length=20)
  #  Password = models.CharField(max_length=20)
    
  #  class Meta:  
        #db_table = "User_Info"
#