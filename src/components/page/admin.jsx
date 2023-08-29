/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

//import AdminView from "../components/admin/AdminView";
import { Link } from '@solidjs/router';
import { createEffect, createSignal } from 'solid-js'

export default function PageAdmin() {

  const [view, setView] = createSignal('home');

  //const [{user}] = useAuth();
  //<AdminView/>
  
  return (<>    
    <div style="height:20px;width:100%;background:gray;">
      <Link href="/">Home</Link><span> | </span>
      <label>Admin</label>
    </div>
    <div style="height:calc(100vh - 20px);width:100%;">
      <div style="height:100%;width:200px;background:blue;float:left;">
        Side Bar
      </div>
      <div style="height:100%;width:calc(100% - 200px);background:yellow;float:left;">
        Content
      </div>
    </div>
  </>)
}