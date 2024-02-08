document.addEventListener("DOMContentLoaded", () => {
    var addStudent = document.getElementById("addStudentButton");
    var studentDiv = document.getElementById("studentDiv");
  
    addStudent.addEventListener("click", function() {
      var newElement = document.createElement("div");
      newElement.innerHTML = `
            <strong>Aluno:</strong>
            <label>Nome</label>
            <input type="text" required>
            <label>Numero</label>
            <input type="number" required>
            <label>Email</label>
            <input type="email" required>
            <button onclick="removeDiv(this)" type="button">Remover</button>
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