Ext.define('Funitect.view.NewSketchWindow', {
    extend: 'Ext.window.Window',

    requires: [
        'Funitect.model.Sketch',
    ],

    layout: 'fit',

    title: 'Add new sketch from your hard disk',

    resizeable: false,
    closable: true,

    width: 300,

    constructor: function() {
        var me = this;
        this.callParent(arguments);
        this.add({
            xtype: 'form',
            layout: 'hbox',
            items: [
                {xtype: 'filefield', flex: 2, name: 'sketch'},
            ],
            buttons: [{
                text: 'Upload',
                handler: function() {
                    var form = this.up('form').getForm();
                    if(form.isValid()){
                        form.submit({
                            url: '/upload-sketch/',
                            method: 'post',
                            waitMsg: 'Uploading new sketch ...',
                            success: function(form, action) {
                                me.onUploadResponse(action.result);
                            },
                            failure: function(form, action) {
                                me.onUploadResponse(action.result);
                            },
                        });
                    }
                },
            }],
        });
    },

    onUploadResponse: function(result) {
        var me = this;
        var sketch = new Funitect.model.Sketch();
        sketch.getProxy().extraParams = {
            element: me.element.data.id,
            src: 'http://' + document.location.host + result.url,
        }
        sketch.save({
            callback: function() {
                me.close();
                if (Ext.isFunction(me.next)) {
                    me.next();
                }
            }
        });
    },

});
