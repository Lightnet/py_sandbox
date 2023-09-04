/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { 
  createContext
, createEffect
, createSignal
, onMount, useContext
} from 'solid-js';
//import { jwtUser } from '../../lib/clientapi.js';

export const AuthContext = createContext();

export function useAuth(){return useContext(AuthContext);}

export default function AuthProvider(props){

  const [session, setSession] = createSignal(props.session || null);
  const [token, setToken] = createSignal(props.token || null);
  const [clientDB, setClientDB] = createSignal(props.clientDB || null);
  const [isLogin, setIsLogin] = createSignal(props.clientDB || false);
  const [user, setUser] = createSignal('Guest');
  const [userID, setUserID] = createSignal('');

  const value = {
    session, setSession,
    user, setUser,
    userID, setUserID,
    isLogin, setIsLogin,
    token, setToken,
    clientDB, setClientDB,
    AssignSession(data) {setSession(data);},
    clearSession() {setSession(null);}
  };

  onMount(()=>{
    checkUser()
  })

  async function checkUser(){
    const response = await fetch("/api/auth/user")
    let data = await response.json()
    if(data){
      if(data.api){
        console.log("data.api: ", data.api)
        if(data.api=='USER'){
          console.log("FOUND USER")
          setToken(data.token)
        }
      }
    }
  }

  //watch data
  createEffect(() => {
    //console.log(token())
    let tokenData = token();
    try{
      if(tokenData){
        //let userData = jwtUser(strToken);
        //console.log(userData)
        setUser(tokenData.alias)
        //setUserID(userData.aliasID)
        setIsLogin(true)
      }else{
        setIsLogin(false)
        setUser('Guest')
        setUserID('')
      }
    }catch(e){
      setIsLogin(false)
      setUser('Guest')
      setUserID('')
    }
  })
  

  return (<AuthContext.Provider value={value}>
    {props.children}
  </AuthContext.Provider>)
}