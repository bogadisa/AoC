filename = "disk.txt"  

def find_dic_size(directory, paths=[]):
    s = [0]
    if any(isinstance(directory[key], dict) for key in directory):
        s.append([])
    for i, key in enumerate(directory):
        if isinstance(directory[key], dict):
            output = find_dic_size(directory[key])
            if len(output) == 2:
                s0, s1 = output
                s[0] += s0
                s[1].append(s0)
                s[1].append(s1)
            else:
                s[0] += output[0]
                s[1].append(output[0])
        else:
            s[0] += directory[key]
    return s

def flatten(nested_list):
    new_list = []
    for item in nested_list:
        if not(isinstance(item, list)):
            new_list.append(item)
        else:
            new_list.extend(flatten(item))
    return new_list

with open(filename, "r") as f:
    f.readline()
    lines = f.readlines()
    current_path = ""
    directories = {}
    current_directory = directories
    for line in lines:
        parts = line.strip().split(" ")
        if "$ cd" in line:
            if ".." in line:
                new_directory = directories
                for path in current_path.split("/")[1:-1]:
                    
                    new_directory = new_directory[path]
                current_directory = new_directory
                current_path = "/".join(current_path.split("/")[:-1])

            else:
                current_path += "/" + parts[-1]
                current_directory = current_directory[parts[-1]]
            

        elif not("$" in parts):
            if current_path == "":
                if "dir" in parts:
                    directories[parts[-1]] = {}
                else:
                    directories[parts[-1]] = int(parts[0])
            else:
                if "dir" in parts:
                    current_directory[parts[-1]] = {}
                else:
                    current_directory[parts[-1]] = int(parts[0])
                    
    s_tot = []
    for key in directories:
        if isinstance(directories[key], dict):
            s_partial = find_dic_size(directories[key])
        else:
            s_partial = directories[key]
        s_tot.append(s_partial)
    dic_sizes = s_tot.copy()
    while any(isinstance(item, list) for item in dic_sizes):
        dic_sizes = flatten(dic_sizes)

    s1 = 0
    for dic_size in dic_sizes:
        if dic_size < 100000:
            s1 += dic_size

    print("Task 1:", s1)
    
    tot_space_used = 0
    for dic_size in s_tot:
        tot_space_used += dic_size[0]

    total_storage = 70000000
    needed_storage = 30000000
    free_space = total_storage - tot_space_used
    space_to_free = needed_storage - free_space
    smallest_dic = max(dic_sizes)
    for dic_size in dic_sizes:
        if dic_size < smallest_dic:
            if dic_size > space_to_free:
                smallest_dic = dic_size

    print("Task 2:", smallest_dic)