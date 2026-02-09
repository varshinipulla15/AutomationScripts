def sum_list(numbers):
    return sum(numbers)

def square(number):
    return number * number

def factorial(number):
    if number < 0:
        raise ValueError('Factorials for -ve number does not exist')
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

if __name__ == "__main__":
    nums = [2,6,8]
    print (f"Numbers are : {nums}")

    print (f"Sum : {sum(nums)}")

    for i in nums:
        print (f"Square of number {i} : {square(i)}")
    
    for j in nums:
        print (f"Factorial of number {j} : {factorial(j)}")