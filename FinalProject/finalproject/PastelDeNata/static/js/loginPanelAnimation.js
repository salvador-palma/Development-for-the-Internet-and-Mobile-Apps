const loginTitle = "PRONTO PARA<br>MAIS UM PASTEL?"
const registerTitle = "A PRIMEIRA DENTADA<br>SABE MELHOR"

const loginSuggestion ="Ainda nao tem conta?"
const registerSuggestion = "Ja tem conta?"

var onLogin = true;
document.addEventListener("DOMContentLoaded", (event) => {

    // const CoverLoginPanel = document.getElementById("LoginRegisterSwitchPanel");
    // const SuggestionButton = document.getElementById("SuggestionLogin");
    // SuggestionButton.addEventListener(onclick, function (){SwitchLoginState()})

});

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