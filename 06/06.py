if __name__ == "__main__":
    with open("06/input.txt") as file:
        signal = file.readline()
        bits = [*signal]
        for n in range(len(bits)):
            if n < 3:
                continue
            if len(set(bits[n-3:n+1])) == len(bits[n-3:n+1]):
                print('Packet begins at value {0}'.format(n+1))
                break
        for n in range(len(bits)):
            if n < 13:
                continue
            if len(set(bits[n-13:n+1])) == len(bits[n-13:n+1]):
                print('Message begins at value {0}'.format(n+1))
                break

