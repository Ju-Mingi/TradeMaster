import os

# 게임 실행 출력화면을 초기화 함수
# 이전 거래 내역을 지울 때 사용
def skiper():
    os.system("cls")

def showprice(fruits):
    print("\n------------------------------------------------------")

    print("\n                  ★오늘의 시세★\n")
    for show in fruits:
        print(" ",show,fruits[show],end=" ")
    print("\n")
    print("\n------------------------------------------------------\n")

def buysell(left_fruits, leftMoney, fruits):
    for i in fruits:
        showprice(fruits) # 재화 가격 출력
        print("현재 보유한", i, " 개수 :", left_fruits[i], "\n\n")
        print("현재 잔액은 ", leftMoney, "원 남았습니다.\n\n")
        fruit_buy = input(f"{i}를 몇 개 구매하시겠습니까?(구매X : 0) ")
        print("\n------------------------------------------------------\n")
        if int(fruit_buy) * fruits[i] > leftMoney:  # 보유 금액보다 구매액이 클 경우
            print("잔돈이 충분하지 않습니다.\n\n")
            print("보유한 %s 개수 :  %d" % (i, left_fruits[i]), "\n")
        else:
            left_fruits[i] = left_fruits[i] + int(fruit_buy) # 구매액보다 보유 금액이 클 경우
            leftMoney = leftMoney - int(fruit_buy) * int(fruits[i])
            print("\n현재 잔액은 ", leftMoney, "원 남았습니다.\n\n")
        if left_fruits[i] > 0: # 보유한 재화를 판매하는 경우 판매 진행
            skiper()
            print("현재 보유한 %s 개수 :  %d" % (i, left_fruits[i]), "\n\n")
            fruits_sell = input("%s를 몇 개 판매하시겠습니까?(판매X : 0) " % i)
            print("\n------------------------------------------------------\n")
            # 판매할 개수가 보유한 개수보다 작거나 같고 수량이 0이 아닐 경우 판매 진행 계속
            if 0 <= int(fruits_sell) <= left_fruits[i]:
                leftMoney = leftMoney + int(fruits_sell) * int(fruits[i])
                left_fruits[i] = left_fruits[i] - int(fruits_sell)

                skiper()
                print("\n",i,"거래 완료!!\n")
                print("\n현재 보유한 %s 개수 :  %d" % (i, left_fruits[i]), '\n')
                print("\n현재 잔액은 ", leftMoney, "원 남았습니다.\n\n")
            # 보유한 개수가 판매 금액보다 적을 경우 판매 거절
            else:
                print("거래는 정당해야합니다. 다음날에 다시 시도하세요.\n\n")
        input("< 다음으로 넘어가려면 엔터를 누르세요 >")
        skiper()
    # 거래 결과 보유 금액과 개수를 반환
    return leftMoney,left_fruits

def view_count(left_fruits):
    print("\n------------------------------------------------------")
    print("\n                  ★보유한 개수★\n")
    for count in left_fruits:
        print("   ",count, left_fruits[count], end=" ")
    print("\n")
    print("\n------------------------------------------------------")

