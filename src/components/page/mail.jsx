/*
  Project Name: 
  License: MIT
  Created by: Lightnet
*/

import { Link } from "@solidjs/router";

export default function PageMail() {
  return (<>    
    <div style="height:20px;width:100%;background:gray;">
      <Link href="/">Home</Link><span> | </span>
      <label>Mail</label>
    </div>
    <div style="height:calc(100vh - 20px);width:100%;">
      <div style="height:100%;width:200px;background:blue;float:left;">
        Side Bar
      </div>
      <div style="height:100%;width:calc(100% - 200px);background:yellow;float:left;">
        Content
      </div>
    </div>
  </>)
}