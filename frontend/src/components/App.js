import React, {useEffect} from 'react';
import {Route, Switch} from "react-router-dom";

import Pusher from 'pusher-js';
import Home from "./Home";
import Blockchain from "./Blockchain";
import CreateTransaction from "./CreateTransaction";
import TransactionPool from "./TransactionPool";
import {API_BASE_URL} from "../config";

function App() {

    useEffect(() => {
        const pusher = new Pusher('946520f9393b1be332a1', {
          cluster: 'us3',
          encrypted: true
        });

        const channel = pusher.subscribe('blockchain');

        channel.bind('transaction-created', data => {
            fetch(`${API_BASE_URL}/transaction/add`,
                {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                })
            .then(response => response.json())
            .then(json => console.log(json))
        })

        channel.bind('block-added', data => {
            fetch(`${API_BASE_URL}/blockchain/replace`,
                {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                })
            .then(response => response.json())
            .then(json => console.log(json))
        })
    });


    return (
        <div className="App">
            <Switch>
                <Route path='/' exact={true} component={Home}/>
                <Route path='/blockchain' component={Blockchain}/>
                <Route path='/create-transaction' component={CreateTransaction}/>
                <Route path='/transaction-pool' component={TransactionPool}/>
            </Switch>
        </div>
    );
}

export default App;
