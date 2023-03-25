# python3
# Nikita Ščipanovs 221RDB061

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    def sift_down(i):
        nonlocal swaps
        min_index = i
        l = 2*i + 1
        if l < n and data[l] < data[min_index]:
            min_index = l
        r = 2*i + 2
        if r < n and data[r] < data[min_index]:
            min_index = r
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)
            
    for i in range(n//2, -1, -1):
        sift_down(i)  


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_method = input().strip()
    
    if (input_method == 'I'):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    else:
        file_name = input()
        f = open("test/" + file_name,'r')
        n = int(f.readline())
        variables = f.readline()
        data = list(map(int, variables.split()))
         



    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
