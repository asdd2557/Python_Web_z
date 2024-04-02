CKEDITOR.plugins.add('englishauto', {
  icons: 'englishauto',

  init: function (editor) {
    editor.addCommand('insertEnglishauto', {
      exec: function (editor) {
        var selection = editor.getSelection();
        var ranges = selection.getRanges();

        for (var i = 0; i < ranges.length; i++) {
          var range = ranges[i];
          var selectedText = range.toString();

          // 굵게 백그라운드 주황색으로 스타일 적용
          var styledText = '<span style="font-weight: bold; background-color: orange;">' + selectedText + '</span>';

          // 현재 선택된 텍스트를 삭제하고 스타일이 적용된 텍스트를 삽입
          range.deleteContents();
          range.insertNode(CKEDITOR.dom.element.createFromHtml(styledText, editor.document));
        }
      }
    });

    editor.ui.addButton('Englishauto', {
      label: 'Insert Englishauto',
      command: 'insertEnglishauto',
      toolbar: 'insert',
    });
  }
});
