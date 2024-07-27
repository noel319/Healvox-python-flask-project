function scrollToSites() {
    // Obtém a posição vertical da descrição
    var descricaoPosition = document.getElementById('sites').offsetTop;

    // Rola a página até a posição da descrição
    window.scrollTo({
      top: descricaoPosition,
      behavior: 'smooth' // Adiciona um efeito de rolagem suave
    });
}

function scrollToSoftware() {
    // Obtém a posição vertical da descrição
    var descricaoPosition = document.getElementById('software').offsetTop;

    // Rola a página até a posição da descrição
    window.scrollTo({
      top: descricaoPosition,
      behavior: 'smooth' // Adiciona um efeito de rolagem suave
    });
}

function scrollToAutomacao() {
    // Obtém a posição vertical da descrição
    var descricaoPosition = document.getElementById('automacao').offsetTop;

    // Rola a página até a posição da descrição
    window.scrollTo({
      top: descricaoPosition,
      behavior: 'smooth' // Adiciona um efeito de rolagem suave
    });
}

function scrollToAnalise() {
    // Obtém a posição vertical da descrição
    var descricaoPosition = document.getElementById('analise').offsetTop;

    // Rola a página até a posição da descrição
    window.scrollTo({
      top: descricaoPosition,
      behavior: 'smooth' // Adiciona um efeito de rolagem suave
    });
}

function scrollToFooter() {
    // Obtém a posição vertical da descrição
    var descricaoPosition = document.getElementById('footer').offsetTop;

    // Rola a página até a posição da descrição
    window.scrollTo({
      top: descricaoPosition,
      behavior: 'smooth' // Adiciona um efeito de rolagem suave
    });
}

/* ============================================================ LOG IN ============================================================*/

var formSignin = document.querySelector('#signin')
var formSignup = document.querySelector('#signup')
var btnColor = document.querySelector('.btnColor')

document.querySelector('#btnSignin')
  .addEventListener('click', () => {
    formSignin.style.left = "25px"
    formSignup.style.left = "450px"
    btnColor.style.left = "0px"
})

document.querySelector('#btnSignup')
  .addEventListener('click', () => {
    formSignin.style.left = "-450px"
    formSignup.style.left = "25px"
    btnColor.style.left = "120px"
})