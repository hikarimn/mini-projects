import React from "react";
import Button from '@material-ui/core/Button';

class Result extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
        this.state = {
            original_url: props.location.state.result.original_url,
            list_size: props.location.state.result.list_size,
            urls: props.location.state.result.urls,
            currentPage: 1,
            listsPerPage: 20
        };
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(event) {
        this.setState({
          currentPage: Number(event.target.id)
        });
    }

    render(){
        const {original_url, list_size, urls, currentPage, listsPerPage} = this.state;
        const indexOfLastUrl = currentPage * listsPerPage;
        const indexOfFirstUrl = indexOfLastUrl - listsPerPage;
        const currentUrls = urls.slice(indexOfFirstUrl, indexOfLastUrl)

        const renderUrls = currentUrls.map((url, index) => {
        return <li key={index}>{url.title} - <a href = {url.url}>{url.url}</a></li>;
        });
        
        const pageNumbers = [];
        for (let i = 1; i <= Math.ceil(urls.length / listsPerPage); i++) {
            pageNumbers.push(i);
        }

        const renderPageNumbers = pageNumbers.map(number => {
            return (
                <li  className="lists"
                key={number}
                id={number}
                onClick={this.handleClick}
                > 
                {number}
              </li> 
           );
        });

        const renderButtons = 
        <p>
        <Button variant="contained" color="primary" type="tosubmission" href="/post">
            Go back to submission page
        </Button>
        <br></br><br></br>        
        <Button variant="contained" type="tohome" href="/">
            Home
        </Button>
        </p>
        
            
        if(list_size == 0){
            return (
                <div className="result">  
                    <p>
                    Submitted URL: <a href = {original_url}>{original_url}</a>
                    </p>
                    <p>
                    The submitted input was not valid.
                    </p>         
                    {renderButtons}        
                </div>    
            );
        } else {
            return (
                <div className = "result">
                    <p>
                    Submitted URL: <a href = {original_url}>{original_url}</a>
                    </p>      
                    <ul id="url-list">
                        {renderUrls}
                    </ul>
                    <ul id="page-numbers">
                        {renderPageNumbers}
                    </ul>
                    {renderButtons}  
                </div>
              );
        }
    }
}

export default Result;