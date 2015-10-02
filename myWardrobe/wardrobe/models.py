from django.db import models
from account.models import MyUser
from colorful.fields import RGBColorField

# Create your models here.
class Wardrobe(models.Model):
  tops_count=models.IntegerField(default=0)
  lowers_count=models.IntegerField(default=0)
  singlePieces_count=models.IntegerField(default=0)
  outfits_count=models.IntegerField(default=0)
  accessories_count=models.IntegerField(default=0)
  owner=models.OneToOneField(MyUser);
  
  def __str__(self):
    return self.owner.username+"'s wardrobe";


SEASON_CHOICES=[('Summer','Summer'),('Winter','Winter'),('Rainy','Rainy'),('All','All')]

OCCASION_CHOICES=[('Informal','Informal/Casuals'),('Work','Work'),('Sport','Sport'),('Party','Party')]  

class DressCategory(models.Model):
  name=models.CharField(max_length=16)
  parent_category_id=models.ForeignKey("self",blank=True,null=True)
  def __str__(self):
    return self.name;

class Dress(models.Model):
  image=models.ImageField(upload_to = 'dresses/')
  
  season=models.CharField(max_length=7,choices=SEASON_CHOICES,default='All')
  occasion=models.CharField(max_length=10,choices=OCCASION_CHOICES,default='Work')
  category=models.ForeignKey(DressCategory)
  
  color=RGBColorField(null=True,blank=True)
  hash_tag=models.CharField(max_length=32,blank=True,null=True)
  owner=models.ForeignKey(MyUser,related_name='outfits')
  wardrobe=models.ForeignKey(Wardrobe,related_name='dresses',null=True)
  
  at_laundry=models.BooleanField(default=False)
  #share=models.CharField(max_length=8,choices=[('Private','Private'),('Public','Public')],default='Private')
  wear_on=models.DateField(auto_now_add=False,auto_now=False,blank=True)
  
  
  def __str__(self):
    return self.owner.username+'_dress-id_'+str(self.id);

ACCESSORY_CATEGORY_CHOICES=[('HandBag','Handbag'),('Clutches','Clutches'),('Broche','Broche'),('Wallet','Wallet'),('Belt','Belt'),('Hat','Hat'),('SunGlasses','SunGlasses'),('Scarf','Scarf'),('Bracelet','Bracelet'),('Necklace','Necklace'),('Ring','Ring'),('Earing','Earing'),('Watch','Watch'),('Gloves','Gloves'),('Sandals','Sandals'),('Shoes','Shoes'),('Bellies','Bellies')]

class Accessory(models.Model):
  image=models.ImageField(upload_to='accessories/')
  
  season=models.CharField(max_length=7,choices=SEASON_CHOICES,default='All')
  occasion=models.CharField(max_length=10,choices=OCCASION_CHOICES,default='Party')
  category=models.CharField(max_length=15,choices=ACCESSORY_CATEGORY_CHOICES,default='Top')
  
  hash_tag=models.CharField(max_length=32,blank=True,null=True)
  owner=models.ForeignKey(MyUser,related_name='accessories')
  
  def __str__(self):
    return self.owner.username+'_acc-id_'+str(self.id);

class Outfit(models.Model):
  name=models.CharField(max_length=32,blank=True)
  dress_components=models.ManyToManyField(Dress)
  accessories_needed=models.ManyToManyField(Accessory)
   
  def __str__(self):
    return self.name+' by '+self.owner.username;

