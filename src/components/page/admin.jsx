/*
  Project Name: solid-js-sandbox
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
    <div>
      <Link href="/"> Home </Link>
      <label>Admin</label>
      
    </div>
  </>)
}