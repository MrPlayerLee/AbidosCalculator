# import module
import os
import time
import sys
import datetime

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
        self.sequnce_common = 0
        self.sequnce_uncommon = 0
        self.origin_common = 0
        self.origin_uncommon = 0
        self.origin_rare = 0
        self.origin_abidos = 0
        self.origin_dust = 0
        self.rareToCommon = 0
        self.probeComToDust1 = 0
        self.probeComToDust1_ = 0
        self.probeResultDust = 0
        self.probeDust1 = 0
        self.probeDust1_ = 0
        self.probeDustToAbidos = 0
        self.probeComToDust2 = 0
        self.probeDust2 = 0
        self.probeUncomToDust = 0
        self.probeDust3 = 0
        self.probeAbidos = 0
        self.probeComm_Unccom = True
        self.probeSeq = 0
        self.calcIntegrity = True
    
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
            self.origin_dust = self.dust
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

    def calc1(self): # 티어2 희귀재료를 일반재료로 변환
        self.common = self.common + (self.rare // 5 * 50)
        self.rareToCommon = self.rare // 5 * 50
        self.rare = self.rare % 5
        return


    def calc2(self): # 일반, 희귀 둘중 더 많은 부분을 생활가루로 변환.
        if self.posible_uncommon < self.posible_common: 
            print("일반재료가 더 많습니다. 생활가루로 변환합니다.")
            self.probeComm_Unccom = True
            self.comm_unccom = (self.posible_common - self.posible_uncommon) * 86 // 100 * 80 #일반재료가 더 많을때
            self.probeComToDust1 = (self.posible_common - self.posible_uncommon) * 86 // 100 #Probe
            self.dust = self.dust + self.comm_unccom
            self.probeDust1 = self.dust #Probe
            self.common = self.common - (self.posible_common - self.posible_uncommon) * 86
        else:
            print("고급재료가 더 많습니다. 생활가루로 변환합니다.")
            self.probeComm_Unccom = False
            self.comm_unccom = (self.posible_uncommon - self.posible_common ) * 45 // 50 * 80 #희귀재료가 더 많을때
            self.probeComToDust1_ = (self.posible_uncommon - self.posible_common ) * 45 // 50 #Probe
            self.dust = self.dust + self.comm_unccom
            self.probeDust1_ = self.dust #Probe
            self.uncommon = self.uncommon - (self.posible_uncommon - self.posible_common) * 45
        return

    def calc3(self, string, calci): # 생활 가루를 아비도스로 변환.
        if string != None:
            print(f"{string}")
        self.abidos += self.dust // 100 * 10
        if calci == True:
            self.probeDustToAbidos = self.abidos
        self.dust %= 100
        return
    
    def calc4(self): # 각 제작재료의 가능횟수를 순차적으로 1씩 삭감하여 가루로 변환 후 100개일시 아비도스로 변환.
        while self.posible_abidos <= min(self.posible_common, self.posible_uncommon): #아비도스 재료와 일치될때까지
            time.sleep(0.01)                            #0.01가 제일 안정적임
            if self.posible_abidos >= min(self.posible_common, self.posible_uncommon): #아비도스 재료가 더 많거나 같으면 중단 선언.
                self.calcIntegrity = False
            os.system("cls")
            print("아비도스로 변환 시뮬레이션중...")
            if self.calcIntegrity == True:
                self.common -= self.need_common         #need Common    86
                self.sequnce_common += self.need_common
                self.uncommon -= self.need_uncommon     #need Uncommon  45
                self.sequnce_uncommon += self.need_uncommon
            else:
                break
            if self.sequnce_common >= 100:              #Sequnce Common
                self.sequnce_common -= 100
                self.common += self.sequnce_common
                self.sequnce_common = 0
                self.dust += 80
                self.probeComToDust2 += 1
            if self.sequnce_uncommon >= 50:             #Sequnce Uncommon
                self.sequnce_uncommon -= 50
                self.uncommon += self.sequnce_uncommon
                self.sequnce_uncommon = 0
                self.dust += 80
                self.probeUncomToDust += 1
            if self.dust > 100:
                self.calc3(None, False)
                self.probeAbidos += 1
            self.showData()
            self.probeResultDust = self.dust
        return

    def result(self):
        self.probeDust2 = self.probeComToDust2 * 86
        self.probeDust3 = self.probeUncomToDust * 45
        #os.system("cls")
        print("최종 결과:")
        print(f"  아비도스 재료 : [{self.abidos}개]  >>  [{self.abidos//33}회분]")
        print(f"  T2 희귀 재료 : [{self.rare}개]")
        print(f"  고급 재료 : [{self.uncommon}개]  >>  [{self.uncommon//45}회분]")
        print(f"  일반 재료 : [{self.common}개]  >>  [{self.common//86}회분]")
        print(f"  생활가루 : [{self.probeResultDust}개]\n")
        print("기존 보유량:")
        print(f"  아비도스 재료 : [{self.origin_abidos}개]  >>  [{self.origin_abidos//33}회분]")
        print(f"  T2 희귀 재료 : [{self.origin_rare}개]")
        print(f"  고급 재료 : [{self.origin_uncommon}개]  >>  [{self.origin_uncommon//45}회분]")
        print(f"  일반 재료 : [{self.origin_common}개]  >>  [{self.origin_common//86}회분]")
        print(f"  생활가루 : [{self.origin_dust}개]\n")
        print(f"교환 과정:")
        print(f"  1. T2 희귀 재료를 모두 일반재료로 변환합니다. (생활가루로 변환하는게 아닙니다.)")
        if self.probeComm_Unccom == True:
            print(f"  2. 일반재료를 생활가루로 [{self.probeComToDust1}회] 교환합니다. (생활가루: {self.probeDust1}개)")
        if self.probeComm_Unccom == False:
            print(f"  2. 고급재료를 생활가루로 [{self.probeComToDust1_}회] 교환합니다. (생활가루: {self.probeDust1_}개)")
        print(f"  3. 교환된 생활가루를 모두 아비도스 재료로 교환합니다. (아비도스: {self.probeDustToAbidos}개)")
        print(f"  4. 일반재료를 생활가루로 [{self.probeComToDust2}회] 교환합니다. (생활가루: {self.probeDust2}개)")
        print(f"  5. 고급재료를 생활가루로 [{self.probeUncomToDust}회] 교환합니다. (생활가루: {self.probeDust3}개)")
        print(f"  6. 모든 생활가루를 아비도스 재료로 교환합니다. (아비도스: {self.probeAbidos*33}개)")





calc = AbidosCalc()
current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M")
file_name = f"saved_{current_date}.txt"
results_folder = "Results"
file_path = os.path.join(results_folder, file_name)

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
calc.calc3("모든 생활가루를 아비도스 재료로 변환합니다.", True)
calc.showData()
calc.timer(3, "다음 단계")

os.system("cls")
calc.calc4()

if not os.path.exists(results_folder):
    os.makedirs(results_folder)


print("아비도스 변환 시뮬레이션 완료.")
calc.timer(3, "정리 단계")
os.system("cls")
calc.result()
with open(file_path, 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f

    calc.result()

    sys.stdout = original_stdout
print(f"\n\n결과가 'Result\{file_name}'에 저장되었습니다.")
print("아무키를 입력하여 종료할 수 있습니다.")
os.system("pause>nul")