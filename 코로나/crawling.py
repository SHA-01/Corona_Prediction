from selenium import webdriver
import time
import csv
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(r'C:\Users\82102\Downloads\chromedriver_win32 (3)\chromedriver.exe', options=options)
driver.get("https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%BD%94%EB%A1%9C%EB%82%9819_%EB%B2%94%EC%9C%A0%ED%96%89")
driver.implicitly_wait(300) #위키피디아 코로나 검색결과에 접속한다.
script = """var list = []; var regex = /[+-]?\d+(\.\d+)?/g;
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
} return a();"""
print("데이터를 가져오고 있습니다.")
data = driver.execute_script(script) #추가 확진자수와 날짜를 가져오는 자바스크립트 코드를 실행한다.
driver.close()
f = open(f'data.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(["date", "Cumulative", "Additional"])  # csv파일의 첫번째 줄을 작성한다.
for i in data:
    csvWriter.writerow(i) #csv파일에 저장한다.
f.close()
print("데이터를 불러오는데 성공했습니다!")
