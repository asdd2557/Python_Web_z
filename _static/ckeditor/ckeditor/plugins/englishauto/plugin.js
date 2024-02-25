/**
 * Copyright (c) 2014-2023, CKSource Holding sp. z o.o. All rights reserved.
 * Licensed under the terms of the MIT License (see LICENSE.md).
 *
 * Basic sample plugin inserting current date and time into the CKEditor editing area.
 *
 * Created out of the CKEditor Plugin SDK:
 * https://ckeditor.com/docs/ckeditor4/latest/guide/plugin_sdk_intro.html
 */

// Register the plugin within the editor.
CKEDITOR.plugins.add( 'englishauto', {

	icons: 'englishauto',

	init: function( editor ) {

		editor.addCommand( 'insertEnglishauto', {

			// Define the function that will be fired when the command is executed.
			exec: function( editor ) {
				 var selection = window.getSelection();
      var range = selection.getRangeAt(0);

      var selectedText = range.toString();
      var styledText = "";

      for (var i = 0; i < selectedText.length; i++) {
        var currentChar = selectedText.charAt(i);

        // 현재 글자가 영어인 경우
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

      var spanContainer = document.createElement("span");
      spanContainer.innerHTML = styledText;

      range.deleteContents();
      range.insertNode(spanContainer);
			}
		});

		// Create the toolbar button that executes the above command.
		editor.ui.addButton( 'Englishauto', {
			label: 'Insert Englishauto',
			command: 'insertEnglishauto',
			toolbar: 'insert',
		});
	}
	});


	//

	 function applyStyle() {

    }