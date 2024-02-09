const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator');

const userSchema = new mongoose.Schema({
    name: {type: String, required: true},
    email: {type: String, required: true, unique:true},
    password: {type: String, required: true, minlength: 6},
    profile_pic: {data: Buffer, contentType: String},
    phone: {type: String},
    address: {type: String}
});

userSchema.plugin(uniqueValidator);

module.exports = mongoose.model('User', userSchema);