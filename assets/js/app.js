import "../scss/app.scss"

async function component() {
  return new Promise((res, rej) => {
      setTimeout(() => {
        console.log('Hello');
        const element = document.createElement('div');

        element.innerHTML = 'Hello async';

        res(element);
      }, 4000)
  });
}

async function init() {
  let el = await component();
  document.body.appendChild(el);
}

init();
