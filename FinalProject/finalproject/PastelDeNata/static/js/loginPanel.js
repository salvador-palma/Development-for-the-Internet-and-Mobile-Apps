const loginTitle = "PRONTO PARA<br>MAIS UM PASTEL?"
const registerTitle = "A PRIMEIRA DENTADA<br>SABE MELHOR"

const loginSuggestion ="Ainda nao tem conta?"
const registerSuggestion = "Ja tem conta?"

var onLogin = true
function SwitchLoginState(){
    const CoverLoginPanel = document.getElementById("LoginRegisterSwitchPanel");

    if(onLogin){
        CoverLoginPanel.setAttribute("state", "register");
        CoverLoginPanel.children[0].innerHTML=registerTitle
        CoverLoginPanel.children[2].innerHTML=registerSuggestion
    }else{
        CoverLoginPanel.setAttribute("state", "login");
        CoverLoginPanel.children[0].innerHTML=loginTitle
        CoverLoginPanel.children[2].innerHTML=loginSuggestion
    }
    onLogin = !onLogin
}



function SwitchClientType(select){
    const RegisterPanel = document.getElementById("Register-Panel");
    var currentValue = select.value;

    if(currentValue == "individual"){
        RegisterPanel.children[1].placeholder = "Nome Completo"
    }else{
        RegisterPanel.children[1].placeholder = "Nome da Empresa"
    }


}