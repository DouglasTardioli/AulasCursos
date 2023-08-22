let name = window.prompt("Digite seu Primeiro nome: ")
let sobreName = window.prompt("Digite seu sobrenome: ")
let CampStud = window.prompt("Digite seu campo de estudo: ")
let YearNasci = window.prompt("Digite seu ano de nascimento: ")


let CalcIdade = 2023 - YearNasci

alert(
"Recruta Salvo com sucesso!\n" + 
"\nSeu nome completo: " + name + " " + sobreName +
"\nCampo de estudo: " + CampStud +
"\nSua Idade: " + CalcIdade
)