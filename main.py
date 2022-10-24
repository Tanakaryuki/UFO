import RPi.GPIO as GPIO

BOTTOM_B = 1
BOTTOM_G = 2
BOTTOM_Y = 3
LED_B = 4
LED_G = 5
LED_Y = 6
SWITCH_1 = 7        #クレーンの上限制限
SWITCH_2 = 8        #クレーンの下降制限
SWITCH_3 = 9        #縦移動の最大制限
SWITCH_4 = 10       #縦移動の最低制限
SWITCH_5 = 11       #横移動の最大制限(奥)
SWITCH_6 = 12       #横移動の最大制限(手前)
SWITCH_7 = 13       #横移動の最小制限(奥)
SWITCH_8 = 14       #横移動の最小制限(手前)
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

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)  #GPIO番号で制御宣言

GPIO.setup(BOTTOM_B,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BOTTOM_G,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BOTTOM_Y,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_B,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_Y,GPIO.OUT)
GPIO.setup(SWITCH_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MOTOR_CRANE_R,GPIO.OUT)
GPIO.setup(MOTOR_CRANE_B,GPIO.OUT)
GPIO.setup(MOTOR_VERTICAL_R,GPIO.OUT)
GPIO.setup(MOTOR_VERTICAL_B,GPIO.OUT)
GPIO.setup(MOTOR_BESIDE_R,GPIO.OUT)
GPIO.setup(MOTOR_BESIDE_B,GPIO.OUT)
GPIO.setup(SOLENOID,GPIO.OUT)
GPIO.setup(SWITCH_KILL,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

if(GPIO.input(SWITCH_KILL) == 1):   #MODEを初期化
    MODE = 0
else:
    MODE = 1

try:
    while True:
        print("hello")

except KeyboardInterrupt:
    GPIO.cleanup()