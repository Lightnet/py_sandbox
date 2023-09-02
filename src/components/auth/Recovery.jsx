/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { createSignal } from 'solid-js';

export default function Recovery(){

  const [count, setCount] = createSignal(0)

  return (<>
    <table>
      <tbody>
        <tr>
          <td colSpan={2}>
            <center>
              <label>Recovery:</label>
            </center>
          </td>
        </tr>
        <tr>
          <td>
            <label>Email:</label>
          </td>
          <td>
            <input placeholder='E-Mail'></input>
          </td>
        </tr>
        <tr>
          <td colSpan={2}>
            <button style="width:100%;">Request</button>
          </td>
        </tr>
        <tr>
          <td colSpan={2}>
            <button style="width:100%;">Cancel</button>
          </td>
        </tr>
      </tbody>
    </table>
  </>)
};
