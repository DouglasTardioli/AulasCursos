import { calculate } from "./calculate.js";
import copyToClipboard from "./copyToClipboard.js";
import {
  handleButtonPress,
  handleClearButton,
  handleTyping,
} from "./keyHandlers.js";
import themeSwitcher from "./themeSwitcher.js";

document.querySelectorAll(".charKey").forEach((charKeyBtn) => {
  charKeyBtn.addEventListener("click", handleButtonPress);
});

document.querySelector("#clear").addEventListener("click", handleClearButton);

document.querySelector("#input").addEventListener("keydown", handleTyping);

// **** CALCULATE **** //
document.querySelector("#equal").addEventListener("click", calculate);

// **** DARK and LIGHT MODE **** //
document
  .querySelector("#themeSwitcher")
  .addEventListener("click", themeSwitcher);

// **** COPIAR CALCULO **** //
document
  .querySelector("#copyToClipboard")
  .addEventListener("click", copyToClipboard);
