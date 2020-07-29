import React from 'react';
import { Link } from 'react-router-dom';

class GenericNotFound extends React.Component{
    render(){
        return <div>
            <p style={{textAlign:"center"}}>
              <Link to="/">Go to Home </Link>
            </p>
          </div>;
    }
}
export default GenericNotFound;