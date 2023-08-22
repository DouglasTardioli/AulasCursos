const num = Number(prompt('DIgite um número: '))


const numTitle = document.getElementById('title')
const textMain = document.getElementById('text')

numTitle.innerHTML = num
textMain.innerHTML += `<p>Raiz quadrada:  ${num ** 0.5}.</p>`
textMain.innerHTML += `<p>${num} é inteiro:  ${Number.isInteger(num)}.</p>`
textMain.innerHTML += `<p>é NaN:  ${Number.isNaN(num)}.</p>`
textMain.innerHTML += `<p>Arredondando para cima:  ${Math.ceil(num)}.</p>`
textMain.innerHTML += `<p>Arredondando para baixo:  ${Math.floor(num)}.</p>`
textMain.innerHTML += `<p>Com duas casas decimais:  ${num.toFixed(2)}.</p>`
