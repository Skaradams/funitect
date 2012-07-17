define(function() {

    return Ember.View.extend({

        classNames: ['viewport'],

        init: function() {
            var Header = require('app/view/header');
            var Workspace = require('app/view/workspace');
            this.header = new Header();
            this.workspace = new Workspace();
        },

        didInsertElement: function() {
            this.header.appendTo(this.$());
            this.workspace.appendTo(this.$());
        },

    });

});
