def index_convert(index, partition):
    if index >= 1 and index <= 5:
        if index >= partition:
            index -= 1
        if index > 0:
            index -= 1
        return index
    else:
        return 0

if __name__ == "__main__":
    x = index_convert(2,3)
    for partition in range(1,6): # 1 to 5
        for index in range(1,6):
            i_1 = index_convert(index,partition)
            print(f"Partition : {partition}, Chosen Card: {index}, Calculatd Index: {i_1}, Place Value {i_1 + 1}")
        print()