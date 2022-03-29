function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function myFunction() {
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  setInterval(3000);
}
  
document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }
    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

  let tags = document.getElementsByClassName("tag");
  for (let i = 0; i < tags.length; i++) {
    let tag = tags[i];
    tag.className += ` tag-color-${getRandomInt(
      1,
      3
    )} tag-rotation-${getRandomInt(1, 3)}`;
  }

  let tagsu = document.getElementsByClassName("tagutil");
  for (let i = 0; i < tagsu.length; i++) {
    let tag = tagsu[i];
    tag.className += ` tagutil-color-${getRandomInt(
      1,
      3
    )} tagutil-rotation-${getRandomInt(1, 3)}`;
  }
});

//Reseta a página a cada 2minutos, evita deixar os cartões com cores e posições iguais
setTimeout(function () { location.reload(true); }, 120000);

//Muda posição e cores sem recarregar a página
setInterval(function(){
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    console.log(card.classList)
    card.classList = [`card card-color-${getRandomInt(1,5)} card-rotation-${getRandomInt(1, 11)}`]
  }
},1000);

  setInterval(function(){
    let tags = document.getElementsByClassName("tag");
    for (let i = 0; i < tags.length; i++) {
      let tag = tags[i];
      tag.classList = [`tag tag-color-${getRandomInt(1,3)} tag-rotation-${getRandomInt(1, 3)}`]
    }
},1000);

setInterval(function(){
  let tags = document.getElementsByClassName("tagutil");
  for (let i = 0; i < tags.length; i++) {
    let tag = tags[i];
    tag.classList = [`tagutil tagutil-color-${getRandomInt(1,3)} tagutil-rotation-${getRandomInt(1, 3)}`]
  }
},1000);







