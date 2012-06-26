Ext.define('Funitect.view.GamesWindow', {
    extend: 'Ext.window.Window',

    layout: 'vbox',

    title: 'Choose one of your games',

    resizeable: false,
    closable: false,

    width: 200,

    addGame: function(game) {
        var gameButtonId = 'game-button-' + game.data.id;
        this.add({
            xtype: 'button',
            id: gameButtonId,
            config: {
                game: game,
            },
            text: game.data.name,
            style: {
                marginLeft: 20,
                marginTop: 10,
                marginBottom: 10
            }, width: 150}
        );
        return gameButtonId;
    },

});