function applyStyle() {
      var selection = window.getSelection();
      var selectedText = selection.toString();

      if (/[a-zA-Z]/.test(selectedText)) {
        // 드래그한 영역에 영어가 있는 경우 스타일 적용
        var span = document.createElement("span");
        span.className = "english";
        selection.getRangeAt(0).surroundContents(span);
      }
    }