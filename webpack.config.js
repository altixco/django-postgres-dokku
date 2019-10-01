const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  context: __dirname,
  mode: "production",
  devtool: "source-map",

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
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Extract css into its own file
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              sourceMap: true
            }
          },
          // Translates CSS into CommonJS to resolve css imports
          {
            loader: 'css-loader',
            options: {
              sourceMap: true
            }
          },
          // Make modern CSS work with old browsers
          {
            loader: 'postcss-loader',
            options: {
              sourceMap: true
            }
          },
          // Compiles Sass to CSS
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true
            }
          }
        ],
      },
    ],
  },
}
