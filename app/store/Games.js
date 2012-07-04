Ext.define('Funitect.store.Games', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.Game',
    ],

    model: 'Funitect.model.Game',

    proxy: {
        type: 'ajax',
        url: '/api/v1/game/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

    autoLoad: true,
});