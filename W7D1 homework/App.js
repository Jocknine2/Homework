// import logo from './logo.svg';
import React, {useState} from 'react';
import './App.css';

function App() {

  const [tasks, setTasks] = useState([
    {name: "Cut the Grass", priority: false},
    {name: "Groceries", priority: true},
    {name: "Laundry", priority: false}
  ]);

  const [newTask, setNewTask] = useState ("");

    const taskNodes = tasks.map((task, index)=> {
      return(
      <li  key={index} className={task.priority ? "High":"Low"}><span>{task.name}</span>
      
      </li>
      )
    })

  const handleTaskInput = (event) => {
    setNewTask(event.target.value)
  }

  const handleTaskPri = (event) => {
    SetNewPri(event.target.value)
  }

  const saveNewTask = (event) => {
    event.preventDefault();
    const copyTasks = [...tasks]
    copyTasks.push({name: newTask, priority: newPri })
    setTasks(copyTasks)
    setNewTask("")
    setNewPri(true)
  }


  return (
    <div className="App">

    <h1>ToDo List</h1>
    <hr></hr>

      <form onSubmit={saveNewTask}>
      <label htmlFor="new_task">Add a New Task:</label>
      <input id="new_task" type="text" value={newTask} onChange={handleTaskInput}/>
      <input type="radio" id="High" name="High" value={newPri}></input>
      <label for="priority">High</label>
      <input type="radio" id="Low" name="Low" value={newPri}></input>
      <label for="priority">Low</label>
      <input type="submit" value="Save Task"></input>
      </form>

      <hr></hr>

    <ul>
      {taskNodes}
    </ul>

    </div>

  );
}

export default App;
