Ext.define('Funitect.controller.Launcher', {
    extend: 'Ext.app.Controller',

    requires: [
        'Funitect.store.Games',
        'Funitect.view.Workspace',
    ],

    init: function() {
        var me = this;
        var games = new Funitect.store.Games({listeners: {
            load: function() {
                Funitect.currentGame = games.first();
                var workspace = new Funitect.view.Workspace();
                workspace.show();
            }
        }});
    },


});
