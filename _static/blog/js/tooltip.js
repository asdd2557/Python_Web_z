
     let tooltipElem; // tooltipElem 함수 선언

    document.onmouseover = function(e) {    //document.onmmouserover 마우스가 어떤 요소 위로 올라갈때 발생하는 이벤트를 처리한다.
      let target = event.target; //마우스 이벤트가 발생한 요소를 가져와 taget변수에 저장함

      // data-tooltip 속성이 있는 요소
      let tooltipHtml = target.dataset.tooltip;

      if (!tooltipHtml) //target의 tooltup 값이 없다면 발생
      return;

      // 툴팁 요소를 만듭니다.

      tooltipElem = document.createElement('div'); //div 테그 생성하여 tooltipElem 함수에 저장
      tooltipElem.className = 'texttip';    //tooltipElem의 클래스 이름을 tooltip으로 바꿈
      tooltipElem.innerHTML = tooltipHtml;  //tooltupElem의 내용을 위에서 저장했던 tooltipHtml함수를 tooltupElemdiv 테그의 내용에 선언합니다.
      document.body.append(tooltipElem);  // tooltipElem을 body에 추가합니다.
      // 툴팁 요소를 data-tooltip 속성이 있는 요소 위, 가운데에 위치시킵니다.
      let coords = target.getBoundingClientRect();  //target의 위치 정보를 가져와 coords 변수에 저장
      let left = coords.left + (target.offsetWidth - tooltipElem.offsetWidth) / 2;
      //target.offsetWidth는 설명하려는 객체의 가로 길이, tip box 가로 길이, coords.left는 target의 left 위치값값

      if (left < 0) left = 0; // 툴팁이 창 왼쪽 가장자리를 넘지 않도록 합니다. 그리고 Tooltip이 -에 오지 않도록 합니다.

      let top = coords.top - tooltipElem.offsetHeight - 5;
      if (top < 0) { // 툴팁이 창 위로 넘치면 요소 아래에 보여줍니다.
        top = coords.top + target.offsetHeight + 5;
      tooltipElem.style.left = left + 'px';
      }else
      {
      tooltipElem.style.left = coords.left + 'px';
      }

      tooltipElem.style.top = top + 'px';   //위에서 위치 다 계산하고 적용
    };

    document.onmouseout = function(e) { //마우스가 요소를 벗어날때 발생하는 이벤트

      if (tooltipElem) {
        tooltipElem.remove();
        tooltipElem = null;
      }
    };

