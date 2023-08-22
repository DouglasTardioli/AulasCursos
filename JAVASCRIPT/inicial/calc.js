
let Number1 = parseFloat(window.prompt('Digite primeiro Número: '))
let Number2 = parseFloat(window.prompt('Digite segundo Número: '))

let soma = (Number1 + Number2)
let multi = (Number1 * Number2)
let divisao = (Number1 / Number2)
let sub = (Number1 - Number2)

alert(
  "Números digitados: " + Number1 + " e " + Number2 +
  "\nresultados: " +
  "\nSoma: " + soma +
  "\nMultiplicação: " + multi +
  "\nDivisão: " + divisao +
  "\nSubtração: " + sub
  )