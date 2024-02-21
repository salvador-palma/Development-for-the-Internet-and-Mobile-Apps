var Theme = {LIGHT: 'light' , DARK : 'dark'};
var isAsideOn = false;


const ISCTE_DAY = "https://keystoneacademic-res.cloudinary.com/image/upload/f_auto/q_auto/g_auto/w_auto/dpr_2.0/element/11/111946_3.jpg";
const ISCTE_NIGHT = "ISCTENIGHT.png";
document.addEventListener("DOMContentLoaded", () => {
    const htmlElement = document.documentElement;
    var addStudent = document.getElementById("addStudentButton");
    var studentDiv = document.getElementById("studentDiv");
    const themeButton = document.getElementById("theme-toggler");
    const iscteLogo = document.getElementById("iscteLogo");
    const background_image = document.getElementById("BG");
    
    themeButton.addEventListener("click", function(){
      var currentTheme = htmlElement.getAttribute("data-theme");
      var newTheme = currentTheme === 'light' ? 'dark' : 'light';
      htmlElement.setAttribute("data-theme", newTheme); 
      
      if(newTheme == "dark"){iscteLogo.setAttribute("src", "Negative Logo.png"); background_image.setAttribute("src", ISCTE_NIGHT);} 
      else{iscteLogo.setAttribute("src", "Logo.png"); background_image.setAttribute("src", ISCTE_DAY);} 

      
    });

    try{
      addStudent.addEventListener("click", function() {

        var divs = document.querySelectorAll("#studentDiv > div");
      
        if (divs.length == 3) {
          warningForm("Os grupos são no máximo de 3 alunos!"); return;
        }
  
        var newElement = document.createElement("div");
        newElement.innerHTML = `<img src="https://www.freeiconspng.com/uploads/clipart--person-icon--cliparts-15.png">
        <div>
            <div class="input">
                <input class="input-field" type="text" placeholder="" required>
                <label class="input-label">Nome</label>
            </div>
            <div class="input">
                <select class="input-field">
                    <option>LEI</option>
                    <option>LEI-PL</option>
                    <option>IGE</option>
                  </select>
                <label class="input-label" >Curso</label>
            </div>
            <div class="input">
                <input class="input-field" type="tel"  pattern="[0-9]{9}" placeholder="" required>
                <label class="input-label">Tel</label>
            </div>
            <div class="input">
                <input class="input-field" type="email" placeholder="" required>
                <label class="input-label" for="">Email</label>
            </div>
        </div>
        <img src="https://cdn0.iconfinder.com/data/icons/octicons/1024/x-512.png" onclick="removeDiv(this)">
          `;
        studentDiv.appendChild(newElement);
      });
    }catch{}
    
    

    
    var asideToggler = document.getElementById("aside-toggler");
    asideToggler.addEventListener("click", function(){
      
      isAsideOn = !isAsideOn;
      const asidePanel = document.getElementById("asidePanel");
      const mainPanel = document.getElementById("mainPanel");
      const headerPanel = document.getElementById("headerPanel");
      asidePanel.style.width = isAsideOn ? "25%" : "0%";
      mainPanel.style.marginRight = isAsideOn ? "25%" : "0%";
      headerPanel.style.marginRight = isAsideOn ? "25%" : "0%";
      

    });

    try{
      document.getElementById("project-form").addEventListener("invalid", function(event){
        event.preventDefault();
        warningForm("Preencha corretamente o formulario");
      }, true);
    }catch{}

    
  });

function removeDiv(img) {
    var divs = document.querySelectorAll("#studentDiv > div");
    

    if (divs.length > 1) {
      img.parentNode.parentNode.removeChild(img.parentNode);
    } else {
      warningForm("O projeto tem que pertencer a pelo menos um aluno");
     
    }
}

function warningForm(msg){
  const asidePanel = document.getElementById("form-console");
  asidePanel.innerText = msg;
}

