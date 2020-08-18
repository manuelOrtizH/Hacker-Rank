#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/collections-counter/problem
import sys
from collections import Counter

def sell_shoes(size_price, shoes_size):
    if size_price[0] in shoes_size:
        shoes_size[size_price[0]] -= 1
    else:
        return False
    if shoes_size[size_price[0]] == 0:
        del shoes_size[size_price[0]]
    return True

def counterShoes(shoes, dict_count, clients):
    total_price = 0
    client_counter = 0
    for i in range(clients):
        if client_counter > clients:
            return total_price
        size_price = list(map(int, input().split()))
        if sell_shoes(size_price, dict_count):
            total_price+=size_price[1]
            client_counter+=1
    return total_price


def main():
    shoes = int(input())
    shoe_size = Counter(map(int, input().split()))
    clients = int(input())
    print(counterShoes(shoes, shoe_size, clients))
    

if __name__ == '__main__':
    main()

    
    
