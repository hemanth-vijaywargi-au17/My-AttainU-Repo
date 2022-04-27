import React, { useState } from "react";
import AddTransactionModal from "./AddTransactionModal";
import TableRow from "./TableRow";
import { v4 as uuidv4 } from 'uuid';

function Table() {
  const [rows, setRows] = useState(
    JSON.parse(localStorage.getItem("rows")) || []
  );

  return (
    <>
      <h1>Transactions</h1>
      <AddTransactionModal setRows={setRows} />
      <table>
        <thead>
          <tr>
            <td>Date (dd-mm-yyyy)</td>
            <td>Description</td>
            <td>Credit</td>
            <td>Debit</td>
            <td>Running Balance</td>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => {
            return <TableRow {...row} key={uuidv4()}/>;
          })}
        </tbody>
      </table>
    </>
  );
}

export default Table;
