
function init(){
 console.log("heelo");
  var category_list=document.getElementById("category_list");
  var occasion_list=document.getElementById("occasion_list");
  var season_list=document.getElementById("season_list");
  
  console.log(category_list);
  var top_choices = [ 
'Top', 'Tunic','Shirt','T-shirt', 'Kurta','Kurti','Coat','Jacket','Sweater', 'Cardigan','Blouse']

  var lower_choices=['Jeans','Shorts','Trouser','Pyjama', 'Skirt','Cargoes','Leggings','Capri']

  var singlePiece_choices=['Suit','Saree','Maxi','Gown','TrackSuit','RainCoat']
 
   var el1=document.createElement("div");
   el1.innerHTML='Tops';
   category_list.appendChild(el1);
   
   for(var i=0;i<top_choices.length;i++)
   {  var el=document.createElement("div");
      el.innerHTML=top_choices[i];
      el1.appendChild(el);
   }
   
   var el2=document.createElement("div");
   el2.innerHTML='Lowers';
   category_list.appendChild(el2);
   
   for(var i=0;i<lower_choices.length;i++)
   {  var el=document.createElement("div");
      el.innerHTML=lower_choices[i];
      el2.appendChild(el);
   }
  
   var el3=document.createElement("div");
   el3.innerHTML='SinglePieces';
   category_list.appendChild(el3);
    
   for(var i=0;i<singlePiece_choices.length;i++)
   {  var el=document.createElement("div");
      el.innerHTML=singlePiece_choices[i];
      el3.appendChild(el);
   }

  var season_choices = ['Summer','Winter','Rainy','All'];
    for(var i=0;i<season_choices.length;i++)
   {  var el=document.createElement("div");
      el.innerHTML=season_choices[i];
      season_list.appendChild(el);
   }

    
    var occasion_choices=['Informal/Casuals','Work','Sport','Party'];
    for(var i=0;i<occasion_choices.length;i++)
   {  var el=document.createElement("div");
      el.innerHTML=occasion_choices[i];
      occasion_list.appendChild(el);
   }

}
