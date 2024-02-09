// Third party imports
const express = require('express');
const {check} = require('express-validator');

// Local imports
const authUserController = require('../controllers/auth_user-controllers');

// Initializing
const router = express.Router();


//-----------------------Routes-----------------------//


// @route   POST auth/signup
router.post(
    '/signup', 
    [
        check('name').not().isEmpty(),
        check('email').normalizeEmail().isEmail(),
        check('password').isLength({min: 6})
    ],
    authUserController.signup
);


// @route   POST auth/login
router.post(
    '/login',
    [
        check('email').normalizeEmail().isEmail(),
        check('password').isLength({min: 6})
    ],
    authUserController.login
);



// Exporting
module.exports = router;