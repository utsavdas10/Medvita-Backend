const mongoose = require('mongoose');

const HttpError = require('../models/http-error');

const Community = require('../models/community-model');
const User = require('../models/users-model');
const Post = require('../models/post-model');




// create new post
const newPost = async (req, res, next) => {
    const {title, content, creator, community} = req.body;
    const date = new Date();
    const upVotes = 0;

    const newPost = new Post({
        title,
        content,
        creator,
        date,
        upVotes,
        community
    });

    let user;
    try {
        user = await User.findById(creator, '-password');
    }
    catch(err){
        const error = new HttpError('Creating post failed, please try again', 500);
        return next(error);
    }

    if(!user){
        const error = new HttpError('Could not find user for provided id', 404);
        return next(error);
    }

    if (creator !== req.userData.userId){
        const error = new HttpError('You are not allowed to create a post for this user', 401);
        return next(error);
    }

    let community_;
    try {
        community_ = await Community.findOne({name: community});
    }
    catch(err){
        const error = new HttpError('Creating post failed, please try again', 500);
        return next(error);
    }

    if(!community_){
        community_ = new Community({
            name: community,
            posts: []
        });
    }

    try {
        const sess = await mongoose.startSession();
        sess.startTransaction();
        await newPost.save({session: sess});
        user.posts.push(newPost);
        await user.save({session: sess});
        community_.posts.push(newPost);
        await community_.save({session: sess});
        await sess.commitTransaction();
    }
    catch(err){
        const error = new HttpError('Creating post failed, please try again', 500);
        return next(error);
    }

    res.status(201).json({message:"New post successful", post: newPost.toObject({getters: true})});
}
    


// get all posts for a community
const getPosts = async (req, res, next) => {
    const community = req.params.community;

    let posts
    if (community === 'General'){
        try {
            //fetch 20 posts
            posts = await Post.find().sort({date: -1}).limit(20);
        }
        catch(err){
            const error = new HttpError('Fetching posts failed, please try again later', 500);
            return next(error);
        }

        if(!posts || posts.length === 0){
            return next(new HttpError('Could not find posts for the provided community', 404));
        }

        res.json({posts: posts.map(post => post.toObject({getters: true}))});
        return;
    }


    try {
        posts = await Community.findOne({name: community}).populate('posts');
    }
    catch(err){
        const error = new HttpError('Fetching posts failed, please try again later', 500);
        return next(error);
    }

    if(!posts || posts.posts.length === 0){
        return next(new HttpError('Could not find posts for the provided community', 404));
    }

    res.json({posts: posts.posts.map(post => post.toObject({getters: true}))});
}



const addUpVotes = async (req, res, next) => {
    const postId = req.params.postId;
    let post;
    try {
        post = await Post.findById(postId)
    }
    catch(err){
        const error = new HttpError('Could not find post', 500);
        return next(error);
    }

    if(!post){
        const error = new HttpError('Could not find post for the provided id', 404);
        return next(error);
    }

    let voted = false;
    if (post.upVoters.includes(req.userData.userId)){
        voted = true;
    }

    if (voted){
        const error = new HttpError('You have already upvoted this post', 401);
        return next(error);
    }

    
    try {
        post.upVotes = post.upVotes + 1;
        post.upVoters.push(req.userData.userId);
        await post.save();
    }
    catch(err){
        const error = new HttpError('Could not upvote post', 500);
        return next(error);
    }

    res.json({message: "Upvoted post", upvotes: post.upVotes});
}



const removeUpVotes = async (req, res, next) => {
    const postId = req.params.postId;
    let post;
    try {
        post = await Post.findById(postId)
    }
    catch(err){
        const error = new HttpError('Could not find post', 500);
        return next(error);
    }

    if(!post){
        const error = new HttpError('Could not find post for the provided id', 404);
        return next(error);
    }

    let voted = false;
    if (post.upVoters.includes(req.userData.userId)){
        voted = true;
    }

    if (!voted){
        const error = new HttpError('You have not upvoted this post', 401);
        return next(error);
    }

    post.upVotes = post.upVotes - 1;
    post.upVoters.pull(req.userData.userId);

    try {
        await post.save();
    }
    catch(err){
        const error = new HttpError('Could not remove upvote from post', 500);
        return next(error);
    }

    res.json({message: "Removed upvote from post", upvotes: post.upVotes});
}





exports.newPost = newPost;
exports.getPosts = getPosts;
exports.addUpVotes = addUpVotes;
exports.removeUpVotes = removeUpVotes;

