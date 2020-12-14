import React, { useState } from "react"
import ReactDom from "react-dom"
import { BrowserRouter, Switch, Route } from "react-router-dom"
import Axios from "axios"
Axios.defaults.baseURL = "http://127.0.0.1:8000/api/"
// My components
import Header from "./components/Header"
import HomeGuest from "./components/HomeGuest"
import Home from "./components/Home"
import Footer from "./components/Footer"
import About from "./components/About"
import Terms from "./components/Terms"
import ViewRegData from "./components/ViewRegData"
import FlashMessages from "./components/FlashMessages"
import ExampleContext from "./ExampleContext"

function Main() {
  const [loggedIn, setLoggedIn] = useState(Boolean(localStorage.getItem("token")))
  const [flashMessages, setFlashMessages] = useState([])

  function addFlashMessage(msg) {
    setFlashMessages((prev) => prev.concat(msg))
  }

  return (
    <ExampleContext.Provider value={{ addFlashMessage, setLoggedIn }}>
      <BrowserRouter>
        <FlashMessages messages={flashMessages} />
        <Header loggedIn={loggedIn} />
        <Switch>
          <Route path="/" exact>
            {loggedIn ? <Home /> : <HomeGuest />}
          </Route>
          <Route path="/about-us">
            <About />
          </Route>
          <Route path="/terms">
            <Terms />
          </Route>
          <Route path="/view-data/:email">
            <ViewRegData />
          </Route>
        </Switch>

        <Footer />
      </BrowserRouter>
    </ExampleContext.Provider>
  )
}

ReactDom.render(<Main />, document.querySelector("#app"))

// added for asyn load
if (module.hot) {
  module.hot.accept()
}
