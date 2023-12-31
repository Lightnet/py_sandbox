/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { createSignal } from 'solid-js'
//import solidLogo from './assets/solid.svg'
//import viteLogo from '/vite.svg'
//import './App.css'

function ButtonCount() {
  const [count, setCount] = createSignal(0)

  return (
    <>
      <label>Count: {count()} </label>
      <button onClick={()=>setCount(count()+1)}>+</button>
      <button onClick={()=>setCount(count()-1)}>-</button>
    </>
  )
}

export default ButtonCount
