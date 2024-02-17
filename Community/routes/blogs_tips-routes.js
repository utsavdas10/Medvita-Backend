const express = require('express'); 

const blogsTipsController = require('../controllers/blogs_tips-controller');

const router = express.Router();



// -----------------------Routes-----------------------//

// get blogs
router.get('/get-blogs', blogsTipsController.getBlogs);

// get tips
router.get('/get-tips', blogsTipsController.getTips);


// Exporting
module.exports = router;

