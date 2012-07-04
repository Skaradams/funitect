Ext.define('Funitect.model.Element', {
    extend: 'Ext.data.Model',

    fields: [
        'name',
    ],

    proxy: {
        type: 'ajax',
        url: '/api/v1/element/',
        writer: {
            type: 'json',
            root: 'objects',
        },
    },

});
