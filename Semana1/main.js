document.addEventListener("DOMContentLoaded", () => {
    var addStudent = document.getElementById("addStudentButton");
    var studentDiv = document.getElementById("studentDiv");
  
    addStudent.addEventListener("click", function() {
      var divs = document.querySelectorAll("#studentDiv > div");
    
      if(divs.length == 3){
        alert("Os grupos teem que ser formados por 3 alunos no maximo");
        return;
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

    
  });

function removeDiv(button) {
    var divs = document.querySelectorAll("#studentDiv > div");
    
    if (divs.length > 1) {
      button.parentNode.parentNode.removeChild(button.parentNode);
    } else {
      alert("O projeto tem que pertencer a pelo menos um aluno");
    }
}