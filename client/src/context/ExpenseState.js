import ExpenseContext from "./expenseContext";
import axios from 'axios';
import { useNavigate } from 'react-router-dom'

import React, { useState } from 'react'

const ExpenseState = (props) => {
  const [user,setUser]=useState();
  const API = axios.create({ baseURL: 'http://localhost:8000' })
  const navigate = useNavigate(); 

  const handleRegister = async (data) => {
    try {
      let response = await axios.post('http://localhost:8000/api/resgister/', data, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token') || ""}`
        }
      })
      response=await response.data
      if (response.success) {
				setUser(response.user);
				localStorage.setItem('token', response.token);
        console.log(response.token);
				navigate("/home", { new: true });
			} 
    } catch (error) {
      console.log(error)
    }
  }

  const handleLogin = async (data) => {
    try {
      let response = await axios.post('http://localhost:8000/api/login/', data, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token') || ""}`
        }
      })
      response=response.data; 
      if (response.success) {
				setUser(response.user);
				localStorage.setItem('token', response.token);
        console.log(response.token);
				navigate("/home", { new: true });
			} 
    } catch (error) {
      console.log(error)
    }
  }

  const getExpense = async () => {
    try {
      let response = await axios.get('http://localhost:8000/api/getExpense/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token') || ""}`
        }
      }) 
      response=await response.data 
      if(response.success){
        console.log(response)
      }
    } catch (error) {
      console.log(error)
    }
  }

  const getPredictionOutput = async (data) => {
    try {
      let response = await axios.post('http://localhost:8000/api/getPredictionOutput/',data, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token') || ""}`
        }
      }) 
      response=await response.data 
      if(response.success){
        console.log(response)
      }
    } catch (error) {
      console.log(error)
    }
  }

  const prompt = async (data) => {
    try {
      let response = await axios.post('http://localhost:8000/api/prompt/', data, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token') || ""}`
        }
      }) 
      response=await response.data 
      console.log(response)
      navigate('/navbar',{new:true})
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <ExpenseContext.Provider value={{ handleLogin, handleRegister,prompt ,getExpense,getPredictionOutput}}>
      {props.children}
    </ExpenseContext.Provider>
  )

}

export default ExpenseState