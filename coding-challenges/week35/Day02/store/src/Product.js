import React from "react";
import PropTypes from "prop-types";

function Product(props) {
  return (
    <div
      style={{
        width: "200px",
        border: "1px solid black",
        padding: "10px",
        margin: "10px",
        textAlign: "center",
        display: "inline-block",
      }}
    >
      <img style={{ width: "100%" }} src={props.image} alt="product" />
      <p>{props.title}</p>
      <p>$ {props.price}</p>
      <p>{props.rating.rate}</p>
      <p>{props.category}</p>
    </div>
  );
}

Product.propTypes = {
  id: PropTypes.number.isRequired,
  title: PropTypes.string,
  price: PropTypes.number,
  description: PropTypes.string,
  category: PropTypes.string,
  image: PropTypes.string,
  rating: PropTypes.object,
};

export default Product;
