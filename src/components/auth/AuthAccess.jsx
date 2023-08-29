/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

//import { createSignal} from 'solid-js';
import { createEffect } from "solid-js";
import { useAuth } from "./AuthProvider.jsx";
import SignIn from "./SignIn.jsx";

export default function AuthAccess(props){

  const {isLogin} = useAuth();

  createEffect(()=>{
    console.log("isLogin:", isLogin());
  })

  //return (<>{props.children}</>)

  return (<>
    {isLogin()?(<>
      {props.children}
    </>):(<>
      <SignIn/>
    </>)}
  </>)
}