/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { createSignal } from 'solid-js'

export default function UILogs() {
  
  const [count, setCount] = createSignal(0)

  return (
    <>
      <label>Logs </label>
    </>
  )
}