# หาพื้นที่สีเหลี่ยม และสามเหลี่ยม โดยรับกว้าง ยาว/ฐาน สูง ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ
# feature การทำงานอะไรบ้าง
# 1. รับค่า กว้างยาว 2. รับค่า ฐาน สูง 
# 3. คำนวณพท.สี่เหลี่ยม และแสดงพท.สี่เหลี่ยม 4. คำนวณพท.สามเหลี่ยม และแสดงพท.สามเหลี่ยม
def inputWitdhLong( ) :
    witd = float( input('ป้อนกว้าง '))
    long = float( input('ป้อนยาว '))
    return witd, long

def inputBaseHigh( ) :
    base = float( input('ป้อนฐาน '))
    high = float( input('ป้อนสูง '))
    return base, high

def calAndShowAreaSquare( witd, long ) :
    area = witd * long
    print(f'สี่เหลี่ยมกว้าง {witd} ยาว {long} มีพื้นที่ {area}')

def calAndShowAreaTrianble( base, high ) :
    area = base * high / 2
    print(f'สี่เหลี่ยมกว้าง {base} ยาว {high} มีพื้นที่ {area}')    

witd, long = inputWitdhLong()
calAndShowAreaSquare(witd, long)
print('--------------------------------------')
base, high = inputBaseHigh( )
calAndShowAreaTrianble(base, high)