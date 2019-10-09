const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

const config = require('./webpack.base.config');

config.mode = 'development';

config.plugins.push(
  new BundleTracker({
    filename: './webpack-development-stats.json'
  }),
);

config.devServer = {
  port: 9000,
  headers: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
    "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
  },
};

config.output.path = path.resolve('./assets/webpack_bundles/');
//override django's STATIC_URL for webpack bundles
config.output.publicPath = 'http://localhost:9000/static/';

module.exports = config;
