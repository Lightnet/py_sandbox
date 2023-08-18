/*
  Project Name: solid-js-sandbox
  License: MIT
  Created by: Lightnet
*/

//import { createEffect, createSignal } from 'solid-js'
import { useNavigate } from '@solidjs/router'
import { useAuth } from './AuthProvider.jsx'

export default function SignOut() {

  const {setToken} = useAuth();

  const navigate = useNavigate();

  const btnSignOut = async (e)=>{
    try{
      fetch('/api/auth/signout',{
        method:"POST",
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body:JSON.stringify({
          api:"LOGOUT"
        })
      })
      setToken(null)
      navigate("/", { replace: true })
    }catch(e){
      console.log(e)
    }
  }

  const btnCancel = (e)=>{
    navigate("/", { replace: true })
  }

  return (
    <div>
      <label> Do you want to Logout?</label><br/>
      <button onClick={btnCancel}> Cancel </button>
      <button onClick={btnSignOut}> Submit </button>
    </div>
  )
}