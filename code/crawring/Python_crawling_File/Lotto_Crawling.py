import requests
import bs4

while True:
    keyword = input("검색을 원하는 키워드를 입력하세요. ( 0을 입력하면 종료 )")
    if keyword == "0":
        break

    sorting = [['&s=8','<판매 인기 순>'],['&s=1','<낮은 가격 순]>'],['','<G마켓 랭크 순>'],['&s=2','<높은 가격 순>']]
    

    # 기존 : G마켓의 마스크 상품 정보
    print("< G마켓의", keyword, "상품 정보 >")
    
    for sort in sorting:
        URL = "https://browse.gmarket.co.kr/search?keyword=" + keyword + sort[0]
        raw = requests.get(URL)
        html = bs4.BeautifulSoup(raw.text, 'html.parser')
        box = html.find('div', {'class' : 'section__module-wrap', 'module-design-id' : '15'})
        items = box.find_all('div', {"class" : 'box__item-container'})

        print(sort[1])

        for item in items[:4]:
            title = item.find('span', {'class' : 'text__item'})
            price = item.find('strong', {'class' : 'text__value'})
            print("이름 : ", title.text)
            print('가격 : ', price.text)
        print()