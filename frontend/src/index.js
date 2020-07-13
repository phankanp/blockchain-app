import React from 'react';
import ReactDOM from 'react-dom';
import {Route, BrowserRouter, Switch} from "react-router-dom";
import {createBrowserHistory} from "history";
import './index.css';
import App from './components/App';

import 'react-bulma-components/dist/react-bulma-components.min.css';

ReactDOM.render(
    <BrowserRouter history={createBrowserHistory()}>
        <App />
    </BrowserRouter>,
    document.getElementById('root')
);

