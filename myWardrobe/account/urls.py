
from django.conf.urls import include, url

urlpatterns = [
    url(r'^home/$','account.views.home',name='home'),
    url(r'^dresses/$','wardrobe.views.dresses',name='dresses'),
    url(r'^dresses/addDress/$','wardrobe.views.addDress',name='addDress'),
    
    url(r'^accessories/$','wardrobe.views.accessories',name='accessories'),
    url(r'^accessories/addAccessory/$','wardrobe.views.addAccessory',name='addAccessory'),
    
    url(r'^outfits/$','wardrobe.views.outfits',name='outfits'),
    url(r'^outfits/createOutfit/$','wardrobe.views.createOutfit',name='createOutfit'),
    url(r'^friends/$','account.views.friends',name='friends'),
    url(r'^logout/$','account.views.logoutview', name='logout'),
]
