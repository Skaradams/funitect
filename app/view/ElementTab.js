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
        var newNoteField = new Ext.form.field.TextArea({
            name: 'note',
            width: window.innerWidth / 5,
            height: window.innerWidth / 10,
        });
        var vContainer = new Ext.container.Container({layout: 'vbox'});
        this.commentsContainer = new Funitect.view.CommentsFrame();
        this.sketchesPreview = new Funitect.view.SketchesPreview({
            element: me.element,
        });
        var hContainer = new Ext.container.Container({
            layout: 'hbox',
            items: [
                {xtype: 'container', flex: 1},
                me.sketchesPreview,
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
                                    element: me.element,
                                    next: function() {
                                        me.onNewSketch();
                                    },
                                });
                                newSketchWindow.show();
                            },
                        },
                        me.commentsContainer,
                        {
                            xtype: 'form',
                            layout: 'hbox',
                            items: [
                                newNoteField,
                                {
                                    xtype: 'button',
                                    text: 'Add note',
                                    handler: function() {
                                        var comment = new Funitect.model.ElementComment();
                                        comment.getProxy().extraParams = {
                                            element: me.element.data.id,
                                            text: Ext.htmlEncode(newNoteField.getValue()),
                                        }
                                        comment.save({
                                            callback: function() {
                                                me.updateComments();
                                            }
                                        });

                                    },
                                    style: {
                                        marginLeft: 30,
                                    },
                                },
                            ],
                            style: {
                                marginTop: 30,
                            },
                        },
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
        me.add(hContainer);
        this.updateComments();
    },


    updateComments: function() {
        var me = this;
        var comments = new Funitect.store.ElementComments({
            element: me.element,
            listeners: {
                load: function() {
                    me.commentsContainer.setComments(comments);
                }
            }
        });
    },

    onNewSketch: function() {
        this.sketchesPreview.reset();
    },

});