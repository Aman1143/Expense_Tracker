import React, { useContext, useEffect, useState } from 'react'
import expenseContext from '../../context/expenseContext'

const Home = () => {
  const context=useContext(expenseContext)
  const {prompt,getPredictionOutput}=context;
  const initialState = {
		label: "",
		number: "", 
	}; 
	const [data, setData] = useState(initialState);
  const [sentance,setStance]=useState();
  const handleChange=(e)=>{
    setData({...data, [e.target.name]:e.target.value});
  }
  const handleSubmit=(e)=>{
    e.preventDefault();
    // prompt(data);
    // setData(initialState);
    console.log(sentance)
    getPredictionOutput( {sentance:sentance}) 

  }
  return (
	<div className='home'>
    <form action="" onSubmit={handleSubmit}>
      {/* <input type="text" name="label" id="" value={data.label} onChange={handleChange}/> 
      <input type="number" name="number" value={data.number} onChange={handleChange} id="" /> */}
      <input type="text" name="sentance" id="" value={sentance} onChange={(e)=>setStance(e.target.value)} />
      <button type='submit'>submit</button>
    </form>
  </div>
  )
}

export default Home