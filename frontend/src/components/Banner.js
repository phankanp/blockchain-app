import React from "react";
import logo from "../assets/buy-sell-coin.png";

function Banner() {
    return (
        <section className="hero is-link">
            <div className="hero-body">
                <div className="container has-text-centered">
                    <figure className="image is-128x128 is-inline-block">
                        <img className="" src={logo} alt="logo"/>
                    </figure>
                </div>
            </div>
        </section>
    )
}

export default Banner