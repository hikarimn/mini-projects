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
    // console.log(data);
    axios
      .post(POST_URL, data, config)
      .then(res => {
        //   console.log(res);
          console.log(res.data);
        //   console.log(this.state);
        // this.setState({
        //     urls: res
        // });
          this.state.urls = res.data;
          console.log('after');

          console.log(this.state.urls);
          console.log('result?');
          console.log(this.state.urls);
          this.props.history.push({
            pathname: '/result',
            state: { urls: this.state.urls }
          });
          this.reset()
        })
  };

  
  render() {    
    return (
      <div className="submission">
        <form noValidate autoComplete="off" onSubmit={this.handleSubmit}>
        
          <TextField id="outlined-basic"  variant="outlined"
            placeholder="URL" value={this.state.url}
            onChange={this.onUrlChange} required
          />
          <br></br><span></span><br></br>
          <TextField id="outlined-basic" variant="outlined"
            placeholder="Limit" value={this.state.index}
            onChange={this.onIndexChange} required
          /><br></br><span></span><br></br>
          <Button variant="contained" color="primary" type="submit">
          Submit
          </Button>
        </form>
        <br></br><span></span><br></br>
        <Button variant="contained" type="tohome" href="/">
          Home
        </Button>
       
      </div>
      
    );
  }
}

export default Post;



// render() {
//     //   console.log(this.state);
//     const resultUrls = this.state.urls;
//     console.log(resultUrls);
//     return (
//       <div className="post">
//         <form className="post" onSubmit={this.handleSubmit}>
//           <input
//             placeholder="Url" value={this.state.url}
//             onChange={this.onUrlChange} required
//           />
//           <textarea
//             placeholder="Index" value={this.state.index}
//             onChange={this.onIndexChange} required
//           />
//           <button type="submit">Create Post</button>
//         </form>
//         <p>
//             {this.state.url}
//         </p>
//         <p>
//             {this.state.index}
//         </p>
//         <p>Urls: {resultUrls}</p>
//         {resultUrls.length > 0 ? (
//             <p>Urls: {resultUrls}</p>
//             ) : (
//             <p></p>
//         )}
       
//       </div>
      
//     );
//   }