Ext.define('Funitect.view.NewElementWindow', {
    extend: 'Ext.window.Window',

    requires: [
        'Funitect.model.Element',
    ],

    layout: 'fit',

    title: 'Create new',

    resizeable: false,
    closable: true,

    width: 300,

    constructor: function() {
        var me = this;
        this.callParent(arguments);
        var nameField = new Ext.form.field.Text({
            flex: 2, name: 'name'
        });
        this.add({
            xtype: 'form',
            layout: {
                type: 'hbox',
                align: 'middle',
            },
            items: [
                {xtype: 'label', flex: 1, text: 'Name :', style: {marginLeft: 10}},
                nameField,
                {
                    xtype: 'button',
                    flex: 1,
                    text: 'OK',
                    style: { marginLeft: 10 },
                    handler: function() {
                        var element = new Funitect.model.Element({
                            name: Ext.htmlEncode(nameField.getValue()),
                        });
                        element.getProxy().extraParams = {
                            kind: me.elementKind.data.id,
                            name: Ext.htmlEncode(nameField.getValue()),
                        };
                        element.save({
                            callback: function() {
                                me.close();
                                if (Ext.isFunction(me.next)) {
                                    me.next();
                                }
                            }
                        });
                    },
                },
            ],
        });
    },

});
