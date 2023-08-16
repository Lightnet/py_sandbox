/*
  Project Name: solid-js-sandbox
  License: MIT
  Created by: Lightnet
*/

import { useAuth } from '../components/auth/auth.jsx';
import AuthAccess from '../components/auth/AuthAccess.jsx';

export default function PageAccount() {

  const [,{isLogin}] = useAuth();

  return (<AuthAccess>
    <div>
      <label>Account</label>
    </div>
    <Account/>
  </AuthAccess>)
}