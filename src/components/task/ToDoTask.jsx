/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { Link } from "@solidjs/router";
import { createSignal, onMount } from "solid-js";

export default function ToDoTask() {

  const [content, setContent] = createSignal('');
  const [tasks, setTasks] = createSignal([]);

  onMount(()=>{
    console.log("init list")
    get_tasks()
  })

  async function get_tasks(){
    try{
      const response = await fetch("/api/task")
      const data = await response.json()
      console.log(data)

      if(data){
        setTasks(data)
      }

    }
    catch(e){
        console.log(e);
    }
  }

  async function create_task(){
    console.log("content:", content())
    try{
      const response = await fetch("/api/task",{
        method:'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body:JSON.stringify({
          content:content(),
        })
      })
      const data = await response.json()
      console.log(data)
      if(data){

      }
    }catch(e){
      console.log(e)
    }
  }

  return (<>
    <Link href="/"> Home </Link><br/>
    <label>To Do Task!</label><br/>
    <input value={content()} onInput={(e)=>setContent(e.target.value)}></input>
    <button onClick={create_task}> Add </button>
  </>)
}