/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { createSignal } from 'solid-js'

export default function Members() {
  
  const [count, setCount] = createSignal(0)

  return (
    <>
      <label>Maintenance Mode: {count()} </label>
      <button onClick={()=>setCount(count()+1)}>On</button>
      <button onClick={()=>setCount(count()-1)}>Off</button>
    </>
  )
}