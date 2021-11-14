
if __name__ == '__main__':
    while(True):
        try:
            n = int(input())
            j = 1;
            while True:
                if j % n or j < n:
                    j = j * 10 + 1
                    continue
                print(len(str(j)))
                break;
        except EOFError:
            break;
