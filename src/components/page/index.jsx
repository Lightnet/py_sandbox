/*
  Project Name: 
  License: MIT
  Created by: Lightnet
*/

import { Link } from '@solidjs/router';
import Access from '../../components/auth/AuthAccess.jsx';
import { useAuth } from '../auth/AuthProvider.jsx';
//import ElMobile from '../components/utilities/ElMobile.jsx';
// <ElMobile/>
export default function PageHome() {

  const {user} = useAuth();
  
  return (<>
    <Access>
      <div>
        <Link href='/account'>Account</Link><span> | </span>
        <Link href='/entity'>Entity</Link><span> | </span>
        <Link href='/message'>Message</Link><span> | </span>
        <Link href='/mail'>Mail</Link><span> | </span>
        <Link href='/settings'>Settings</Link><span> | </span>
        <Link href='/admin'>Admin</Link><span> | </span>
        <Link href='/signout'>Logout</Link><span> | </span>
      </div>
      <div>
        <label>Home, {user()}!</label>
      </div>
    </Access>
  </>)
}