Ext.define('Funitect.model.ElementComment', {
    extend: 'Ext.data.Model',

    fields: [
        'user',
        'text',
    ],

    proxy: {
        type: 'ajax',
        url: '/api/v1/element-comment/',
        writer: {
            type: 'json',
            root: 'objects',
        },
    },
});
