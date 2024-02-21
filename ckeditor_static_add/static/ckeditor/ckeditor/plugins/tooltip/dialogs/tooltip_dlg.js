
CKEDITOR.dialog.add('tooltip_dlg', function (editor) {
    return {
        title: 'TooltipInsert', // text shown titlebar.
        minWidth: 400,
        minHeight: 200,

        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    // UI elements of the first tab should be defined here.
                    {
                        type: 'text',
                        id: 'id-gisturi',
                        label: 'GitHub Gist ID',
                        validate: CKEDITOR.dialog.validate.notEmpty("GitHub Gist ID field cannot be empty.")
                    }
                ]
            },
            {
                id: 'tab-adv',
                label: 'Advanced Settings',
                elements: [
                    // UI elements of the second tab will be defined here.
                    {
                        type: 'text',
                        id: 'id-dummy',
                        label: 'title',
                    }
                ]
            }
        ],
        onOk: function () {
            var dialog = this;
            var selectedText = editor.getSelection().getSelectedText();
            var spanElement = new CKEDITOR.dom.element('span');
            spanElement.setHtml(selectedText);
            spanElement.setAttribute('data-tooltip', dialog.getValueOf('tab-basic', 'id-gisturi'));
            editor.insertElement(spanElement);
        }
    };
});