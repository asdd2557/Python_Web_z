CKEDITOR.plugins.add('tooltip', {
    icons: 'tooltip',
    init: function (editor) {

        editor.addCommand('insertTooltip', new CKEDITOR.dialogCommand('tooltip_dlg'));

        // Create the toolbar button that executes the above command.
        editor.ui.addButton('Tooltip', {
            label: 'Insert Tooltip',
            command: 'insertTooltip',
            toolbar: 'insert',
        });
    CKEDITOR.dialog.add('tooltip_dlg',this.path+'dialogs/tooltip_dlg.js');
    }
});


