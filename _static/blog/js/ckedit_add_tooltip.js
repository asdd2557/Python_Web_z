
document.addEventListener("DOMContentLoaded", function () {     //HTML 문서의 로딩이 완료되었을때 실행되는 이벤트 리스너 등록
    // 기존 CKEditor 인스턴스를 찾아서 ID 가져오기
    var existingCkEditorId = CKEDITOR.instances['id_content'];

    // CKEditor 인스턴스가 이미 초기화되지 않은 경우 초기화
    if (!existingCkEditorId) {
        CKEDITOR.replace('id_content', {
            // 필요한 설정들 추가
        });
    } else {
        // 기존 CKEditor에 플러그인 추가
        existingCkEditorId.addCommand('customPluginCommand', {
            exec: function (editor) {
                var selectedText = editor.getSelection().getSelectedText();

                // 새 창 열기
                var newWindow = window.open('', 'customFormWindow', 'width=300,height=200');
                newWindow.document.body.innerHTML = '<html><head><title>Custom Form</title></head><body>' +
                    '<label for="customInput">값 입력:</label>' +
                    '<input type="text" id="customInput">' +
                    '<button onclick="submitCustomForm()">확인</button>' +
                    '</body></html>';

                // 부모 창에 함수 정의
                newWindow.submitCustomForm = function () {
                    var inputValue = newWindow.document.getElementById('customInput').value;

                    var pElement = new CKEDITOR.dom.element('span');
                    pElement.setHtml(selectedText);
                    pElement.setAttribute('data-tooltip', inputValue);

                    editor.getSelection().getStartElement().remove();
                    editor.insertElement(pElement);

                    // 새 창 닫기
                    newWindow.close();
                };
            }
        });

        existingCkEditorId.ui.addButton('CustomPlugin', {
            label: '내 버튼',
            command: 'customPluginCommand',
            toolbar: 'insert'
            icons: 'customPluginCommand'

        });
    }
});

