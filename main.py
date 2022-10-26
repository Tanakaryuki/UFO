import RPi.GPIO as GPIO
import time
import sys

def Move_Motor(Direction,Action):
    if(Direction == "VERTICAL"):    # 縦の場合
        Pin1 = MOTOR_VERTICAL_R
        Pin2 = MOTOR_VERTICAL_B 
    elif(Direction == "BESIDE"):    # 横の場合
        Pin1 = MOTOR_BESIDE_R
        Pin2 = MOTOR_BESIDE_B
    elif(Direction == "CRANE"):     # クレーンの場合
        Pin1 = MOTOR_CRANE_R
        Pin2 = MOTOR_CRANE_B
    elif(Direction == "SOLENOID"):
        Pin1 = SOLENOID

    if(Action == "PREVIOUS"):
        GPIO.output(Pin1,GPIO.HIGH)
        GPIO.output(Pin2,GPIO.LOW)
        print("ACT==PRE")
    elif(Action == "BACK"):
        GPIO.output(Pin1,GPIO.LOW)
        GPIO.output(Pin2,GPIO.HIGH)
    elif(Action == "BRAKE"):
        GPIO.output(Pin1,GPIO.HIGH)
        GPIO.output(Pin2,GPIO.HIGH)
    elif(Action == "CLOSE"):
        GPIO.output(Pin1,GPIO.HIGH)
    elif(Action == "OPEN"):
        GPIO.output(Pin1,GPIO.LOW)
    else:
        GPIO.output(Pin2,GPIO.LOW)
        GPIO.output(Pin1,GPIO.LOW)

BOTTOM_B = 1
BOTTOM_G = 24
BOTTOM_Y =25
LED_B = 4
LED_G = 5
LED_Y = 6
SWITCH_1 = 7        # クレーンの上限制限
# SWITCH_2 = 8      # クレーンの下降制限
SWITCH_3 = 9        # 縦移動の最大制限
SWITCH_4 = 10       # 縦移動の最低制限
SWITCH_5 = 11       # 横移動の最大制限(奥)
SWITCH_6 = 12       # 横移動の最大制限(手前)
SWITCH_7 = 13       # 横移動の最小制限(奥)
SWITCH_8 = 14       # 横移動の最小制限(手前)
MOTOR_CRANE_R = 15
MOTOR_CRANE_B = 16
MOTOR_VERTICAL_R = 17
MOTOR_VERTICAL_B = 18
MOTOR_BESIDE_R = 19
MOTOR_BESIDE_B = 20
SOLENOID = 21
# SOLENOID = 22(GND)
SWITCH_KILL = 23

MODE = 0
# 0=完全停止
# 1=準備完了 横移動待機
# 2=横移動完了 縦移動待機
# 3=縦移動完了 降下停止待機
# 4=降下完了 初期位置に移動

GPIO.setmode(GPIO.BCM)  #GPIO番号で制御宣言

GPIO.setup(BOTTOM_B,GPIO.IN)
GPIO.setup(BOTTOM_G,GPIO.IN)
GPIO.setup(BOTTOM_Y,GPIO.IN)
GPIO.setup(LED_B,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_Y,GPIO.OUT)
GPIO.setup(SWITCH_1,GPIO.IN)
# GPIO.setup(SWITCH_2,GPIO.IN)
GPIO.setup(SWITCH_3,GPIO.IN)
GPIO.setup(SWITCH_4,GPIO.IN)
GPIO.setup(SWITCH_5,GPIO.IN)
GPIO.setup(SWITCH_6,GPIO.IN)
GPIO.setup(SWITCH_7,GPIO.IN)
GPIO.setup(SWITCH_8,GPIO.IN)
GPIO.setup(MOTOR_CRANE_R,GPIO.OUT)
GPIO.setup(MOTOR_CRANE_B,GPIO.OUT)
GPIO.setup(MOTOR_VERTICAL_R,GPIO.OUT)
GPIO.setup(MOTOR_VERTICAL_B,GPIO.OUT)
GPIO.setup(MOTOR_BESIDE_R,GPIO.OUT)
GPIO.setup(MOTOR_BESIDE_B,GPIO.OUT)
GPIO.setup(SOLENOID,GPIO.OUT)
GPIO.setup(SWITCH_KILL,GPIO.IN)

if(GPIO.input(SWITCH_KILL) == 1):   #MODEを初期化
    MODE = 0
    print("MODE={}".format(MODE))
else:
    MODE = 1
    print("MODE={}".format(MODE))
print("初期化完了")

try:
    while True:
        if(GPIO.input(BOTTOM_B) == GPIO.HIGH):
            GPIO.output(LED_B,GPIO.HIGH)
            Move_Motor("CRANE","PREVIOUS")
        else:
            GPIO.output(LED_B,GPIO.LOW)
            Move_Motor("CRANE","BRAKE")
        
        if(GPIO.input(BOTTOM_G) == GPIO.HIGH):
            GPIO.output(LED_G,GPIO.HIGH)
            Move_Motor("CRANE","BACK")
        else:
            GPIO.output(LED_G,GPIO.LOW)
            Move_Motor("CRANE","BRAKE")
        
        if(GPIO.input(BOTTOM_Y) == GPIO.HIGH):
            GPIO.output(LED_Y,GPIO.HIGH)
        else:
            GPIO.output(LED_Y,GPIO.LOW)
        
        if(GPIO.input(SWITCH_1) == GPIO.HIGH):
            Move_Motor("SOLENOID","CLOSE")
        else:
            Move_Motor("SOLENOID","OPEN")
        
        if(GPIO.input(SWITCH_3) == GPIO.HIGH):
            Move_Motor("VERTICAL","PREVIOUS")
        else:
            Move_Motor("VERTICAL","BRAKE")
        
        if(GPIO.input(SWITCH_4) == GPIO.HIGH):
            Move_Motor("VERTICAL","BACK")
        else:
            Move_Motor("VERTICAL","BRAKE")
        
        if(GPIO.input(SWITCH_5) == GPIO.HIGH):
            Move_Motor("BESIDE","PREVIOUS")
        else:
            Move_Motor("BESIDE","BRAKE")
        
        if(GPIO.input(SWITCH_6) == GPIO.HIGH):
            Move_Motor("BESIDE","BACK")
        else:
            Move_Motor("BESIDE","BRAKE")
        
        if(GPIO.input(SWITCH_7) == GPIO.HIGH):
            print("7")
        
        if(GPIO.input(SWITCH_8) == GPIO.HIGH):
            print("8")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()