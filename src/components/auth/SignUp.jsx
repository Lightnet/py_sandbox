/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { Link, useNavigate } from '@solidjs/router'
import { createEffect, createSignal } from 'solid-js'

export default function SignUp() {

  const [alias, setAlias] = createSignal('test')
  const [passphrase, setPassphrase] = createSignal('test')
  const [email, setEmail] = createSignal('test@test.test')

  const navigate = useNavigate();

  const btnCancel = (e)=>{
    navigate("/", { replace: true })
  }

  const btnSignUp = async (e)=>{
    console.log(alias())
    console.log(passphrase())
    const resp = await fetch('/api/auth/signup',{
      method:'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body:JSON.stringify({
        alias:alias(),
        email:email(),
        passphrase:passphrase()
      })
    })
    const data = await resp.json()
    console.log(data)
  }

  return (<div>
    <table>
      <thead>
            <tr>
              <td colSpan="">
                <label>Sign In</label>
              </td>
            </tr>
          </thead>
        <tbody>
          <tr>
            <td>
              <label> Alias: </label>
            </td>
            <td>
            <input value={alias()} onInput={(e)=>setAlias(e.target.value)}/>
            </td>
          </tr>
          <tr>
            <td>
            <label> E-Mail: </label>
            </td>
            <td>
            <input value={email()} onInput={(e)=>setEmail(e.target.value)}/>
            </td>
          </tr>
          <tr>
            <td>
            <label> Passphrase: </label>
            </td>
            <td>
            <input value={passphrase()} onInput={(e)=>setPassphrase(e.target.value)} />
            </td>
          </tr>
          <tr>
            <td colSpan="2">
              <span style="float:right;">
                <button onClick={btnSignUp}> Register </button>
                <button onClick={btnCancel}> Cancel </button>
              </span>
            </td>
          </tr>
        </tbody>
      </table>  
    </div>)
}
/*
<button onClick={btnSignUp}> Sign Up </button>
      <button onClick={btnCancel}> Cancel </button>
*/
