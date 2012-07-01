Ext.define('Funitect.store.Sketches', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.Sketch',
    ],

    constructor: function() {
        this.callParent(arguments);
        this.getProxy().extraParams = {
            element: this.element.data.id,
        }
    },

    model: 'Funitect.model.Sketch',


    proxy: {
        type: 'ajax',
        url: '/api/v1/sketch/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

    autoLoad: true,
});