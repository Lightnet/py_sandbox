/*
  Project Name: 
  License: MIT
  Created by: Lightnet
*/

import Access from '../../components/auth/AuthAccess.jsx';
import { useAuth } from '../auth/AuthProvider.jsx';
//import ElMobile from '../components/utilities/ElMobile.jsx';
// <ElMobile/>
export default function PageHome() {

  const {user} = useAuth();
  
  return (<>
    <Access>
      <label>Home, {user()}!</label>
    </Access>
  </>)
}