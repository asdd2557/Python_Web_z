CKEDITOR.plugins.add('englishauto', {
  icons: 'englishauto',

  init: function (editor) {
    editor.addCommand('insertEnglishauto', {
      exec: function (editor) {
        var selection = editor.getSelection();
        var selection_english = '';
        var styledText = "";

                if (selection) {
          var selectedText = selection.getSelectedText();
          if (selectedText) {


        for (var i = 0; i < selectedText.length; i++){
            var currentChar = selectedText.charAt(i);
                    if (/^[a-zA-Z]+$/.test(currentChar)) {
          // 한글이 나오거나 공백이 나올 때까지 글자를 묶음
          var englishWord = "";
          while (/^[a-zA-Z]+$/.test(currentChar) && i < selectedText.length) {
            englishWord += currentChar;
            i++;
            currentChar = selectedText.charAt(i);
          }

          // 묶인 영어에 스타일 적용
          styledText += '<span class="english">' + englishWord + '</span>';

        } else {
          // 영어가 아닌 경우 그대로 추가
          styledText += currentChar;
        }

        }



          }
          console.log(styledText);
        editor.setData(styledText);
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
