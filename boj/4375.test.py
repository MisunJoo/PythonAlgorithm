

if __name__ == '__main__':
    while True:
            try:
                n = int()
                i = 1
                while True:
                    if i < n or i % n:
                        i = i * 10 + 1
                        continue
                    print(len(str(i)))
                    break
            except EOFError:
                break