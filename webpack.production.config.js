const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

var config = require('./webpack.base.config');

config.mode = 'production';

config.output.path = path.resolve('./main/static/dist/');

config.plugins.push(
  new BundleTracker({
    filename: './webpack-production-stats.json'
  }),
);

module.exports = config;
