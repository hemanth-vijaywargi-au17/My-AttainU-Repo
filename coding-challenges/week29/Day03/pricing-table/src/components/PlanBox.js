import './styles.css'

function PlanBox(props) {
    return (
        <div className="price-box">
            <div className="plan-name slanted">
                <div className="slanted-content">
                    {props.planInfo.planName.toUpperCase()}
                </div>
            </div>
            <div className="plan-price">
                <span className="size3">$</span>
                <span className="size1">{props.planInfo.price}</span>
                <span className="size2">.99</span>
                /MON
            </div>
            <div className="features">{props.planInfo.bandWidth} Bandwidth</div>
            <div className="features">{props.planInfo.storage} Storage</div>
            <div className="features">{props.planInfo.accounts} Accounts</div>
            <div className="features">{props.planInfo.domains} Host Domain</div>
            <div className="features">24/7 Support</div>
            <input type="submit" value="SIGN UP" />
        </div>
    );
}

export default PlanBox