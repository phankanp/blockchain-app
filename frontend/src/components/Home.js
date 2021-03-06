import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import {API_BASE_URL} from "../config";

import logo from "../assets/buy-sell-coin.png";

function Home() {
    const [walletInfo, setWalletInfo] = useState({})

    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`)
            .then(response => response.json())
            .then(json => setWalletInfo(json))
    }, [])

    const { wallet_address, balance } = walletInfo;

    return (
        <div className="Home">
            <section className="hero is-link is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <figure className="image is-128x128 is-inline-block">
                            <img className="" src={logo} alt="logo"/>
                        </figure>
                        <h1 className="title is-2 has-text-white">PY Blockchain</h1>
                        <div className="columns">
                            <div className="column">
                                <div>Wallet: {wallet_address}</div>
                            </div>
                        </div>
                        <div className="columns">
                            <div className="column">
                                <div>Balance: {balance}</div>
                            </div>
                        </div>
                        <div className="columns">
                            <div className="column">
                                <Link className="button is-danger" to="/blockchain">View Blockchain</Link>
                            </div>
                        </div>
                        <div className="columns">
                            <div className="column">
                                <Link className="button is-danger" to="/create-transaction">Create Transaction</Link>
                            </div>
                        </div>
                        <div className="columns">
                            <div className="column">
                                <Link className="button is-danger" to="/transaction-pool">Transaction Pool</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Home