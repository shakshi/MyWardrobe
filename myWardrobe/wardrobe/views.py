from django.shortcuts import render,redirect
from wardrobe.forms import DressForm,AccessoryForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
@login_required
@require_http_methods(['GET','POST'])
def dresses(request):
  if request.method=='GET':
    #f=DressFilterForm();
    return render(request,'wardrobe/dresses.html');
  #else:
    #f=DressFilterForm(request.POST)
    
    #if f.is_valid():
      #category_option=f.cleaned_data['category']
      #dress_list=request.user.dresses.filter(category=category_option)
      #return render(request,'account/wardrobe.html',{'filterForm':f,'dress_list':dress_list})


@login_required
def outfits(request):
  return render(request,'wardrobe/outfits.html');

@require_http_methods(['GET','POST'])
@login_required
def createOutfit(request):
  return render(request,'wardrobe/createOutfit.html');

@login_required
def showItems(request):
  return render(request,'wardrobe/outfits.html',{'item-list':item_list});

@login_required
@require_http_methods(['GET','POST'])
def accessories(request):
  acc_list=['HandBag','Clutch','Broche','Wallet','Belt','Hat','SunGlasses','Scarf','Bracelet','Necklace','Ring','Earing','Watch','Gloves'];
  if request.method=='GET':
    return render(request,'wardrobe/accessories.html',{'list':acc_list});

@require_http_methods(['GET','POST'])
@login_required
def addDress(request):
  if(request.method=='GET'):
    f=DressForm()
    return render(request,'wardrobe/addDress.html',{'nForm':f});
  else:
    f=DressForm(request.POST,request.FILES)
    if f.is_valid(): 
      dress=f.save(commit=False)
      dress.wardrobe=request.user.wardrobe
      dress.owner=request.user
      dress.save()
      return redirect('dresses')
    else:
      return render(request,'wardrobe/addDress.html',{'nForm':f});  

@require_http_methods(['GET','POST'])
@login_required
def addAccessory(request):
  if(request.method=='GET'):
    f=AccessoryForm()
    return render(request,'wardrobe/addAccessory.html',{'nForm':f});
  else:
    f=AccessoryForm(request.POST,request.FILES)
    if f.is_valid(): 
      accessory=f.save(commit=False)
      accessory.owner=request.user
      accessory.save()
      return redirect('accessories')
    else:
      return render(request,'wardrobe/addAccessory.html',{'nForm':f});

