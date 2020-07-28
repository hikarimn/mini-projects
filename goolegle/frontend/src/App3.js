import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

export default class App extends Component {

    // constructor(props, context) {
    //     super(props, context);

    //     this.state = {
    //         url: '',
    //         index: '',
    //         urls: ''
    //     }
    // }
    constructor(props) {
        super(props);
        this.state = {
          url: '',
          index: '',
          urls: ''
        }
      }

    onChange(e) {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    onSubmit(e) {
        // e.preventDefault();

        // fetch(this.props.formAction, {
        //     headers: {
        //         'Accept': 'application/json',
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({description: this.state.description})
        // });

        // this.setState({description: ''});
        // console.log(this.state)
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
            }   else if(response.data.status === 'fail'){
                // console.log(this.state)
                alert("Message failed to send.")
                this.resetForm()
            }
        })
    }
    resetForm(){
        this.setState({url: '', index: '', urls: ''})
     }

    render() {
        console.log(this.state);
        return (
            <div className="App">
                <form
                    id="url-submission"
                    action={this.props.action}
                    method={this.props.method}
                    onSubmit={this.onSubmit}>
                    <h2>URL Submission</h2>
                    <label>
                        <span class="text">URL:</span>
                        <input type="url" name="url"/><br/>
                    </label>
                    <br/>
                    <label>
                        <span class="text">Limit:</span>
                        <input type="limit" name="limit"/><br/>
                    </label>
                    <br/>
                    <div class="align-right">
                        <button>Submit</button>
                    </div>
                </form>
            </div>
        );
    }

}

// App.propTypes = { action: React.PropTypes.string.isRequired, method: React.PropTypes.string}
App.defaultProps = {
    action: 'http://don.healthedata.com/admin/login',
    method: 'post'
};

// module.exports = App;
// export default App;