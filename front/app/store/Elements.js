Ext.define('Funitect.store.Elements', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.Element',
    ],

    constructor: function() {
        this.callParent(arguments);
        this.getProxy().extraParams = {
            kind: this.elementKind.data.id,
        }
    },

    model: 'Funitect.model.Element',

    proxy: {
        type: 'ajax',
        url: '/api/v1/element/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

    autoLoad: true,
});