import React, { useContext, useEffect, useState } from 'react'
import expenseContext from '../../context/expenseContext'

const Home = () => {
  const context=useContext(expenseContext)
  const {prompt,getExpense}=context;
  const initialState = {
		label: "",
		number: "", 
	};

  useEffect(()=>{
    getExpense()
  },[]);
	const [data, setData] = useState(initialState);
  const handleChange=(e)=>{
    setData({...data, [e.target.name]:e.target.value});
  }
  const handleSubmit=(e)=>{
    e.preventDefault();
    prompt(data);
    setData(initialState);

  }
  return (
	<div className='home'>
    <form action="" onSubmit={handleSubmit}>
      <input type="text" name="label" id="" value={data.label} onChange={handleChange}/> 
      <input type="number" name="number" value={data.number} onChange={handleChange} id="" />
      <button type='submit'>submit</button>
    </form>
  </div>
  )
}

export default Home