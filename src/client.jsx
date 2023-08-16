/* @refresh reload */
import { render } from 'solid-js/web'

import App from './components/app.jsx'

const root = document.getElementById('root')

render(() => <App />, root)
console.log("client test...")