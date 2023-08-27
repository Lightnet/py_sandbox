import { createSignal, lazy } from 'solid-js'
import { Router, Routes, Route } from '@solidjs/router';
import AuthProvider from './auth/AuthProvider.jsx';
//import solidLogo from './assets/solid.svg'
//import viteLogo from '/vite.svg'
//import './App.css'
//import ButtonCount from "./buttoncount.jsx"
const Home = lazy(() => import('./page/index.jsx'))
const SignIn = lazy(() => import('./page/login.jsx'))
const SignUp = lazy(() => import('./page/register.jsx'))
const SignOut = lazy(() => import('./page/logout.jsx'))

const Account = lazy(() => import('./page/account.jsx'))
const Admin = lazy(() => import('./page/admin.jsx'))
const Settings = lazy(() => import('./page/settings.jsx'))

const Entity = lazy(() => import('./page/entity.jsx'))

const Message = lazy(() => import('./page/message.jsx'))
const EMail = lazy(() => import('./page/mail.jsx'))

function App() {
  const [count, setCount] = createSignal(0)

  return (<>
  <AuthProvider>
    <Router>
      <Routes>
        <Route path="/" component={Home}/>
        <Route path="/signin" component={SignIn}/>
        <Route path="/signup" component={SignUp}/>
        <Route path="/signout" component={SignOut}/>

        <Route path="/account" component={Account}/>
        <Route path="/message" component={Message}/>
        <Route path="/settings" component={Settings}/>
        <Route path="/admin" component={Admin}/>

        <Route path="/entity" component={Entity}/>
        <Route path="/mail" component={EMail}/>
      </Routes>
    </Router>
  </AuthProvider>
  </>)
}

export default App
