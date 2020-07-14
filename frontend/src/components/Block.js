import React, {useState} from "react";

import Transaction from "./Transaction";

function ToggleTransactions({block}) {
    const [showTransactions, setShowTransactions] = useState(false)
    const {data} = block

    const setToggleVal = () => {
        setShowTransactions(!showTransactions)
    }

    if (showTransactions) {
        return (
            <div className="">
                {
                    data.map(transaction => (
                        <div key={transaction.id}>
                            <Transaction transaction={transaction}/>
                            <hr/>
                        </div>
                    ))
                }
                <br/>
                <div className="buttons">
                    <button className="button is-fullwidth is-info block-button" onClick={setToggleVal}>
                        Hide Transactions
                    </button>
                </div>
            </div>

        )
    }

    return (
        <div className="buttons">
            <button className="button is-fullwidth is-info block-button" onClick={setToggleVal}>Show Transactions
            </button>
        </div>
    )
}

function Block({block}) {
    const {timestamp, hash, data} = block

    const hashSub = `${hash.substring(0, 15)}...`
    const timeStamp = new Date(timestamp / 1000000).toLocaleString()

    return (
        <div className="block">
            <div>Hash: {hashSub}</div>
            <div>Timestamp = {timeStamp}</div>
            <hr/>
            <ToggleTransactions block={block}/>
        </div>
    )
}

export default Block