import React, { Component } from "react";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

import axios from "axios";
const POST_URL = "http://localhost:5000/api/v1/links";
let config = {
    headers: {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Content-Type': 'application/json'
    }
  }

const initialState = {
  url: "",
  index: "",
  urls: ""
};


class Post extends Component {

  state = {
    url: "",
    index: "",
    urls: ""
  };

  onUrlChange = e => {
    this.setState({
      url: e.target.value
    });
  };

  onIndexChange = e => {
    this.setState({
      index: e.target.value
    });
  };

  reset() {
    this.setState(initialState);
  }

  handleSubmit = e => {
    e.preventDefault();
    const data = {
      url: this.state.url,
      index: this.state.index
    };
    axios
      .post(POST_URL, data, config)
      .then(res => {
          this.state.urls = res.data;
          this.props.history.push({
            pathname: '/result',
            state: { result: this.state.urls }
          });
          this.reset()
        })
  };

  render() {    
    return (
      <div className="submission">
        <p>
          It may take a few seconds to display the result. 
        </p>
        <form noValidate autoComplete="off" onSubmit={this.handleSubmit}>
          <p>
          <TextField id="outlined-basic"  variant="outlined"
            placeholder="URL" value={this.state.url}
            onChange={this.onUrlChange} required
          />
          </p>
          <p>
          <TextField id="outlined-basic" variant="outlined"
            placeholder="Limit" value={this.state.index}
            onChange={this.onIndexChange} required
          />
          </p>
          <p>
          <Button variant="contained" color="primary" type="submit">
          Submit
          </Button>
          </p>
        </form>
        <p>
          <Button variant="contained" type="tohome" href="/">
          Home
          </Button>
        </p>
      </div>
      
    );
  }
}

export default Post;

