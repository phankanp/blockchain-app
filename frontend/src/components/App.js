import React, {useEffect, useState} from 'react';
import logo from '../assets/logo2.png'
import {API_BASE_URL} from "../config";

import Blockchain from "./Blockchain";

function App() {
    const [walletInfo, setWalletInfo] = useState({})

    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`)
            .then(response => response.json())
            .then(json => setWalletInfo(json))
    }, [])

    return (
        <div className="App">
            <section className="hero is-link">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <figure className="image is-128x128 is-inline-block">
                            <img className="" src={logo} alt="logo"/>
                        </figure>
                        <h1 className="title is-2 has-text-black">PY Blockchain</h1>
                    </div>
                </div>
            </section>
            <br />
            <Blockchain />
        </div>
    );
}

export default App;
