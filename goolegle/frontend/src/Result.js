import React from "react";
import Button from '@material-ui/core/Button';

class Result extends React.Component {
    constructor(props) {
        super(props);
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
            return <li key={index}>{url}</li>;
        });
        
        const pageNumbers = [];
        for (let i = 1; i <= Math.ceil(urls.length / listsPerPage); i++) {
            pageNumbers.push(i);
        }

        const renderPageNumbers = pageNumbers.map(number => {
            return (
                <li
                key={number}
                id={number}
                onClick={this.handleClick}
                > 
                {number}
              </li> 
           );
        });
            

        if(list_size == 0){
            return (
                <div className="result">  
                    <p>
                        Input: {original_url}
                    </p>
                    <p>
                        The submitted input was not valid url.
                    </p>                 
                    <p>
                    <Button variant="contained" color="primary" type="tosubmission" href="/post">
                        Go back to submission page
                    </Button>
                  </p>
                    <p>
                    <Button variant="contained" type="tohome" href="/">
                        Home
                    </Button>
                    </p>
                </div>    
            );
        } else {
            return (
                <div className = "result">
                    <p>
                        Input: {original_url}
                    </p>
                    <ul>
                        {renderUrls}
                    </ul>
                    <ul id="page-numbers">
                        {renderPageNumbers}
                    </ul>
                    <p>
                        <Button variant="contained" color="primary" type="tosubmission" href="/post">
                        Go back to submission page
                        </Button>
                    </p>
                    <p>
                        <Button variant="contained" type="tohome" href="/">
                        Home
                        </Button>
                    </p>
                </div>
              );
        }
    }
}

export default Result;