Ext.define('Funitect.view.Workspace', {
    extend: 'Ext.tab.Panel',


    requires: [
        'Funitect.view.Dashboard',
        'Funitect.view.ElementsTab',
        'Funitect.view.EventsTab',
        'Funitect.store.ElementKinds',
    ],

    id: 'workspace',

    renderTo: document.body,

    width: window.innerWidth,
    height: window.innerHeight,


    layout: 'fit',

    items: [
        //{xtype: 'dashboard'},
    ],

    show: function() {
        this.callParent();
        var me  = this;
        var elementKinds = new Funitect.store.ElementKinds({listeners: {
            load: function() {
                elementKinds.each(function(elementKind) {
                    me.add({xtype: 'elements-tab', elementKind: elementKind, workspace: me});
                });
                me.add({xtype: 'events-tab'});
                me.items.first().show();
            }
        }});
    },

});
