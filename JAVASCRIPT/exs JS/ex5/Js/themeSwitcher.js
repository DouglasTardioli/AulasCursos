export default function () {
  const main = document.querySelector("main");
  const root = document.querySelector(":root");


    if (main.dataset.theme === 'dark') {
      root.style.setProperty('--bg-color', "#f1f5f9")
      root.style.setProperty('--border-color', "#aaa")
      root.style.setProperty('--font-color', "#212529")
      root.style.setProperty('--primary-color', "#26834A")
      root.style.setProperty('--bg-box-color', "#212529")
      main.dataset.theme = 'light'
    } else {
      root.style.setProperty('--bg-color', "#212529")
      root.style.setProperty('--border-color', "#666")
      root.style.setProperty('--font-color', "#f1f5f9")
      root.style.setProperty('--primary-color', "#25f575")
      root.style.setProperty('--bg-box-color', "#161616")
      main.dataset.theme = 'dark'
    }
  
}