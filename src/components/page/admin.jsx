/*
  Project Name: solid-js-sandbox
  License: MIT
  Created by: Lightnet
*/

import AdminView from "../components/admin/AdminView";
import { createEffect, createSignal } from 'solid-js'

export default function PageAdmin() {

  const [view, setView] = createSignal('home');

  //const [{user}] = useAuth();

  return (<>
    <div>
      <label>Admin</label>
      <AdminView/>
    </div>
  </>)
}