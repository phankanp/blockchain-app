import React, {useState} from "react";

import {API_BASE_URL} from "../config";
import Banner from "./Banner";
import {Link} from "react-router-dom";

function CreateTransaction() {
    const [amount, setAmount] = useState(0)
    const [recipient, setRecipient] = useState('')

    const updateRecipient = (event) => {
        setRecipient(event.target.value)
    }

    const updateAmount = (event) => {
        setAmount(Number(event.target.value))
    }

    const submitTransaction = () => {
        fetch(`${API_BASE_URL}/transaction/new`,
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({recipient, amount})
            }).then(response => response.json())
            .then(json => {
                alert('Success!')
            })
    }

    return (
        <div className="create-transaction">
            <Banner/>
            <br/>
            <div className="container">
                <div className="columns is-centered">
                    <div className="column is-two-fifths">
                        <Link className="button is-danger is-fullwidth" to="/">Go Home</Link>
                    </div>
                </div>
                <hr/>
                <h3 className="title is-2 has-text-centered">Create a Transaction</h3>
                <div className="columns is-centered">
                    <div className="column column is-two-fifths">
                <div className="field">
                    <label className="label">Recipient</label>
                    <div className="control">
                        <input
                            className="input"
                            type="text"
                            placeholder="recipient"
                            value={recipient}
                            onChange={updateRecipient}
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Amount</label>
                    <div className="control">
                        <input
                            className="input"
                            type="number"
                            placeholder="amount"
                            value={amount}
                            onChange={updateAmount}
                        />
                    </div>
                </div>
                <div className="control">
                    <button className="button is-link is-fullwidth" onClick={submitTransaction}>Submit</button>
                </div>
                    </div>
                    </div>
            </div>
        </div>
    )
}


export default CreateTransaction