var webpack = require('webpack');
var common = require('./webpack.common.config.js');
var assign = require('object-assign');

module.exports = assign(common, {
    debug: true,
    plugins: common.plugins.concat([
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.optimize.AggressiveMergingPlugin(),
        new webpack.optimize.UglifyJsPlugin({exclude: /conference.*?\.js$/})
    ])
});
