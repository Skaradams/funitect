define(function() {

    var App = function() {};

    App.prototype = {

        loadLibs: function(next) {
            requirejs([
                'ember',
                'markdown',
                'text',
                'jquery-ui'
            ], next);
        },

        loadTemplate: function(baseName, content) {
            $('head').append(
                $('<script></script').attr('type', 'text/x-handlebars')
                                     .attr('data-template-name', baseName)
                                     .append(content)
            );
        },

        loadTemplates: function(next) {
            var that = this;
            var pathes = [];
            var names = [];
            $.each(that.config.templates, function(index, relPath) {
                pathes.push('text!/front/' + relPath + '.hbs');
                names.push(relPath.split('/').pop());
            });
            require(pathes, function() {
                for(var index = 0; index < arguments.length; index++) {
                    that.loadTemplate(names[index], arguments[index]);
                }
                next();
            });
        },

        onTemplatesLoaded: function() {
            var that = this;
            this.loadLibs(function() {
                that.onLibsLoaded();
            });
        },

        onLibsLoaded: function() {
            this.startApp();
        },

        startApp: function() {
            requirejs(this.config.modules, function() {
                var Index = require('app/view/index');
                index = new Index();
                index.appendTo('body');
            });
        },

        load: function() {
            var that = this;
            requirejs.config({
                baseUrl: '/front/lib',
                paths: {
                    app: '../app'
                }
            });
            this.loadTemplates(function(){
                that.onTemplatesLoaded();
            });
        }

    };

    return new App();
});
