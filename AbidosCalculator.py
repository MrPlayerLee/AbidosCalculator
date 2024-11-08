# import module
import os
import time

# Abidos Calculator

class AbidosCalc:
    def __init__(self):
        self.common = 0
        self.uncommon = 0
        self.rare = 0
        self.abidos = 0
        self.dust = 0
        self.sec = 0
        self.posible_common = 0
        self.posible_uncommon = 0
        self.posible_abidos = 0
        self.need_common = 86
        self.need_uncommon = 45
        self.need_abidos = 33
        self.comm_unccom = 0
        self.dustuse = 0
        self.sequnce_common = 0
        self.sequnce_uncommon = 0
        self.origin_common = 0
        self.origin_uncommon = 0
        self.origin_rare = 0
        self.origin_abidos = 0
        self.oriposible_common = 0
        self.oriposible_uncommon = 0
        self.oriposible_abidos = 0
    
    def timer(self, sec, string):
        print("\n\n\n")
        for i in range(sec, 0, -1):
            print(f"{i}초후 {string}를 진행합니다.")
            time.sleep(1)
        return self.sec

    def inputData(self):
        try:
            self.common = int(input("소지하고 있는 일반재료의 갯수 \n >> "))
            self.uncommon = int(input("소지하고 있는 고급재료의 갯수 \n >> "))
            self.rare = int(input("소지하고 있는 희귀재료(시즌2)의 갯수\n(경고. 해당 질문은 채광과 벌목만 해당됩니다. 그 외에는 0을 입력해주세요.)\n >> "))
            self.abidos = int(input("소지하고 있는 아비도스재료의 갯수 \n >> "))
            self.dust = int(input("소지하고 있는 생활 가루의 갯수 \n >> "))
            self.origin_common = self.common
            self.origin_uncommon = self.uncommon
            self.origin_rare = self.rare
            self.origin_abidos = self.abidos
        except ValueError:
            print("숫자만 입력하십시오.")
        return

    def showData(self):

        self.posible_common = self.common // self.need_common
        self.posible_uncommon = self.uncommon // self.need_uncommon
        self.posible_abidos = self.abidos // self.need_abidos

        print(f"일반재료: {self.common} 개 (제작가능: {self.posible_common})")
        print(f"고급재료: {self.uncommon} 개 (제작가능: {self.posible_uncommon})")
        #print(f"희귀재료: {self.rare} 개")
        print(f"아비도스: {self.abidos} 개 (제작가능: {self.posible_abidos})")
        print(f"생활가루: {self.dust} 개")
        return

    def calc1(self): # 티어2 희귀 재료를 모두 생활가루로 변환 후 아비도스 재료로 변환
        self.common = self.common + (self.rare // 5 * 50)
        self.rare = self.rare % 5
        return


    def calc2(self): # 일반, 희귀 둘중 더 많은 부분을 생활가루로 변환.
        if self.posible_uncommon < self.posible_common: 
            print("일반재료가 더 많습니다. 생활가루로 변환합니다.")
            self.comm_unccom = (self.posible_common - self.posible_uncommon) * 86 // 100 * 80 #일반재료가 더 많을때
            self.dust = self.dust + self.comm_unccom
            self.common = self.common - (self.posible_common - self.posible_uncommon) * 86
        else:
            print("고급재료가 더 많습니다. 생활가루로 변환합니다.")
            self.comm_unccom = (self.posible_uncommon - self.posible_common ) * 45 // 50 * 80 #희귀재료가 더 많을때
            self.dust = self.dust + self.comm_unccom
            self.uncommon = self.uncommon - (self.posible_uncommon - self.posible_common) * 45
        return

    def calc3(self, string): # 생활 가루를 아비도스로 변환.
        print(f"{string}")
        self.abidos += self.dust // 60 * 10
        self.dust %= 60
        return
    
    def calc4(self): # 각 제작재료의 가능횟수를 순차적으로 1씩 삭감하여 가루로 변환 후 100개일시 아비도스로 변환.
        while self.posible_abidos < min(self.posible_common, self.posible_uncommon):
            time.sleep(0.01)
            os.system("cls")
            print("아비도스로 변환 시뮬레이션중...")
            self.common -= 86
            self.uncommon -= 45
            self.sequnce_common += 86
            self.sequnce_uncommon += 45
            if self.sequnce_common > 100:
                self.sequnce_common - 100
                self.dust += 80
            if self.sequnce_uncommon > 50:
                self.sequnce_uncommon - 50
                self.dust += 80
            if self.dust > 100:
                self.calc3("실시간으로 모든 생활가루를 아비도스 재료로 변환중...")
            self.showData()
        return
    
    def end(self):

        self.oriposible_common = self.origin_common // self.need_common
        self.oriposible_uncommon = self.origin_uncommon // self.need_uncommon
        self.oriposible_abidos = self.origin_abidos // self.need_abidos

        print("\n\n원래 재료:")
        print(f"일반재료 : {self.origin_common} (제작가능: {self.oriposible_common})")
        print(f"고급재료 : {self.origin_uncommon} (제작가능: {self.oriposible_uncommon})")
        print(f"희귀재료 : {self.origin_rare} (교환가능: {self.origin_rare // 5})")
        print(f"아비도스 : {self.origin_abidos} (제작가능: {self.oriposible_abidos})")

        self.oriposible_common = (self.origin_common + self.origin_rare // 5 * 50) // self.need_common

        print("\n\n최종 결과:")
        print("\n일반재료 : ")
        print(f"< 원래재료 : {self.origin_common}개 > + < 변환된 희귀재료(T2) : {self.origin_rare // 5 * 50}개 >")
        print(f"일반재료 최종 : \n{self.origin_common + self.origin_rare // 5 * 50}개 -> {self.common}개 (제작가능: {self.oriposible_common}회 -> {self.posible_common}회) [ {((self.origin_common + self.origin_rare // 5 * 50) - self.common) // 100}회 교환 ]\n")
        print("고급재료 : ")
        print(f"{self.origin_uncommon}개 -> {self.uncommon}개 (제작가능: {self.oriposible_uncommon}회 -> {self.posible_uncommon}회) [ {(self.origin_uncommon - self.uncommon) // 50}회 교환 ]\n")
        print("아비도스 : ")
        print(f"{self.origin_abidos}개 -> {self.abidos}개 (제작가능: {self.oriposible_abidos}회 -> {self.posible_abidos}회)\n")

calc = AbidosCalc()
calc.inputData()


os.system("cls")
print("현재 보유중인 제작재료:")
calc.calc1()
calc.showData()
calc.timer(3, "다음 단계")

os.system("cls")
calc.calc2()
calc.showData()
calc.timer(3, "다음 단계")

os.system("cls")
calc.calc3("모든 생활가루를 아비도스 재료로 변환합니다.")
calc.showData()
calc.timer(3, "다음 단계")

os.system("cls")
calc.calc4()


print("아비도스 변환 시뮬레이션 완료.")
calc.timer(3, "정리 단계")

os.system("cls")
print("현재 보유중인 제작재료:")
calc.showData()
calc.end()

os.system("pause>nul")