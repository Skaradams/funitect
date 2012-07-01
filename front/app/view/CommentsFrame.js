Ext.define('Funitect.view.CommentsFrame', {
	extend: 'Ext.container.Container',

	requires: [
		'Funitect.store.ElementComments',
	],

	xtype: 'comments-frame',

	layout: 'vbox',

	setComments: function(comments) {
		var me  = this;
        comments.each(function(comment) {
            me.add({
                xtype: 'container',
                layout: 'vbox',

                items: [
                    {
                        xtype: 'component',
                        autoEl: {
                            tag: 'span',
                            html: comment.data.user,
                            cls: 'comment-user',
                        },
                        style: {
                            fontSize: '110%',
                            fontWeight: 'bold',
                            marginBottom: 10,
                            marginTop: 5,
                        },
                    },
                    {
                        xtype: 'component',
                        autoEl: {
                            tag: 'span',
                            html: comment.data.text,
                            cls: 'comment-text',
                        },
                        style: {
                            marginLeft: 10,
                        },
                    },
                ],
                style: {
                    marginTop: 20,
                }
            })
        });
	}
});