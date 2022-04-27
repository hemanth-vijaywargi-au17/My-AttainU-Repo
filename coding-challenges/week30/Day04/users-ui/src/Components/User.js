function User(props) {
    return (
        <div className="card m-4">
            <ul className="list-group list-group-flush">
                <li className="list-group-item">
                    <div className="small text-muted">Id</div>
                    <div className="">{props.userData.id}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Name</div>
                    <div className="">{props.userData.name}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Username</div>
                    <div className="">{props.userData.username}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Email</div>
                    <div className="">{props.userData.email}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Address</div>
                    <div className="">{props.userData.address.city}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Phone Number</div>
                    <div className="">{props.userData.phone}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Website</div>
                    <div className="">{props.userData.website}</div>
                </li>
                <li className="list-group-item">
                    <div className="small text-muted">Company Name</div>
                    <div className="">{props.userData.company.name}</div>
                </li>
            </ul>
        </div>
    );
}

export default User