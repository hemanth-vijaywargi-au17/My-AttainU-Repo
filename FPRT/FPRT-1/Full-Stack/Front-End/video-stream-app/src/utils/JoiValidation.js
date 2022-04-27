const Joi = require("joi");

const loginSchema = Joi.object({
  email: Joi.string()
    .email({ minDomainSegments: 2, tlds: {} })
    .required()
    .min(4)
    .lowercase()
    .label("E-Mail"),
  pass: Joi.string().required().label("Password"),
});

const signupSchema = Joi.object({
  username: Joi.string().alphanum().min(6).max(30).required().label("Username"),
  email: Joi.string()
    .email({ minDomainSegments: 2, tlds: {} })
    .required()
    .min(4)
    .lowercase()
    .label("E-Mail"),
  pass: Joi.string().required().min(6).max(16).label("Password"),
  repeat_password: Joi.any()
    .label("Confirm password")
    .equal(Joi.ref("pass"))
    .required()
    .options({ messages: { "any.only": "{{#label}} does not match" } }),
});

module.exports = { loginSchema, signupSchema };
