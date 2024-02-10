    <script>
        document.addEventListener("DOMContentLoaded", function () {
            CKEDITOR.plugins.add('customPlugin', {
                init: function (editor) {
                    editor.addCommand('customPluginCommand', {
                        exec: function (editor) {
                            var selectedText = editor.getSelection().getSelectedText();
                            var boldText = '<strong>' + selectedText + '</strong>';
                            editor.insertHtml(boldText);
                            //alert('Selected Text: ' + selectedText);
                        }
                    });

                    editor.ui.addButton('CustomPlugin', {
                        label: '내 버튼',
                        command: 'customPluginCommand',
                        toolbar: 'insert'
                    });
                }
            });

            CKEDITOR.replace('editor', {
                extraPlugins: 'customPlugin'
            });
        });
    </script>


  <script>
        document.addEventListener("DOMContentLoaded", function () {
            CKEDITOR.replace('editor', {
                extraPlugins: 'customPlugin'
            });

            CKEDITOR.plugins.add('customPlugin', {
                init: function (editor) {
                    editor.addCommand('customPluginCommand', {
                        exec: function (editor) {
                            // 에디터의 현재 선택된 텍스트 가져오기
                            var selectedText = editor.getSelection().getSelectedText();

                            // 선택된 텍스트를 포함하는 p 엘리먼트 생성
                            var pElement = new CKEDITOR.dom.element('p');
                            pElement.setHtml(selectedText);

                            // p 엘리먼트에 data-tooltip 속성 추가
                            pElement.setAttribute('data-tooltip', '내용');

                            // 에디터의 현재 선택된 요소를 새로운 p 엘리먼트로 교체
                            editor.getSelection().getStartElement().remove();
                            editor.insertElement(pElement);
                        }
                    });

                    editor.ui.addButton('CustomPlugin', {
                        label: '내 버튼',
                        command: 'customPluginCommand',
                        toolbar: 'insert'
                    });
                }
            });
        });
    </script>