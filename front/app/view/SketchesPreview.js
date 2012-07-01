Ext.define('Funitect.view.SketchesPreview', {
	extend: 'Ext.container.Container',

	requires: [
		'Funitect.store.Sketches',
	],

	xtype: 'sketches-preview',

	layout: 'vbox',


	width: window.innerWidth / 3,
	height: window.innerWidth / 3,

	constructor: function() {
		var me = this;
		this.callParent(arguments);

		this.sketchesPreviewGrid = {};

		for (var row = 0; row < 3; row++) {
			me.sketchesPreviewGrid[row] = {}
			var hContainer = new Ext.container.Container({
				layout: 'hbox',
			});
			for (var col = 0; col < 3; col++) {
				var color = null;
				if (row % 2 == 0 && col % 2 != 0 || col % 2 == 0 && row % 2 != 0) {
					var color = '#cfcfcf';
				} else {
					var color = '#efefff';
				}
				var img = new Ext.Img({
					width: window.innerWidth / 9,
					height: 'auto',
				});
				var sketchContainer = new Ext.container.Container({
					style: {
						backgroundColor: color,
						borderRadius: 15,
						border: '1px solid white',
					},
					id: 'sketch-preview-' + me.id + '-' + row + '-' + col,
					width: window.innerWidth / 9,
					height: window.innerWidth / 9,
					items: [img],
				});
				me.sketchesPreviewGrid[row][col] = img;
				hContainer.add(sketchContainer);
			}
			me.add(hContainer);
		}

		var sketches = new Funitect.store.Sketches({
            element: me.element,
            listeners: {
                load: function() {
                	var row = 0;
                	var col = 0;
                    sketches.each(function(sketch) {
                    	if(row < 3 && col < 3) {
                    		me.sketchesPreviewGrid[row][col].setSrc(sketch.data.src);
	                    	col++;
	                    	if(col == 2) {
	                    		col = 0;
	                    		row++;
	                    	}
                    	}
                    });
                }
            }
        });
	}

});