print('A','B', 10,20)
print('A','B', 10,20,sep="/")
print(2020,7,4,sep="/")
print("우리 취업합니다", end="\n")

# path
print("d:\\A\\B\\C")

# 문자열 구분
print("이름 : 이시형")
print("전화번호 : 010-1234-1234")
print("이름" "이시형" "28")
print("이름","이시형","28")
print("이름" ,"이시형", "28", sep=" ")

# example
print("\t\t" + "#"*4, "회비 내역", "#"*4)
print("="*45)
print("이름\t나이\t전화번호\t회비")
print("="*45)

print("%s\t%d\t%s\t%s" % ("김예쁜", 25, "010-8888-9999", format(20000, ',')))
print("{0:s}\t{1:d}\t{2:s}\t{3:s}".format("김잘남", 25, "010-8338-1111", format(50000,',')))
num = "01077779999"
print("{0:s}\t{1:d}\t{2:s}\t{3:s}" .format("이이상", 35, num[:3] + "-" + num[3:7] + "-" + num[7:], format(30000, ',')))
print("="*45)
print("\t\t\t총합계\t"+ "%s" % (format(100000,',')))

# .format
print('{:10}{:10}{:10}'.format("name", "age", "address"))
print('{:<10}{:<10}{:<10}'.format("name", "age", "address"))
print('{:>10}{:>10}{:>10}'.format("name", "age", "address"))
print('{:^10}{:^10}{:^10}'.format("name", "age", "address"))
print('{:-^10}{:-^10}{:-^10}'.format("name", "age", "address"))

## 화폐단위 1000단위 컴머
print('{:,}{:,}'.format(10000,10000))

# IP address 192.168.108.11
num = "192.168.108.11"
print(num[12:15])
print(bin(int(num[:3])),bin(int(num[4:7])),bin(int(num[8:11])),bin(int(num[12:15])))
print('{:b}.{:b}.{:b}.{:b}'.format(192,168,108,11))

# 글자 반대
print('{4} {5} {0} {1} {2} {3}'.format('The','famine','was','severe','in','Samaria'))