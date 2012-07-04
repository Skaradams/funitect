Ext.define('Funitect.store.ElementKinds', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.ElementKind',
    ],

    constructor: function() {
        this.getProxy().extraParams = {
            game: Funitect.currentGame.data.id,
        }
        this.callParent(arguments);
    },

    model: 'Funitect.model.ElementKind',


    proxy: {
        type: 'ajax',
        url: '/api/v1/element-kind/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

    autoLoad: true,
});