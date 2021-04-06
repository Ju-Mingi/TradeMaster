
from PIL import Image
from matplotlib import font_manager,rc
from matplotlib import pyplot as plt
from matplotlib import image as img
import random as rd
import time
import os
from tqdm import tqdm
import infolist
import updownwidth
from buysell import buysell, skiper, view_count


# matlotlib 차트에 한글 텍스트를 출력하기 위하여 작성
font_path = 'C:/Windows/Fonts/gulim.ttc'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

os.system("cls")

# 게임 시작시 출력 화면
print("☆★☆★☆★☆★☆★ 장사의 달인 ☆★☆★☆★☆★☆★\n\n")
print("\t물건을 사고 팔며 부자가 되어보자!\n\n")
print("★☆★☆★☆★☆★☆★☆★☆★☆★☆★★☆★☆★☆★☆\n\n\n")


leftMoney = 100000
investMoney = 0
cnt = 0
rate = rd.uniform(-5,5)

# 재화의 랜덤 등락폭을 설정

rdfruit, rdfood, rdcutlery, rdgame = updownwidth.rdlist()

# 재화의 가격 및 보유 수량

fruits = {'사과': 1000 + rdfruit, '포도': 2000 + rdfruit, '수박': 3000 + rdfruit, '블루베리': 2500 + rdfruit}
left_fruits = {'사과': 0, '포도': 0, '수박': 0, '블루베리': 0}

foods = {'김치': 3500 + rdfood, '카레': 3000 + rdfood, '삼겹살': 5000 + rdfood, '수프': 3000 + rdfood}
left_foods = {'김치':0, '카레':0, '삼겹살':0, '수프':0}

cutlery = {'나이프': 4500 + rdcutlery, '유리잔': 5500 + rdcutlery}
left_cutlery = {'나이프':0, '유리잔':0}

games = {'닌텐도스위치': 10000 + rdgame, 'Xbox': 20000 + rdgame, 'Ps5': 30000 + rdgame}
left_games = {'닌텐도스위치':0, 'Xbox':0, 'Ps5':0}

# 장사 시작
while cnt < 10:
    print("###########장사 종료까지 ", 10 - cnt, "일 남았습니다.###########", "\n\n")
    print("보유 금액은 ", leftMoney, "원 입니다.", "\n\n")
    print("투자금은 ", investMoney, "원 입니다.", "\n\n")

# 투자금 회수

    if investMoney > 0:
        withdraw = input("투자금을 회수 하시겠습니까? (y/n) : ")
        if withdraw == "y":
            leftMoney = leftMoney + investMoney
            investMoney = 0

# 금액 지불 후 무작위 정보 습득
    info = input("\n10000원을 지불하고 무작위 정보를 얻겠습니까? (y/n) : ")
    print("\n")
    if info == "y":
        leftMoney = leftMoney - 10000
        info_out = rd.choice(infolist.info_list) # 무작위 정보를 랜덤 선택하여 출력
        os.system("cls")
        print("\n")
        print(info_out)
        print("\n\n")

# 장사 시작 1일차에 정보 습득시 출력할 초기 가격 이미지 출력
        if cnt == 0:
            image1 = Image.open("pricestart.png")
            image1.show()
        else:
            image2 = Image.open("priceplt.png")
            image2.show()
    else:
        os.system("cls")

# 등락된 재화의 가격을 막대 차트로 표현

    font_path = 'C:/Windows/Fonts/gulim.ttc' # 차트의 한글 텍스트 지원을 위한 작성 코드
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
    plt.figure(figsize=(12, 6))
    y_tick = [i for i in range(0, 35000, 1500)]
    plt.yticks(y_tick)
    plt.bar(fruits.keys(), fruits.values())
    plt.bar(foods.keys(), foods.values())
    plt.bar(cutlery.keys(), cutlery.values())
    plt.bar(games.keys(), games.values())
    plt.savefig('priceplt.png')

