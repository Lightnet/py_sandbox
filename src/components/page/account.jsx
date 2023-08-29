/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { useAuth } from '../auth/AuthProvider.jsx';
import AuthAccess from '../auth/AuthAccess.jsx';
import { Link } from '@solidjs/router';

export default function PageAccount() {

  const [,{isLogin}] = useAuth();
  //<Account/>
  return (<AuthAccess>
    <div>
      <Link href="/"> Home </Link>
      <label>Account</label>
    </div>
    
  </AuthAccess>)
}