const { buildSchema } = require("graphql");
const { graphqlHTTP } = require("express-graphql");
const { studentModel } = require("./models/Student");

// GraphQl Schema
const graphqlSchema = buildSchema(`
    type Student {
        name : String,
        id : Int,
        course : String
    }

    type Query {
        student(id: Int) : Student
        allStudents : [Student]
    }

    type Mutation{
        addStudent(name: String, id: Int,course: String): Student
        updateStudent(name: String, id: Int,course: String): Student
        deleteStudent(id: Int) : Student
    }
`);

// GraphQl Resolvers
const graphqlResolvers = {
  allStudents: async () => {
    let db_response = await studentModel.find({});
    return db_response;
  },
  student: async ({id}) => {
    let db_response = await studentModel.find({id});
    return db_response[0];
  },
  addStudent: async ({ name, id, course }) => {
    const studentObj = { name, id, course };
    const db_response = await studentModel.create(studentObj);
    return db_response;
  },
  updateStudent: async ({ id, name, course }) => {
    let filter = { id };
    let update = { name, course };
    let options = { new: true };
    const db_response = await studentModel.findOneAndUpdate(filter, update, options);
    return db_response;
  },
  deleteStudent: async ({ id }) => {
    const db_response = await studentModel.findOneAndDelete({ id });
    return db_response;
  },
};

// GraphQl MiddleWare for Express Server
const graphqlMiddleWare = graphqlHTTP({
  schema: graphqlSchema,
  rootValue: graphqlResolvers,
  graphiql: true,
});

module.exports = graphqlMiddleWare;