# 모든 거래 스킵

    next_day = input("\n모든 거래를 스킵하시겠습니까? (y/n) : ")
    print("\n\n")
    while next_day != 'y':
        # 스킵 하지 않았을 때 거래를 진행
        while True: # 종목 선택 시 종료하지 않을 경우 선택 거래 반복
            print("1. 과일 2. 음식 3. 식기 4. 게임기 5. 거래 종료하기.\n")
            select = input("거래할 종목을 선택하세요 : ")

            if select == "1":
                (leftMoney,left_fruits) = buysell(left_fruits, leftMoney, fruits) # 과일의 구매 판매
                print("\n\n")
            elif select == "2":
                (leftMoney,left_foods) = buysell(left_foods, leftMoney, foods) # 음식의 구매 판매
                print("\n\n")
            elif select == "3":
                (leftMoney,left_cutlery) = buysell(left_cutlery, leftMoney, cutlery) # 식기의 구매 판매
                print("\n\n")
            elif select == "4":
                (leftMoney,left_games) = buysell(left_games, leftMoney, games) # 게임기의 구매 판매
                print("\n\n")
            elif select == "5": # 거래 종료
                print("\n\n모든 거래 완료!!")
                next_day = 'y'
                break # 거래 종료 조건 만족시 반복 루프 탈출

# 은행에 투자하는 기능

    # 장사 시작 9일 차에서는 은행 투자 옵션을 스킵.
    if cnt == 9:
        pass
    elif cnt < 9:
        invest = input("\n\n은행에 투자 하시겠습니까? (y/n) : ")
        # 투자할 경우
        if invest == "y":
            im = input("\n\n얼마를 투자하시겠습니까?\n\n")
            input_Money = int(im)
            if input_Money < leftMoney:
                leftMoney = leftMoney - int(im)
                investMoney = investMoney + int(im)
                print("\n\n떡상을 기대하세요.\n\n")
                investMoney = int(investMoney * rate)
        # 보유 금액보다 투자 금액이 높을 경우 경고 출력
            elif input_Money > leftMoney:
                warning = "\n\n불공정 거래 감지 !!!\n\n"
                print(warning*10)
                leftMoney = leftMoney
                time.sleep(2)
    # 투자 하지 않을 경우
        elif invest == "n":
            print("\n\n떡상 각인데...\n\n")
            check = input("다음으로 넘어가려면 엔터를 누르세요.")
            skiper()
            investMoney = int(investMoney * rate)

    # 모든 거래 종료시 출력 화면
    print("\n\n팁 : 일정 금액을 지불하면 정보를 얻을 수 있습니다.\n\n")
    print("\n\n팁 : 정보는 100% 정확하지 않습니다.\n\n")
    print("[system] 오늘의 거래 마감 중.")
    # 출력 화면에서 진행바를 표시하여 시간의 흐름 시각화
    for i in tqdm(range(100)):
        time.sleep(0.01)
    os.system("cls")
    # 거래 일수 증가
    cnt += 1

    # 보유한 전체 재화 개수 출력
    left_list = [left_fruits,left_foods,left_cutlery,left_games]
    for view in left_list:
        viewlist = view_count(view)


os.system("cls")

# 잔여 금액에 따른 등급 부여

if leftMoney >= 100000000:
    print("당신은 금수저 입니다!")
    gold = img.imread("gold.png")
    goldimage = Image.open("gold.png")
    goldimage.show()
elif leftMoney >= 10000000:
    print("당신은 은수저 입니다!")
    silver = img.imread("silver.png")
    silverimage = Image.open("silver.png")
    silverimage.show()
elif leftMoney >= 1000000:
    print("당신은 똥수저 입니다!")
    copper = img.imread("copper.png")
    copperimage = Image.open("copper.png")
    copperimage.show()
else:
    print("에잇 거지!!!!!")
    beggar = img.imread("beggar.png")
    beggarimage = Image.open("beggar.png")
    beggarimage.show()

exit_game = input("\n\n게임을 끝내려면 enter를 누르세요.")
os.system("exit")


