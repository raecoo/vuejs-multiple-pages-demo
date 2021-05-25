# vm

> A multiple pages Vue.js project skeleton by history mode

## Structure

```bash
├── README.md
├── build
│   ├── build.js
│   ├── check-versions.js
│   ├── logo.png
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   └── webpack.prod.conf.js
├── config
│   ├── dev.env.js
│   ├── index.js
│   ├── prod.env.js
│   └── test.env.js
├── deploy.sh
├── env.config
├── package-lock.json
├── package.json
├── requirements.txt
├── run.py
├── server
│   ├── api
│   ├── config.py
│   ├── entrance.py
│   └── website
├── serverless.yml
├── src
│   ├── components
│   ├── modules
│   └── pages
├── static
└── test
    ├── e2e
    └── unit
```

## Build Setup

```bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

## Deploy

```bash
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-wsgi
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
