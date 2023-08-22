const parágrafos = document.querySelectorAll('p')

const styleBody = getComputedStyle(document.body)
const backgroundBody = styleBody.backgroundColor

console.log(backgroundBody)

for (let p of parágrafos) {
  p.style.padding = '8px'
  p.style.marginTop = '8px'
  p.style.borderRadius = '16px'
  p.style.backgroundColor = backgroundBody
  p.style.Color = '#FFF'
}