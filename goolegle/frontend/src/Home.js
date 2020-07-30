import React, { Component } from "react";
import axios from "axios";
import Button from '@material-ui/core/Button';
const POST_URL = "http://localhost:5000/api/v1/links";
let config = {
    headers: {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Content-Type': 'application/json'
    }
  }
class Home extends Component {

  render() {    
    return (
      <div className="submission">
          <Button variant="contained" type="notion" href="/post">
          Woogle
          </Button>
      </div>
      
    );
  }
}

export default Home;