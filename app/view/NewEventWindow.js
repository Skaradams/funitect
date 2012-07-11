
Ext.define('Funitect.view.NewEventWindow', {
    extend: 'Ext.window.Window',

    requires: [
        'Funitect.store.EventKinds',
    ],

    layout: 'fit',

    title: 'Create new',

    resizeable: false,
    closable: true,

    width: window.innerWidth - 100,

    constructor: function() {
        var me = this;
        var eventKinds = new Funitect.store.EventKinds({game: Funitect.currentGame});

        eventKinds.load();
        this.eventTypeField = new Ext.form.field.ComboBox({
            store: eventKinds,
            displayField: 'readableSentence',
            editable: false,
            width: me.width - 20,
            flex: 1,
            listeners:{
                 select: function(){me.onChangeEventType()},
            },
        });
        this.callParent(arguments);
        this.sandboxPanel = new Ext.Panel({
            width: me.width - 20,
            height: 300,
            flex: 2,
            layout: 'hbox',
        })
        this.add({
            xtype: 'panel',
            layout: {
                type: 'vbox',
            },
            width: me.width - 20,
            height: 100,
            items: [
                me.eventTypeField,
                this.sandboxPanel,
            ],
        });
    },

    onChangeEventType: function() {
        var me = this;
        me.sandboxPanel.removeAll();
        var eventKind = this.eventTypeField.findRecordByValue(
            this.eventTypeField.getValue()
        );
        Ext.each(eventKind.data.sentence, function(part) {
            if (Ext.isObject(part)) {
                me.sandboxPanel.add({
                    xtype: 'combobox',
                    store: new Ext.data.Store({
                        fields: ['name', 'id'],
                        data: eventKind.data.possibilities[part.id],
                    }),
                    queryMode: 'local',
                    displayField: 'name',
                    editable: false,
                    style: {
                        marginLeft: 10,
                    },
                });
            } else {
                me.sandboxPanel.add({
                    xtype: 'label',
                    text: part,
                    style: {
                        marginLeft: 10,
                    },
                });
            }
        });
    },

});
