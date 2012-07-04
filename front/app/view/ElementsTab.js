Ext.define('Funitect.view.ElementsTab', {
    extend: 'Ext.panel.Panel',

    requires: [
        'Funitect.store.Elements',
        'Funitect.view.ElementTab',
        'Funitect.view.NewElementWindow',
    ],


    xtype: 'elements-tab',
    closable: false,
    layout: 'fit',

    constructor: function() {
        var me = this;
        this.callParent(arguments);
        this.title = this.elementKind.data.name;

        this.vContainer = new Ext.Panel({
            layout: 'vbox',
            autoScroll: true,
            height: window.innerWidth / 3,
        });


        this.addButton = new Ext.button.Button({
            text: '+1 ' + me.elementKind.data.name,
            style: {
                marginTop: 30,
                marginLeft: window.innerWidth / 5,
                fontSize: '200%',
            },
            handler: function() {
                var newElementWindow = new Funitect.view.NewElementWindow({
                    elementKind: me.elementKind,
                    next: function(){
                        me.reset();
                    },
                });
                newElementWindow.show();
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
        var elements = new Funitect.store.Elements({
            elementKind: this.elementKind,
            listeners: {
                load: function() {
                    elements.each(function(element) {
                        me.addElement(element);
                    });
                    me.vContainer.scrollBy(0, 100000, true);
                }
            },
        });
    },

    addElement: function(element) {
        var me = this;
        if(!Ext.isObject(Ext.getCmp(me.elementKind + '-' + element.data.id))) {
            this.vContainer.add({
                xtype: 'button',
                text: element.data.name,
                height: 40,
                width: 520,
                id: me.elementKind + '-' + element.data.id,
                handler: function() {
                    var elementTab = new Funitect.view.ElementTab({element: element});
                    me.workspace.add(elementTab);
                    elementTab.show();
                },
                style: {
                    marginTop: 40,
                    marginLeft: 40,
                    marginRight: 40,
                },
            });
        }
    },

});
