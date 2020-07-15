### exmple 1 ###
## variables ##
numStr, i, num_len = "",0,0

## main ##
if __name__ == "__main__":
    numStr = input("숫자를 여러 개 입력하시오. ")
    num_len = len(numStr)
    
    for i in range(0, num_len):
        for i in range(0, int(numStr[i])):
            print('\u2665', end='')
        print()
