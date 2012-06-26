Ext.define('Funitect.controller.Launcher', {
    extend: 'Ext.app.Controller',

    requires: [
        'Funitect.store.Games',
        'Funitect.view.GamesWindow',
        'Funitect.view.Workspace',
    ],

    init: function() {
        var me = this;
        this.gamesWindow = new Funitect.view.GamesWindow();
        var games = new Funitect.store.Games({listeners: {
            load: function() {
                
                games.each(function(game) {
                    var selector = '#' + me.gamesWindow.addGame(game);
                    listeners = {};
                    listeners[selector] = {click: me.onChooseGame};
                    me.control(listeners);
                })
                
                me.gamesWindow.show();
            }
        }});
    },

    onChooseGame: function(el) {
        this.gamesWindow.hide();
        Funitect.currentGame = el.config.game;
        var workspace = new Funitect.view.Workspace();
        workspace.show();
    },

});