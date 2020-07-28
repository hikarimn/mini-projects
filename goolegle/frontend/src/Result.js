import React, { Component } from "react";
import axios from "axios";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

const POST_URL = "http://localhost:5000/api/v1/links";
let config = {
    headers: {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Content-Type': 'application/json'
    }
  }
  
const Result = (props)=> {
    const result = props.location.state.urls;
    console.log("urls: ", result);
    return (

      <div className="result">
          {result}
         {/* {result ? (
            <p>Urls: {result}</p>
            ) : (
            <p></p>
        )} */}
        <br></br><span></span><br></br>
        <Button variant="contained" color="primary" type="tosubmission" href="/post">
          Go back to submission page
        </Button>
        <br></br><span></span><br></br>
        <Button variant="contained" type="tohome" href="/">
          Home
        </Button>
       
      </div>
      
      
    );
  }


export default Result;

