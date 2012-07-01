Ext.define('Funitect.store.ElementComments', {
    extend: 'Ext.data.Store',

    requires: [
        'Funitect.model.Comment',
    ],

    constructor: function() {
        this.callParent(arguments);
        this.getProxy().extraParams = {
            element: this.element.data.id,
        }
    },

    model: 'Funitect.model.Comment',


    proxy: {
        type: 'ajax',
        url: '/api/v1/element-comment/',
        reader: {
            type: 'json',
            root: 'objects',
        },
    },

    autoLoad: true,
});