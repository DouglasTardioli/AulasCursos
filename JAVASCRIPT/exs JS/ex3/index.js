function addPlayer() {
  const position = document.querySelector('#position').value
  const name = document.querySelector('#name').value
  const number = document.querySelector('#number').value

  const confirmation = confirm(`Escalar ${name} como ${position}?`)

  if (confirmation) {
    const teamList = document.querySelector('#teamList')
    const playerItem = document.createElement('li')
    playerItem.id = 'player-' + number
    playerItem.innerText = `${position} ${name} (${number})`
    teamList.appendChild(playerItem)
    
    document.querySelector('#position').value = ''
    document.querySelector('#name').value =  ''
    document.querySelector('#number').value = ''
  }
}
function removePlayer() {
  const number = document.getElementById('numberToRemove').value
  const playerToRemove = document.getElementById('player-' + number)

  const confirmation = confirm('Remover Jogador ' + playerToRemove.innerText + '?')

  if(confirmation) {
    document.getElementById('teamList').removeChild(playerToRemove)
    document.getElementById('numberToRemove').value = ''
  }
}