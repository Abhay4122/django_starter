import React, { useEffect, useState, useContext } from "react"
import Page from "./Page"
import Axios from "axios"
import Swal from "sweetalert2"
import { withRouter } from "react-router-dom"
import ExampleContext from "../ExampleContext"

function HomeGuest(props) {
  const [name, setName] = useState()
  const [email, setEmail] = useState()
  const [contact, setContact] = useState()
  const [address, setAddress] = useState()
  const addFlashMessage = useContext(ExampleContext)

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      const response = await Axios.post("student", { name: name, email: email, contact: contact, address: address })
      addFlashMessage("Student has been added!")
      // Swal.fire("Success", "Successfully Added!", "success")
      // Redirect to new post url
      props.history.push(`/view-data/${response.data}`)
    } catch (e) {
      Swal.fire("Oops...", "Something went wrong!", "error")
    }
  }

  return (
    <Page title="Home" wide={true}>
      <div className="row align-items-center">
        <div className="col-lg-7 py-3 py-md-5">
          <h1 className="display-3">Add Student?</h1>
          <p className="lead text-muted">Are you sick of short tweets and impersonal &ldquo;shared&rdquo; posts that are reminiscent of the late 90&rsquo;s email forwards? We believe getting back to actually writing is the key to enjoying the internet again.</p>
        </div>
        <div className="col-lg-5 pl-lg-5 pb-3 py-lg-5">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="username-register" className="text-muted mb-1">
                <small>Username</small>
              </label>
              <input onChange={(e) => setName(e.target.value)} id="username-register" name="name" className="form-control" type="text" placeholder="Pick a username" autoComplete="off" />
            </div>
            <div className="form-group">
              <label htmlFor="email-register" className="text-muted mb-1">
                <small>Email</small>
              </label>
              <input onChange={(e) => setEmail(e.target.value)} id="email-register" name="email" className="form-control" type="text" placeholder="you@example.com" autoComplete="off" />
            </div>
            <div className="form-group">
              <label htmlFor="contact-register" className="text-muted mb-1">
                <small>Contact</small>
              </label>
              <input onChange={(e) => setContact(e.target.value)} id="contact-register" name="contact" className="form-control" type="text" placeholder="Enter Contact" />
            </div>
            <div className="form-group">
              <label htmlFor="address-register" className="text-muted mb-1">
                <small>Address</small>
              </label>
              <input onChange={(e) => setAddress(e.target.value)} id="address-register" name="address" className="form-control" type="text" placeholder="Enter Address" />
            </div>
            <button type="submit" className="py-3 mt-4 btn btn-lg btn-success btn-block">
              Sign up for ComplexApp
            </button>
          </form>
        </div>
      </div>
    </Page>
  )
}

export default withRouter(HomeGuest)
