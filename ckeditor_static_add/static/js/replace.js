	CKEDITOR.replace( 'editor1', {

			extraPlugins: 'timestamp',

			// Rearrange toolbar groups and remove unnecessary plugins.
			toolbarGroups: [
				{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
				{ name: 'links' },
				{ name: 'insert' },
				{ name: 'document',	   groups: [ 'mode' ] },
				'/',
				{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
				{ name: 'paragraph',   groups: [ 'list', 'indent' ] },
				{ name: 'styles' },
				{ name: 'about' }
			],
			removePlugins: 'font,iframe,pagebreak,stylescombo,print,preview,save,smiley,pastetext,pastefromword',
			removeButtons: 'Anchor,Font,Strike,Subscript,Superscript',
		} );