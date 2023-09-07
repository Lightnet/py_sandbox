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
      <label>Members: </label>
      <table>
        <tbody>
          <tr>
            <td>
              <label>Name:</label>
            </td>
            <td>
              <label>Role:</label>
            </td>
            <td>
              <label>Actions:</label>
            </td>
          </tr>

          
        </tbody>
      </table>
    </>
  )
  //<button onClick={()=>setCount(count()+1)}>On</button>
  //<button onClick={()=>setCount(count()-1)}>Off</button>
}