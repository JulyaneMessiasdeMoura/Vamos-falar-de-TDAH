let chat = document.getElementById('chat');
let div_mais = document.getElementById('div_mais');
let botao_mais = document.getElementById('botao_mais');
let botao_menos = document.getElementById('botao_menos');
var exibir = 

console.log(exibir)

function teste(exibir){
    if (exibir == false){
        chat.className='visible';
        console.log(exibir)
    }
    if (exibir == true){
        chat.classList.remove('visible');
        console.log(exibir)
    }
}

function mostrar_mais(){
    div_mais.classList.remove('div_invisivel');

    botao_mais.className='div_invisivel';
    
    botao_menos.classList.remove('div_invisivel');
}
function mostrar_menos(){
    div_mais.className='div_invisivel';

    botao_mais.classList.remove('div_invisivel');

    botao_menos.className='div_invisivel';
}