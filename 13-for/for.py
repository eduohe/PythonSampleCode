#!/usr/bin/python3

def main():
    arq = open('exemplo.txt')
    for linha in arq.readlines():
        print(linha, end = '')

if __name__ == "__main__" : main()