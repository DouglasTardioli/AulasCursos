const atacante = prompt("Qual o nome do personagem de ataque? ") 
const attack= prompt("Qual o poder de ataque dele? ") 


const defensor = prompt("Qual o nome do personagem de defesa? ")
let pontosDeVida = prompt('Quantos pontos de vida ele possui?') 
const defesa = prompt("Qual o seu poder de defesa? ")
const possuiEscudo = prompt("Ele possui um escudo? (S/N)")


let danoCausado = 0

if (attack > defesa && possuiEscudo === "N") {
  danoCausado = attack - defesa
} else if (attack > defesa && possuiEscudo === "S") {
  danoCausado = (attack - defesa) / 2
}

pontosDeVida -= danoCausado

alert(`${atacante} causou ${danoCausado} pontos de dano em ${defensor}`)
alert(`${atacante} poder de ataque:  ${attack}
       ${defensor} pontos de vida: ${pontosDeVida}
       poder de defesa: ${defesa}
       possui escudo: ${possuiEscudo}`)