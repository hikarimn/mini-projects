import React from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Post from './Post'
import Home from './Home'
import Result from './Result'

function App() {
    return (
        <main>
            <BrowserRouter>

            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/post" component={Post} />
                <Route path="/result" component={Result} />
            </Switch>
            </BrowserRouter>

        </main>
    )
}

export default App;