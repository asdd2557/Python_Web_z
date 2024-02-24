// JavaScript
document.addEventListener("DOMContentLoaded", function() {
  var sections = document.querySelectorAll("section");

  sections.forEach(function(section) {
    var paragraphs = section.querySelectorAll("p");

    paragraphs.forEach(function(paragraph) {
      var characters = paragraph.textContent.split('');

      paragraph.innerHTML = characters.map(function(char) {
        // 영어 글자인 경우
        if (/[a-zA-Z]/.test(char)) {
          return '<span class="english">' + char + '</span>';
        }
        // 그 외의 경우 (한글 등)
        return char;
      }).join('');
    });
  });
});
