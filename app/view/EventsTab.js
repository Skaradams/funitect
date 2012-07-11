Ext.define('Funitect.view.EventsTab', {
    extend: 'Ext.panel.Panel',

    requires: [
        'Funitect.view.NewEventWindow',
    ],

    xtype: 'events-tab',
    closable: false,
    layout: 'fit',

    title: 'Events',

    constructor: function() {
        var me = this;
        this.callParent(arguments);

        this.vContainer = new Ext.Panel({
            layout: 'vbox',
            autoScroll: true,
            height: window.innerWidth / 3,
        });

        this.addButton = new Ext.button.Button({
            text: '+1 Event',
            style: {
                marginTop: 30,
                marginLeft: window.innerWidth / 5,
                fontSize: '200%',
            },
            handler: function() {
                var newEventWindow = new Funitect.view.NewEventWindow();
                newEventWindow.show();
            },
        });

        var hContainer = new Ext.container.Container({
            layout: 'hbox',
            items: [
                {xtype: 'container', flex: 1, items: [me.addButton]},
                me.vContainer,
                {xtype: 'container', flex: 1},
            ],
           });
        this.reset();
        this.add(hContainer);
    },

    reset: function() {
        var me = this;
    },

});
