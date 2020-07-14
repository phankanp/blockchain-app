import React, {useEffect, useState} from 'react';
import {API_BASE_URL} from "../config";
import {Link, useHistory} from "react-router-dom";

import Banner from "./Banner";
import Transaction from "./Transaction";

import wallet_logo from "../assets/wallet-and-coin.png";

function TransactionPool() {
    const [transactions, setTransactions] = useState([]);

    let history = useHistory();

    const fetchTransactions = () => {
        fetch(`${API_BASE_URL}/transactions`)
            .then(response => response.json())
            .then(json => setTransactions(json))
    }

    useEffect(() => {
        fetchTransactions()

        const intervalID = setInterval(fetchTransactions, 20000)

        return () => clearInterval(intervalID)

    }, [])

    const mineBlock = () => {
        fetch(`${API_BASE_URL}/blockchain/mine`)
            .then(response => response.json())
            .then(() => {
                alert('Successfully mined block!')

                history.push('/blockchain')
            })
    }

    return (
        <div className="blockchain">
            <Banner/>
            <br />
            <div className="container">
                <div className="columns is-centered">
                    <div className="column is-two-fifths">
                        <Link className="button is-danger is-fullwidth" to="/">Go Home</Link>
                    </div>
                </div>
                <div className="columns is-centered">
                    <div className="column is-two-fifths">
                        <button
                            className="button is-danger is-fullwidth"
                            onClick={mineBlock}
                        >
                            Mine Block!
                        </button>
                    </div>
                </div>
                <hr/>
                <h3 className="title is-2 has-text-centered">Transaction Pool</h3>
                <div>{transactions.map(transaction =>
                    <div className="columns is-mobile is-centered">
                        <div className="column is-5">
                            <div className="card has-text-centered">
                                <header className="card-header ">
                                    <p className="card-header-title is-centered">
                                        <div className="card-image is-danger">
                                            <figure className="image is-64x64 is-inline-block">
                                                <img className="" src={wallet_logo} alt="wallet logo"/>
                                            </figure>
                                        </div>
                                    </p>
                                </header>
                                <div className="card-content">
                                    <Transaction  key={transaction.id} transaction={transaction}/>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
                </div>
                <hr />

            </div>
        </div>
    )
}

export default TransactionPool;