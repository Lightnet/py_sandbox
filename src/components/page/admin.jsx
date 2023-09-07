/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

//import AdminView from "../components/admin/AdminView";
import { Link } from '@solidjs/router';
import { createEffect, createSignal, createMemo  } from 'solid-js'
import AdminHome from '../admin/Home';
import GroupManagement from '../admin/GroupManagement';
import Members from '../admin/Members';
import UILogs from '../admin/Logs';

export default function PageAdmin() {

  const [view, setView] = createSignal('home');

  //const [{user}] = useAuth();
  //<AdminView/>

  const viewContent = createMemo(()=>{
    if (view() == 'home'){
      return <AdminHome/>
    }
    if (view() == 'members'){
      return <Members/>
    }
    if (view() == 'groups'){
      return <GroupManagement/>
    }
    if (view() == 'logs'){
      return <UILogs/>
    }

    return null
  })
  
  return (<>    
    <div style="height:20px;width:100%;">
      <Link href="/">Home</Link><span> | </span>
      <label>Admin</label><span> | </span>
      <label>Theme</label><span> | </span>
      <label>Settings</label><span> | </span>
    </div>
    <div style="height:calc(100vh - 20px);width:100%;">
      <div style="height:100%;width:200px;float:left;">
        <button onClick={(e)=>setView('home')}> Home </button> <br/>
        <button onClick={(e)=>setView('members')}> Members </button><br/>
        <button onClick={(e)=>setView('groups')}> Groups </button><br/>
        <button onClick={(e)=>setView('Applications')}> Applications </button><br/>
        <button onClick={(e)=>setView('access')}> Access </button><br/>
        <button onClick={(e)=>setView('logs')}> Logs </button><br/>
      </div>
      <div style="height:100%;width:calc(100% - 200px);float:left;">
        {viewContent()}
      </div>
    </div>
  </>)
}