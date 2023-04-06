def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1)*num

def main():
    nums=[0,2,4,6,8,10,12,14]
    for num in nums:
        print(str(num) + "! = " + str(factorial(num)))

if __name__ == "__main__":
    main()
