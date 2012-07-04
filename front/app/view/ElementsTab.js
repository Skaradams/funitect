Ext.define('Funitect.view.ElementsTab', {
    extend: 'Ext.panel.Panel',
    
    requires: [
    	'Funitect.store.Elements',
    	'Funitect.view.ElementTab',
    ],

    
    xtype: 'elements-tab',
    closable: false,
    layout: 'fit',

    constructor: function() {
    	var me = this;
        this.callParent(arguments);
        this.title = this.elementKind.data.name;

		var vContainer = new Ext.container.Container({layout: 'vbox'});

        var hContainer = new Ext.container.Container({
        	layout: 'hbox',
        	items: [
        		{xtype: 'container', flex: 1},
				vContainer,        		
        		{xtype: 'container', flex: 1},
        	],
       	});
        var elements = new Funitect.store.Elements({
        	elementKind: this.elementKind,
        	listeners: {
	            load: function() {
	                elements.each(function(element) {
	                	vContainer.add({
	                		xtype: 'button',
	                		text: element.data.name,
	                		height: 40,
	                		width: 600,
	                		handler: function() {
	                			var elementTab = new Funitect.view.ElementTab({element: element});
	                			me.workspace.add(elementTab);
	                			elementTab.show();
	                		},
	                		style: {
		                		marginTop: 40,
	                		},
	                	});
	                });
	            }
        	},
    	});
        this.add(hContainer);
    },
   
});