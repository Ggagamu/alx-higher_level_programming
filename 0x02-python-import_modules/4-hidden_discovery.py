#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    folder = dir(hidden_4)
    length = len(folder)
    for u in range(0, length):
        if folder[u][0:2] != "__":
            print(folder[u])
