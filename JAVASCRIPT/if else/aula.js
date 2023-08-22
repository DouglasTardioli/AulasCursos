const carro1 = prompt("Digite Nome carro 1: ")
const velo1 = prompt("Digite Velocidade carro 1: ")

const carro2 = prompt("Digite Nome carro 2: ")
const velo2 = prompt("Digite Velocidade carro 2: ")


if (velo1 > velo2) {
  alert(`Velocidade do ${carro1}, ${velo1}km/h maior que a do ${carro2}, ${velo2}km/h`)
} else if (velo2 > velo1){
  alert(`Velocidade do ${carro2}, ${velo2}km/h maior que a do ${carro1}, ${velo1}km/h`)
} else {
  alert('Velocidade dos carros iguais')
}