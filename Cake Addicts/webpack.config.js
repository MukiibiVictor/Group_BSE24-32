const path = require('path');

module.exports = {
    entry: './cakestore/static/cakestore/js/main.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/dist'),
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: ['style-loader', 'css-loader'],
        },
        {
            test: /\.(scss)$/,
            use: [{
                loader: 'style-loader',
            },
            {
                loader: 'css-loader',
            },
            {
                loader: 'sass-loader',
                options: {
                    implementation: require('sass'),
                },
            },
            ],
        },
        ],
    },
};