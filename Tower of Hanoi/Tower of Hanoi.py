#This program is a recursive solution to the Tower of Hanoi problem. 
#The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
#The objective of the puzzle is to move the entire stack to another rod


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# 3 disks
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
