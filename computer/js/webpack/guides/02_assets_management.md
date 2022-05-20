# Webpack Guides

## Chapter 02: Asset Management

- History
  - Prior to webpack, front-end developers would use tools like grunt and gulp to process these assets and
    move them from their /src folder into their /dist or /build directory.

- Dynamically bundle
  - Tools like webpack will dynamically bundle all dependencies (creating what's known as a dependency graph).
  - This is great because every module now explicitly states its dependencies and we'll avoid bundling modules that aren't in use.

- Supports any type of file
  - One of the coolest webpack features is that you can also include any other type of file, besides JavaScript,
    for which there is a loader or built-in Asset Modules support.
  - This means that the same benefits listed above for JavaScript (e.g. explicit dependencies)
    can be applied to everything used in building a website or web app.

### Loading CSS

- In order to import a CSS file from within a JavaScript module,
  you need to install and add the style-loader and css-loader to your module configuration:

  ```sh
  npm install --save-dev style-loader css-loader
  ```
