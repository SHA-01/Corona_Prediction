var list = []; var regex = /[+-]?\d+(\.\d+)?/g;
let table = document.querySelector('#mw-content-text > div.mw-parser-output > div:nth-child(8) > table > tbody');
children = Array.from(table.children);
children = children.slice(20, children.length).forEach(get); // foreach 메서드를 이용하여 표의 자식 요소에 함수를 메개변수에 넣는다.
function get(element) {
    if (typeof element.children[0] != 'undefined' && typeof element.children[1] != 'undefined') {
        let e = element.children[0].innerHTML.trim() || null
        t = e.replace('일', '').split("월 ");
        dates = "2020-"+t[0].padStart(2, "0") + "-" + t[1].padStart(2, "0");
        let numbers = element.children[1].innerHTML || null; 
        list.push([dates, numbers.replaceAll(',', '').match(regex)[0], numbers.replaceAll(',', '').match(regex)[1]])
    }
} //get 함수는 매개변수의 자식 요소 즉 날짜와 확진자수를 가져온후 다듬는다. (trim, replace, match, regex등을 이용한다.)
console.log(list)
function a(){
    return list
} return a(); // 자바스크립트 메모리에 저장된 변수를 파이썬로 리턴한다.
// ab = "5-26"; e = ab.split("-"); date = e[0].padStart(2, "0") + "-" + e[1].padStart(2, "0");