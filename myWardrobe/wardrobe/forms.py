from django import forms
from wardrobe.models import Dress,Accessory,Outfit

#Create you forms here
class DressForm(forms.ModelForm):
  class Meta:
    model=Dress
    exclude=['wear_on','owner','wardrobe']
    widgets = {
          'season':forms.RadioSelect,
          'occasion':forms.RadioSelect,
          'category':forms.RadioSelect,
        }

class AccessoryForm(forms.ModelForm):
  class Meta:
    model=Accessory
    fields='__all__'
    widgets = {
          'season':forms.RadioSelect,
          'occasion':forms.RadioSelect,
          'category':forms.RadioSelect,
        }


class OutfitForm(forms.ModelForm):
  class Meta:
    model=Outfit
    fields='__all__'
    widgets = {
          'dress_components':forms.CheckboxSelectMultiple,
	  'accessories_needed':forms.CheckboxSelectMultiple,
              }

