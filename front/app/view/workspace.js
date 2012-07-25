define(function() {

    return Ember.View.extend({
        templateName: 'workspace',

        tabs: [
            {name: 'Character'},
            {name: 'Place'},
            {name: 'Item'},
        ],

        didInsertElement: function() {
            this.$('.workspace').tabs({closable: true});
        },


    });

});
