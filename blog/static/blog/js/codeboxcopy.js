
// 코드 태그 옆에 자동으로 카피 버튼을 추가하는 함수
document.addEventListener('DOMContentLoaded', function() {
    var codeBlocks = document.querySelectorAll('code');

    codeBlocks.forEach(function(codeBlock) {
         var languageClass = '';
         var classes = codeBlock.className.split(' ');
                 for (var i = 0; i < classes.length; i++) {
            if (classes[i].startsWith('language-')) {
                // 'language-' 다음의 부분을 변수에 저장
                languageClass = classes[i].substring('language-'.length);
                 addCopyButton(codeBlock, classes);
                break;
            }
        }

    });
});

// 코드 태그 위에 카피 버튼을 추가하는 함수
function addCopyButton(codeContainer, classLanguage) {
    var copyButtonContainer = document.createElement('p');
    copyButtonContainer.className = 'copy-container';
    var containerName = document.createElement('span');
    containerName.className = 'copy-container-name';
    containerName.textContent = classLanguage;

    var copyButton = document.createElement('button');
    copyButton.className = 'copy-button';
    copyButton.textContent = 'Copy code';

    // 수정된 부분: codeContainer를 copyCode 함수에 전달
    copyButton.onclick = function() {
    copyCode(codeContainer);
    };
    var parentContainer = codeContainer.parentNode;
    parentContainer.insertBefore(copyButtonContainer, codeContainer);
    //codeContainer.insertBefore(copyButtonContainer, codeContainer.firstChild);
    copyButtonContainer.appendChild(copyButton);
    copyButtonContainer.appendChild(containerName);
}

// 코드 태그의 텍스트를 복사하는 함수
function copyCode(codeBlock) {
    var range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);

    // 복사 명령 수행
    var success = document.execCommand('copy');


        // 복사 성공 시 버튼 텍스트 변경 후 일정 시간 뒤에 원래의 텍스트로 복구
        var copyButton = codeBlock.parentNode.querySelector('.copy-button');
        if (copyButton) {
            copyButton.textContent = 'Copied!';
            setTimeout(function() {
                copyButton.textContent = 'Copy code';
            }, 2000); // 2초 후에 원래 텍스트로 변경 (2000은 2초를 밀리초로 나타낸 값)
        }

    window.getSelection().removeAllRanges();
}
