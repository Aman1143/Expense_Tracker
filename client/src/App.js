import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import './App.css';
import ExpenseState from './context/ExpenseState';
import { Routes, Route } from 'react-router-dom'
import Auth from './pages/auth/Auth';
import Home from './pages/home/Home';
import Navbar from './components/Navbar';

function App() {
  const token = JSON.stringify(localStorage.getItem('token'));
  return (

    <>
      <ExpenseState>
        <Routes>
          <Route path='/' element={<Auth />} />
          <Route path='/home' element={token ?<Home />:<Auth />} />
          <Route path='/navbar' element={token?<Navbar />:<Auth />} />
        </Routes>
      </ExpenseState>
    </>
  
  )
}

export default App;
