Ext.define('Funitect.view.NewSketchWindow', {
    extend: 'Ext.window.Window',

    layout: 'fit',

    title: 'Add new sketch from your hard disk',

    resizeable: false,
    closable: true,

    width: 300,

    items: [
        {
            xtype: 'form',
            layout: 'hbox',
            items: [
                {xtype: 'filefield', flex: 2, name: 'sketch'},
                {xtype: 'hidden', name: 'component', id: 'component-field'},
            ],
            buttons: [{
                text: 'Upload',
                handler: function() {
                    var form = this.up('form').getForm();
                    if(form.isValid()){
                        form.submit({
                            url: '/upload-sketch/',
                            method: 'post',
                            params: {
                                format: 'json',
                            },
                            waitMsg: 'Uploading new sketch ...',
                            success: function(fp, o) {
                                Ext.Msg.alert('Success', 'Your photo "' + o.result.file + '" has been uploaded.');
                            }
                        });
                    }
                },
            }],
        }
    ],

    show: function() {
        this.callParent(arguments);
        Ext.getCmp('component-field').setValue(this.component.data.id);
    },

});