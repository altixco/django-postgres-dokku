const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  context: __dirname,
  mode: "production",

  entry: {
    app: './assets/js/app',
    vendor: './assets/js/vendor'
  },

  output: {
    path: path.resolve('./assets/webpack_bundles/'),
    filename: '[name].js',
    chunkFilename: '[name].js'
  },

  optimization: {
    // Extract common imports between dependencies and app bundles into a modules.js file
    splitChunks: {
      chunks: 'all',
      name: 'modules',
    },
  },

  plugins: [
    new BundleTracker({
      filename: './webpack-stats.json'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css'
    })
  ],

  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Extract css into its own file
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              // only enable hot reloading in development
              hmr: true,
              // if hmr does not work, this is a forceful method.
              reloadAll: true,
            },
          },
          // Translates CSS into CommonJS to resolve css imports
          'css-loader',
          // Compiles Sass to CSS
          'sass-loader',
        ],
      },
    ],
  },
};
