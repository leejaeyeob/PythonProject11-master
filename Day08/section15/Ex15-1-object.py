'''
클래스
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계
    객체화(인스턴스화) - 메모리에 올리는 것

객체(object)
    현실 세계에 존재하는 물리적, 추상적 식별할 수 있는 모든 것
    예) 컴퓨터, 학생, 주문, 배송

객체 구성
    초기화용 - 생성자
    속성 값 - 변수
    기능 - 메소드(함수)
'''
# computer 클래스 정의
class Computer:

    # 첫번쨰 매개 변수가 self 이므로 인스턴스 메소드이다.
    # self를 제외한 나머지 매개변수에 실제로 상용될 데이터가 전달된다.
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer() # Computer 객체화(객체 생성)
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print()

desktop.cpu = 'i9'
desktop.hardware_info()
print()

macbook = Computer()
macbook.set_spec('M2', '16GB', 'M2', '512GB')
macbook.hardware_info()