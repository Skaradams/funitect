Ext.define('Funitect.view.ElementTab', {
    extend: 'Ext.panel.Panel',
    
    requires: [
        'Funitect.view.CommentsFrame',
        'Funitect.view.SketchesPreview',
        'Funitect.view.NewSketchWindow',
    ],

    xtype: 'element-tab',
    closable: true,
    layout: 'fit',

    constructor: function() {
    	var me = this;
        this.callParent(arguments);
        this.title = this.element.data.name;
        var vContainer = new Ext.container.Container({layout: 'vbox'});
        var commentsContainer = new Funitect.view.CommentsFrame();
        var hContainer = new Ext.container.Container({
            layout: 'hbox',
            items: [
                {xtype: 'container', flex: 1},
                {
                    xtype: 'sketches-preview', element: me.element,
                },
                {   
                    xtype: 'container',
                    flex: 3,
                    layout: 'vbox',

                    items: [
                        {
                            xtype: 'component',
                            autoEl: {
                                tag: 'span',
                                html: me.element.data.name,
                                cls: 'component-title',
                                style: {
                                    fontSize: '200%',
                                    marginBottom: 20,
                                },
                            },
                        },
                        {
                            xtype: 'button',
                            text: 'Add new sketch',
                            handler: function() {
                                var newSketchWindow = new Funitect.view.NewSketchWindow({
                                    component: me.component,
                                });
                                newSketchWindow.show();
                            },
                        },
                        commentsContainer,
                    ],

                    style: {
                        marginLeft: 50,
                    },
                },
                {xtype: 'container', flex: 1},
            ],
            style: {
                marginTop: 50,
            },
        });

        /*
        Add comments
        */
        var comments = new Funitect.store.ElementComments({
            element: me.element,
            listeners: {
                load: function() {
                    commentsContainer.setComments(comments);
                }
            }
        });


        me.add(hContainer);
        console.log(this.element.data.comments);
    },

});