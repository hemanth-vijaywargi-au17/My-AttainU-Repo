import { Component } from 'react'
import './productStyles.css'

class Product extends Component {
    render() {
        return (
            <div className="product">
                <div className="header-parent"><div className="header">{this.props.productsInfo.header}</div></div>
                <h2>{this.props.productsInfo.productName}<span>{this.props.productsInfo.productNameTM}</span></h2>
                <p>{this.props.productsInfo.description}</p>
                <button>Learn more</button>
            </div>
        );
    }
}

export default Product