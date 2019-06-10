
function enviar(){

    var nome = document.getElementById("nome");
    var email = document.getElementById("email");
    var celular = document.getElementById("celular");
    var cpf = document.getElementById("CPF");
    var apelido = document.getElementById("apelido");
    var senha = document.getElementById("senha");
    var cpfim = cpf.length

    if (nome.value === "" && nome.value === '1234567890'){
        alert("nome invalido")
    }

    if (email.value === ''){
        alert("email invalido")
      
    }
    //if (celular.value != '0123456789'){
      //  alert("celular invalido")
    
    if (celular.value === ''){
        alert("celular invalido")
        console.log("celular invalido")
    }
    if (length(celular.value) === 9){
        console.log("celular ok");
    }
    if (cpfim.value < 11 ){
        alert("cpf invalido");
    }
    if (apelido.value === '' && apelido.value === '1234567890'){
        alert('apelido invalido')
    }
    if (length(senha.value)>8){
        console.log('Senha ok')
    }else{
        alert('senha invalida')
    }
    if (senha.value === ''){
        alert('senha invalida')
    }
}

