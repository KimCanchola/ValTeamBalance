import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import HomePage from "./pages/HomePage"
import Error from "./pages/Error"
import Help from "./pages/Help"
import ManualInput from "./pages/ManualInput"
import Results from "./pages/Results"
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <div id="page-body">
          <Route path="/" component={HomePage} exact />
          <Route path="/error" component={Error} exact />
          <Route path="/help" component={Help} exact />
          <Route path="/form" component={ManualInput} exact />
          <Route path="/results" component={Results} exact />
        </div>
      </div>
    </Router>

  );
}

export default App;
