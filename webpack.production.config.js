const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

const config = require('./webpack.base.config');

config.mode = 'production';

config.plugins.push(
  new BundleTracker({
    filename: './webpack-production-stats.json'
  }),
);

config.output.path = path.resolve('./main/static/dist/');

module.exports = config;
