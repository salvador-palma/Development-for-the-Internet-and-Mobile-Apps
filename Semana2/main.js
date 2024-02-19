var Theme = {LIGHT: 'light' , DARK : 'dark'};
var isAsideOn = false;

document.addEventListener("DOMContentLoaded", () => {
    const htmlElement = document.documentElement;
    var addStudent = document.getElementById("addStudentButton");
    var studentDiv = document.getElementById("studentDiv");
    const themeButton = document.getElementById("theme-toggler");
    const iscteLogo = document.getElementById("iscteLogo");
  
    // themeButton.addEventListener("click", function(){
    //   var currentTheme = htmlElement.getAttribute("data-theme");
    //   var newTheme = currentTheme === 'light' ? 'dark' : 'light';
    //   htmlElement.setAttribute("data-theme", newTheme); 
      
    //   if(newTheme == "dark") iscteLogo.setAttribute("src", "Negative Logo.png");
    //   else iscteLogo.setAttribute("src", "Logo.png");
      
    // });

    addStudent.addEventListener("click", function() {

      var divs = document.querySelectorAll("#studentDiv > div");
    
      if (divs.length == 3) {
        alert("Os grupos são no máximo de 3 alunos!"); return;
      }

      var newElement = document.createElement("div");
      newElement.innerHTML = `
        <strong>Aluno:</strong>
        <div class="input">
          <label class="input-label">Nome</label>
          <input class="input-field" type="text" placeholder="" required>
        </div>
        <div class="input">
          <label class="input-label">Numero</label>
          <input class="input-field" type="number" placeholder="" required>
        </div>
        <div class="input">
          <label class="input-label">Email</label>
          <input class="input-field" type="email" placeholder="" required>
        </div>

        <button onclick="removeDiv(this)"><img src="https://icon-library.com/images/white-cross-icon/white-cross-icon-3.jpg"></button>
          <br>
        `;
      studentDiv.appendChild(newElement);
    });

    
    var asideToggler = document.getElementById("aside-toggler");
    asideToggler.addEventListener("click", function(){
      console.log("isAsideOn");
      isAsideOn = !isAsideOn;
      const asidePanel = document.getElementById("asidePanel");
      const mainPanel = document.getElementById("mainPanel");
      const headerPanel = document.getElementById("headerPanel");
      asidePanel.style.width = isAsideOn ? "25%" : "0%";
      mainPanel.style.marginRight = isAsideOn ? "25%" : "0%";
      headerPanel.style.marginRight = isAsideOn ? "25%" : "0%";
      

    });


  });

function removeDiv(button) {
    var divs = document.querySelectorAll("#studentDiv > div");
    

    if (divs.length > 1) {
      button.parentNode.parentNode.removeChild(button.parentNode);
    } else {
      alert("O projeto tem que pertencer a pelo menos um aluno");
    }
}