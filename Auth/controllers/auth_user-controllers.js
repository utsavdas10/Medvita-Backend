// Environment Variable Configuration
require('dotenv').config();

// Third party imports
const { validationResult } = require('express-validator');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Local imports
const HttpError = require('../models/http-error');
const User = require('../models/users');



//-----------------------Controllers-----------------------//


const signup = async (req, res, next) => {
    // Extracting data from the request
    const {name, email, password} = req.body;

    // Checking if the user already exists
    let existingUser;
    try{
        existingUser = await User.findOne({email: email});
    }
    catch(err){
        const error = new HttpError('Signup failed, please try again later!', 500);
        return next(error);
    }

    if(existingUser){
        const error = new HttpError('User already exists, please login instead!', 422);
        return next(error);
    }

    // Hashing the password
    let hashedPassword;
    try{
        hashedPassword = await bcrypt.hash(password, 12);
    }
    catch(err){
        const error = new HttpError('Could not create user, please try again!', 500);
        return next(error);
    }

    // Creating a new user
    const createdUser = new User({
        name,
        email,
        password: hashedPassword
    });

    // Saving the user to the database
    try{
        await createdUser.save();
    }
    catch(err){
        const error = new HttpError('Signup failed, please try again later!', 500);
        return next(error);
    }

    // Creating a token
    let token;
    try{
        token = jwt.sign(
            {userId: createdUser.id, email: createdUser.email},
            process.env.JWT_KEY,
            {expiresIn: '720h'}
        );
    }
    catch(err){
        const error = new HttpError('Signup failed, please try again later!', 500);
        return next(error);
    }

    // Sending the response
    res.status(201).json({userId: createdUser.id, email: createdUser.email, token: token});
}



const login = async (req, res, next) => {
    // Extracting data from the request
    const {email, password} = req.body;

    // Checking if the user exists
    let existingUser;
    try{
        existingUser = await User.findOne({email: email});
    }
    catch(err){
        const error = new HttpError('Login failed, please try again later!', 500);
        return next(error);
    }

    if(!existingUser){
        const error = new HttpError('Invalid credentials, could not log you in!', 403);
        return next(error);
    }

    // Checking if the password is correct
    let isValidPassword = false;
    try{
        isValidPassword = await bcrypt.compare(password, existingUser.password);
    }
    catch(err){
        const error = new HttpError('Could not log you in, please check your credentials and try again!', 500);
        return next(error);
    }

    if(!isValidPassword){
        const error = new HttpError('Invalid credentials, could not log you in!', 403);
        return next(error);
    }

    // Creating a token
    let token;
    try{
        token = jwt.sign(
            {userId: existingUser.id, email: existingUser.email},
            process.env.JWT_KEY,
            {expiresIn: '720h'}
        );
    }
    catch(err){
        const error = new HttpError('Login failed, please try again later!', 500);
        return next(error);
    }

    // Sending the response
    res.status(200).json({userId: existingUser.id, email: existingUser.email, token: token});
}



// Exporting
exports.signup = signup;
exports.login = login;
