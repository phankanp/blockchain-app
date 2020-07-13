import React, {useEffect, useState} from "react";
import {API_BASE_URL} from "../config";
import Block from "./Block";
import Pagination from "./Pagination";

import coin from '../assets/coin.png'
import {Link} from "react-router-dom";
import Banner from "./Banner";


function Blockchain() {
    const [blockchain, setBlockchain] = useState([])
    const [currentPage, setCurrentPage] = useState(1)
    const [blocksPerPage, setBlocksPerPage] = useState(4)

    useEffect(() => {
        fetch(`${API_BASE_URL}/blockchain`)
            .then(response => response.json())
            .then(json => setBlockchain(json))
    }, [])

    const indexOfLastBlock = currentPage * blocksPerPage
    const indexOfFirstBlock = indexOfLastBlock - blocksPerPage
    const currentBlocks = blockchain.slice(indexOfFirstBlock, indexOfLastBlock)

    const paginate = (pageNumber) => {
        setCurrentPage(pageNumber)
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
                <hr/>
                <div>{currentBlocks.map(block =>
                    <div className="columns is-mobile is-centered">
                        <div className="column is-5">
                            <div className="card has-text-centered">
                                <header className="card-header ">
                                    <p className="card-header-title is-centered">
                                        <div className="card-image is-danger">
                                            <figure className="image is-64x64 is-inline-block">
                                                <img className="" src={coin} alt="coin"/>
                                            </figure>
                                        </div>
                                    </p>
                                </header>
                                <div className="card-content">
                                    <Block key={block.hash} block={block}/>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
                </div>
                <br/>
                <Pagination blocksPerPage={blocksPerPage} totalBlocks={blockchain.length} paginate={paginate}
                            currentPage={currentPage}/>
            </div>
        </div>
    )
}

export default Blockchain