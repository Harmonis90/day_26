with open("file1.txt", "r") as f1_data:
    f1_nums = [int(n.strip()) for n in f1_data.readlines()]

    with open("file2.txt", "r") as f2_data:
        f2_nums = [int(n.strip()) for n in f2_data.readlines()]

        result = [num for num in f1_nums if num in f2_nums]
        print(result)