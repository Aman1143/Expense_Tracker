import React, { useContext, useEffect } from 'react'
import expenseContext from '../context/expenseContext';

const Navbar = () => {
  const context = useContext(expenseContext)
  const { getExpense } = context;
  useEffect(() => {
    getExpense();
  }, [])
  return (
    <div>
      Welcome to Navbar
    </div>
  )
}

export default Navbar