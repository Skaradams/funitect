Ext.define('Funitect.store.EventKinds', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.EventKind',
    ],

    constructor: function() {
        this.getProxy().extraParams = {
            game: Funitect.currentGame.data.id,
        }
        this.callParent(arguments);
    },

    model: 'Funitect.model.EventKind',

    proxy: {
        type: 'ajax',
        url: '/api/v1/event-kind/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

});
