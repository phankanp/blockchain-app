import React from "react";


function Pagination({blocksPerPage, totalBlocks, paginate, currentPage}) {
    const pageNumbers = []

    for (let i = 1; i <= Math.ceil(totalBlocks / blocksPerPage); i++) {
        pageNumbers.push(i)
    }

    return (
        <nav className="pagination is-centered" role="navigation" aria-label="pagination">
            <ul className="pagination-list">
                {pageNumbers.map(pageNumber => (
                    <li key={pageNumber}>
                        <a
                            className={(currentPage === pageNumber ? 'pagination-link is-current' : 'pagination-link ')}
                            onClick={() => paginate(pageNumber)}>{pageNumber}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    )
}

export default Pagination