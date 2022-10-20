import time
import os

print("정말 작동에 동의하십니까?? \n Enter버튼을 눌러주세요.\n")
m=input("입력하시는 파일은 시간이 경과 후 자동으로 삭제되는 프로그램입니다. \n ")
mm=input("모든 책임은 지금까지 프로그램을 끄지 않은 여러분들에게 있습니다. \n")
mmm=input("컴퓨터의 중요파일의 이름은 쓰지 마세요. \n")
mmmm=input('\033[91m' +"이름이 같은 파일은 전부 삭제됩니다. \n")
mi=input("다시 한번 말하는데 여러분 책임입니다..\n")

nbc = input('\033[0m'+ "파일이름(확장자 포함 ex: abc.txt): ")
inp = int(input("초입력: "))
si=input("시작버튼\n Enter버튼을 눌러주세요")

print("파일 찾는중..")
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
filepath = findfile(nbc, "/")
print('\033[0m'+"파일 탐색완료 \n",filepath)
print('\033[94m'+"타이머 시작.: ",filepath)
print('\033[92m'+".\n")
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='\n')
        time.sleep(1)
        num_of_secs -= 1     
    print('\033[91m'+"파일 삭제됨.",filepath)
    print()
    os.remove(filepath)
countdown(inp)
os.system('pause')
