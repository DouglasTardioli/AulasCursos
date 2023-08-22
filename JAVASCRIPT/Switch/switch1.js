const medida = prompt('Insira uma medida em metros: ')

const unit = prompt(
  "Para qual unidade de medida deseja converter?" +
  "\n1. milímetros (mm)" +
  "\n2. centímetros (cm)" +
  "\n3. decímetros (dm)" +
  "\n4. decâmetros (dam)" +
  "\n5. hectômetros (hm)" +
  "\n6. quilômetros (km)" 
)

switch (unit) {
  case "1":
    alert(`resultado: ${medida}m = ${medida * 1000}mm`)
    break
  case "2":
    alert(`resultado: ${medida}m = ${medida * 100}cm`)
    break
  case "3":
    alert(`resultado: ${medida}m = ${medida * 10}dm`)
    break
  case "4":
    alert(`resultado: ${medida}m = ${medida / 10}dam`)
    break
  case "5":
    alert(`resultado: ${medida}m = ${medida / 100}hm`)
    break
  case "6":
    alert(`resultado: ${medida}m = ${medida / 1000}km`)
    break
  default:
    alert('Opção Inválida!!!')
}