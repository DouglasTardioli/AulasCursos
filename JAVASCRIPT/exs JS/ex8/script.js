const elementos = [
  { tag: "h1", texto: "Alooo policia federal uiiiu" },
  { tag: "div", texto: "Frase 2" },
  { tag: "p", texto: "Frase 3" },
  { tag: "footer", texto: "Frase 4" },
];

const container = document.querySelector(".container");
const div = document.createElement("div");

for (let i = 0; i < elementos.length; i++) {
  let { tag, texto } = elementos[i];
  let createdTag = document.createElement(tag);
  let createdText = document.createTextNode(texto);

  createdTag.appendChild(createdText);
  div.appendChild(createdTag);
}

container.appendChild(div);
