import React, {useEffect, useState} from 'react';
import {Route, Switch} from "react-router-dom";
import {API_BASE_URL} from "../config";

import Blockchain from "./Blockchain";
import CreateTransaction from "./CreateTransaction";
import Home from "./Home";
import logo from '../assets/buy-sell-coin.png'

function App() {


    return (
        <div className="App">
            <Switch>
                <Route path='/' exact={true} component={Home} />
                <Route path='/blockchain' component={Blockchain}/>
                <Route path='/create-transaction' component={CreateTransaction}/>
            </Switch>
        </div>
    );
}

export default App;
