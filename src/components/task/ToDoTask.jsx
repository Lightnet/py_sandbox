/*
  Project Name: py_sandbox
  License: MIT
  Created by: Lightnet
*/

import { Link } from "@solidjs/router";
import { createSignal, onMount, For } from "solid-js";

export default function ToDoTask() {

  const [content, setContent] = createSignal('');
  const [tasks, setTasks] = createSignal([]);

  const [editId, setEditId] = createSignal('');
  const [editContent, setEditContent] = createSignal('');

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
      console.log("List error! ",e);
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
        if(data.api == 'CREATED'){
          console.log("ADDING...")
          setTasks(state=>[...state,{
            id:data.id,
            content:content(),
            isDone:false
          }])
        }
      }
    }catch(e){
      console.log(e)
    }
  }

  function task_edit(id){
    setEditId(id)
    
    let task = tasks().find(item=>item.id == id)
    setEditContent(task.content)
    console.log(task.content)
  }

  async function task_update(){
    try{
      const response = await fetch(`/api/task/${editId()}`,{
        method:'PUT',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body:JSON.stringify({
          id:editId(),
          content:editContent(),
        })
      })
      const data = await response.json()
      console.log("update data: ",data)
      if(data){
        //setContent()
        if(data.api == 'UPDATE'){
          console.log("UPDATE...")
          setTasks(state=>state.map(item=>{
            console.log("item: ",item);
            if (item.id == editId()){
              console.log("FOUND ID:", item.id)
              item.content = editContent()
              return item;
            }
            return item;
          }))
          setEditId('')
        }
      }
    }catch(e){
      console.log(e)
    }
  }

  async function task_delete(id){
    console.log("ID: ", id)
    try{
      const response = await fetch(`/api/task/${id}`,{
        method:'DELETE'
      })
      const data = await response.json()
      console.log("delete data: ",data)
      if(data){
        //setContent()
        if(data.api == 'DELETE'){
          setTasks(state=>state.filter(item=>item.id !== id))
        }
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
    <table>
      <tbody>
        <tr>
          <td>
            Tasks:
          </td>
          <td>
            Actions:
          </td>
        </tr>
        <For each={tasks()}>{(tasks, i) =>
          <tr>
            <td>
              {editId() == tasks.id ?<input value={editContent()} onInput={(e)=>setEditContent(e.target.value)}></input>:<label>{tasks.content}</label>}
            </td>
            <td>
              {editId() == tasks.id ? <button onClick={()=>task_update()}>Update</button>: <button onClick={()=>task_edit(tasks.id)}>Edit</button>}
              
              <button onClick={()=>task_delete(tasks.id)}>Delete</button>
            </td>
          </tr>
        }</For>

      </tbody>
    </table>
  </>)
}