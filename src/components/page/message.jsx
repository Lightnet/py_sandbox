/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { Link } from "@solidjs/router";

//import SignIn from "../auth/SignIn.jsx";

export default function PageMessage() {
  return (<>
    <Link href="/"> Home </Link>
    <label>Message</label>
  </>)
}