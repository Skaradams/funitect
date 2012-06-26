Ext.define('Funitect.view.ElementsTab', {
    extend: 'Ext.tab.Tab',
    
    xtype: 'elements-tab',

    closable: false,

    constructor: function() {
        this.callParent(arguments);
        this.title = this.elementKind.data.name;
    },

});