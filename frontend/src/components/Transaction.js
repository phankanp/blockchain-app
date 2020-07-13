import React from "react";


function Transaction({transaction}) {
    const { input, outputs } = transaction

    let {recipient_address, recipient_amount, sender_address, sender_amount}  = outputs

    if (sender_address !== 'Mining-Reward-Transaction') {
        sender_address = sender_address.substring(57,67)
    }

    return (
        <div className="Transaction">
            <div>Recipient: {recipient_address.substring(57,67)}...</div>
            <div>Received: {recipient_amount}</div>
            <div>Sender: {sender_address}...</div>
            <div>Sent: {sender_amount}</div>
        </div>
    )
}

export default Transaction