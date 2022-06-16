
var tbody=document.querySelector("tbody")
const thead=document.querySelector('thead').querySelector('tr')

const trb=tbody.querySelectorAll("tr")
const categorie=document.getElementById("cat")
const selection = document.getElementById('select')

function createtbody(data){
    output=""
   for(i of data){
    output+=`
    <tr>
        <td>${i.libelle}</td>
      <td>
      <img src="${i.image}" alt="jbdu">
        </td>
        <td>${i.prix}</td>
        <td class="affichCat">${i.categorie}</td>
        <td>${i.name}</td>
    </tr>
             `
    tbody.innerHTML=output
   }
}


async function recupdonnees(){
   let reponse=await fetch('/donnes');
   let data = await reponse.json()
   data.sort(function(a,b){ return a.prix -b.prix})
   createtbody(data)
 categorie.addEventListener('click',e=>{
    let select= document.getElementById("select")
    select.style.display='block'
    document.getElementById("categorie").style.display='none'
 })
 selection.addEventListener('change',()=>{
    document.getElementById("categorie").style.display='block'
    document.getElementById("select").style.display='none'
    valeur = document.getElementById("select").value
    let litr=[]
    const affichCat = tbody.querySelectorAll('.affichCat')
    console.log(affichCat);

    affichCat.forEach(cat => {
         var el= cat.parentNode
          el.style.display = 'block'
        if(cat.innerText != valeur){
            let tr = cat.parentNode
            // console.log(tr);
            
            tr.style.display = 'none'

        }
        else{
          console.log(el);
        //   el.style.width="200%"

        }
       
        
    });
   
 })

 console.log(data);
 


}
var data=recupdonnees()






























