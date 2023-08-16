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
      </Routes>
    </Router>
  </AuthProvider>
  </>)
}

export default App
