const name = prompt('Digite seu nome completo: ')



document.body.innerHTML += `o seu nome é: <strong>${name}</strong><br />`
document.body.innerHTML += `seu nome tem ${name.length} letras.<br />`
document.body.innerHTML += `a segunda letra do seu nome é: ${name[1]}<br />`
document.body.innerHTML += `Qual o primeiro índice na letra a no seu nome: ${name.indexOf('a')}<br />`
document.body.innerHTML += `Qual o ultimo índice na letra a no seu nome: ${name.lastIndexOf('a')}<br />`
document.body.innerHTML += `As ultimas 3 letras do seu nome são: ${name.slice(-3)}<br />`
document.body.innerHTML += `as palavras do seu nome são: ${name.split(' ')}<br />`
document.body.innerHTML += `seu nome com letras maíusculas: ${name.toUpperCase()}<br />`
document.body.innerHTML += `seu nome com letras minusculas: ${name.toLowerCase()}<br />`