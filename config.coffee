exports.config =
    paths:
        public: 'static'
    files:
        javascripts:
            defaultExtension: 'coffee'
            joinTo:
                'js/app.js': /^app/
                'js/vendor.js': /^vendor/
            order:
                before: [
                    'vendor/jquery.js'
                    'vendor/bootstrap/js/bootstrap.js'
                ]
        stylesheets:
            defaultExtension: 'less'
            joinTo:
                'css/app.css': /^app/
                'css/vendor.css': /^vendor/
    plugins:
        autoReload:
            enabled: true
            port: [1234, 2345, 3456]
            delay: 200 if require('os').platform() is 'win32'
