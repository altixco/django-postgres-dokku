import "../scss/app.scss"
import "bootstrap"

function component() {
  console.log('Hello');
  const element = document.createElement('div');

  // Lodash, currently included via a script, is required for this line to work
  element.innerHTML = 'Hello webpacks';

  return element;
}

document.body.appendChild(component());
