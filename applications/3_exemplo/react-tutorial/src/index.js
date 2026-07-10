import React, { Component } from 'react'
import { createRoot } from 'react-dom/client' // Mudança aqui
import './index.css'
import App from './App'

// Nova forma de renderizar no React 18+
const container = document.getElementById('root')
const root = createRoot(container)
root.render(<App />)
