const lista = []

function showGallery(ul) {
    const inputPergunta = document.getElementById("inputPergunta").value;

    localStorage.setItem('inputPergunta', inputPergunta)
    console.log(localStorage.getItem('inputPergunta'))
    lista.push(localStorage.getItem('inputPergunta'))
    console.log(lista)

    if (inputPergunta) {
        const li = document.createElement("li");
        li.innerHTML = `
<fieldset class="uk-fieldset">
<legend class="uk-legend">${inputPergunta}</legend>
<div class="uk-margin">
  <input name='pergunta${inputNumber}' class="uk-input" type="text" placeholder="Resposta" aria-label="Input">
</div>
</fieldset>
`;
        ul.appendChild(li);
    }
}

document.getElementById("criar").addEventListener("click", function () {
    const ul = document.querySelector(".uk-list");
    showGallery(ul);
});

document.getElementById("excluir").addEventListener("click", function () {
    const ul = document.querySelector(".uk-list");
    const liElements = ul.querySelectorAll("li");

    if (liElements.length > 0) {
        // Remove o último elemento da lista
        ul.removeChild(liElements[liElements.length - 1]);
        lista.pop(localStorage.getItem('inputPergunta'))
        console.log(lista)
    }
});