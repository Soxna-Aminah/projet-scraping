const {pool}=require('./connexion')
const puppeteer=require("puppeteer")

async function getdonne(){
    const browser=await puppeteer.launch({headless:false})
    const page= await browser.newPage()
    await page.goto("https://sn.coinafrique.com/search?category=11&keyword=meubles+bureau")

    let donnees=await page.evaluate(function(){

        let tableau=new Array()

        const block=document.querySelector(".row.adcard__listing")
        const div= block.childNodes

        div.forEach(sblock =>{
            let data={}
            img=sblock.querySelector(".ad__card-img")
            let span=sblock.querySelector("span")
            // console.log(span);
            if (span!=null && img!=null){
                  var lib=span.getAttribute("data-ad-title")
                  lib=lib.toLowerCase()
                  if(lib.includes("table")){
                    data.categorie="table"
                  }
                  else if(lib.includes("chaise"))
                  {
                    data.categorie="chaise"
                  }
                  else{
                    data.categorie="autre"
                  }
                  data.price=span.getAttribute("data-ad-price")
                  data.img=img.getAttribute('src')
                  data.libelle=lib

                  tableau.push(data)
    
                
            }
          
         })
       return tableau


    })
    for(i of donnees){
         requete=`INSERT INTO meubles(categorie,libelle,image,prix,pageid) VALUES ($1,$2,$3,$4,$5)`
         value=[i.categorie,i.libelle,i.img,i.price,3]
         await pool.query(requete,value)

       }    
    await browser.close()


}
getdonne()