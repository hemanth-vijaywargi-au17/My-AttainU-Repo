require("dotenv").config();
require("./db.js").dbConnect();

const CustomerModel = require("./models/Customer.js");
const CarModel = require("./models/Car.js");

async function addUser(userName) {
  return await CustomerModel.create({
    name: userName,
    cars: [],
  });
}

async function addCar(car_model, car_price, owner_id) {
  let car = await CarModel.create({
    model: car_model,
    price: car_price,
    customer_id: owner_id,
  });
  await CustomerModel.updateOne(
    { _id: owner_id },
    { $push: { cars: car._id } }
  );
}

async function main() {
  // Creating Customer 1
  let customer1 = await addUser("Jack");

  // Adding Cars for Customer 1
  await addCar("Audi A4", 5000000, customer1._id);
  await addCar("Tesla Model S", 5000000, customer1._id);
  await addCar("Bugatti Veyron", 5000000, customer1._id);

  // Creating Customer 2
  let customer2 = await addUser("Dorsey");

  // Adding Cars for Customer 2
  await addCar("Lexus LFA", 5000000, customer2._id);
  await addCar("Ford GT40", 5000000, customer2._id);
  await addCar("Eagle Speedster", 5000000, customer2._id);
  await addCar("Koenigsegg CCXR", 5000000, customer2._id);

  // Query 1 - Get a list of all the cars of customer 2 (should display 4 cars)
  customer2 = await CustomerModel.findById(customer2._id).populate("cars");
  console.log("Customer 2 Cars : \n", customer2.cars);

  // Query 2 - Get a list of all the customers along with their cars in the cars property of Customer model.
  let customers = await CustomerModel.find().populate("cars");
  console.log("All Customers Info :\n", customers);

  process.exit();
}

main();
