import React from 'react';
import axios from 'axios';

class App extends React.Component{
  
  constructor(props) {
	super(props);
	this.state = {
  	url: '',
  	index: '',
  	urls: ''
	}
  }

  handleSubmit(e){
    e.preventDefault();
    axios({
      method: "POST", 
      // url:"http://localhost:3002/send", 
      url: " http://127.0.0.1:5000/api/v1/links",
      data:  this.state
    }).then((response)=>{
      if (response.data.status === 'success'){
        alert("Message Sent."); 
        console.log(this.state)
        // this.resetForm()
        this.setState({name: response.data});
      }else if(response.data.status === 'fail'){
        console.log(this.state)
        alert("Message failed to send.")
        this.resetForm()
      }
    })
  }

  resetForm(){
     this.setState({url: '', index: '', urls: ''})
  }
  
  render() {

	  return(
  	  <div className="App">
  	    <form id="contact-form" onSubmit={this.handleSubmit.bind(this)} method="POST">
  	      <div className="form-group">
      	    <label htmlFor="url">Url</label>
        	  <input type="text" className="form-control" id="url" value={this.state.url} onChange={this.onUrlChange.bind(this)} />
  	      </div>
  	      <div className="form-group">
        	  <label htmlFor="index">Index</label>
        	  <input type="index" className="form-control" id="index" value={this.state.index} onChange={this.onIndexChange.bind(this)} />
  	      </div>
  	      <button type="submit" className="btn btn-primary">Submit</button>
  	    </form>
  	  </div>
	  );
  }

  onUrlChange(event) {
	  this.setState({name: event.target.value})
  }

  onIndexChange(event) {
	  this.setState({email: event.target.value})
  }

}

export default App;