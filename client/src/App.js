import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import './App.css';
import ExpenseState from './context/ExpenseState';
import { Routes, Route } from 'react-router-dom'
import Auth from './pages/auth/Auth';
import Home from './pages/home/Home'; 

function App() {  
  return (

    <>
      <ExpenseState>
        <Routes>
          <Route path='/' element={<Auth />} />
          <Route path='/home' element={ <Home /> } />
        </Routes>
      </ExpenseState>
    </>
  )

}

export default App;
