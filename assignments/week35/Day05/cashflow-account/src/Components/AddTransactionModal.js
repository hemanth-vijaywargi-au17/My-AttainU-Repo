import { useState } from "react";
import Modal from "react-modal";

const customStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
  },
};

Modal.setAppElement("#root");

function AddTransactionModal({ setRows, setBalance }) {
  const [modalIsOpen, setIsOpen] = useState(false);

  function openModal() {
    setIsOpen(true);
  }

  function closeModal() {
    setIsOpen(false);
  }
  console.log()
  const [amount, setAmount] = useState("");
  const [description, setDescription] = useState("");
  const [transaction, setTransaction] = useState("debit");
  const [date, setDate] = useState(new Date().toISOString().slice(0,10)); // Default Date is today's date

  function handleSubmit() {
    setRows((prevState) => {
      let balance = prevState.length === 0 ? 0 : prevState[0].running_balance;
      let newTransactionObj = {
        date: date.split("-").reverse().join("-"),
        description: description,
        credit: transaction !== "debit" ? amount : "-",
        debit: transaction !== "credit" ? amount : "-",
        running_balance:
          transaction === "debit"
            ? balance - Number(amount)
            : balance + Number(amount),
      };
      let newRows = [newTransactionObj, ...prevState];
      localStorage.setItem("rows", JSON.stringify(newRows));
      return newRows;
    });
  }

  return (
    <>
      <button onClick={openModal}>Add Transaction</button>
      <Modal isOpen={modalIsOpen} style={customStyles}>
        <div className="modal-header">
          <h2>Add Transaction</h2>
          <svg
            className="modal-close"
            onClick={closeModal}
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clipRule="evenodd"
            ></path>
          </svg>
        </div>

        <div className="modal-body">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              setAmount("");
              setDescription("");
              setDate("")
              handleSubmit();
              closeModal();
            }}
          >
            <label>Transaction Type</label>
            <select
              onChange={(e) => {
                setTransaction(e.target.value);
              }}
              value={transaction}
            >
              <option value="debit">Debit</option>
              <option value="credit">Credit</option>
            </select>

            <label>Date</label>
            <input
              onChange={(e) => {
                setDate(e.target.value);
              }}
              value={date}
              type="date"
              required
            />

            <label>Amount</label>
            <input
              type="number"
              onChange={(e) => {
                setAmount(e.target.value);
              }}
              value={amount}
              required
            />

            <label>Description</label>
            <input
              type="text"
              onChange={(e) => {
                setDescription(e.target.value);
              }}
              value={description}
              required
            />
            <div className="modal-button-div">
              <button type="submit">Save</button>
            </div>
          </form>
        </div>
      </Modal>
    </>
  );
}

export default AddTransactionModal;
