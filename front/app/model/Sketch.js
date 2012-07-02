Ext.define('Funitect.model.Sketch', {
    extend: 'Ext.data.Model',

    fields: [
    	'src',
    	'element',
    	'user',
    ],

    proxy: {
        type: 'ajax',
        url: '/api/v1/sketch/',
        writer: {
            type: 'json',
            root: 'objects',
        },
    },

});