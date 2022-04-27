import React from 'react'

function TableRow({date,description,credit,debit,running_balance}) {
    return (
        <tr>
            <td>{date}</td>
            <td>{description}</td>
            <td>{credit}</td>
            <td>{debit}</td>
            <td>{running_balance}</td>
        </tr>
    )
}

export default TableRow
