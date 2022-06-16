## Submarine Position
"""
# You are in a submarine, which is navigated via a series of input steps which change the position of the submarine. Your task is to create a solution which provides the final horizontal and depth positions.

# For example:

# ```
# forward 5 down 5 forward 8 up 3 down 8 forward 2
# ```

# Your horizontal position and depth both start at `0`

# After following these instructions, you would have a horizontal position of `15` and a depth of `10`.
"""
#f1 -> 5 f2 ->8 f3 -> 2 
#d1  -> d2 -> 8
#u -> 2 


# def submarine(f,d,u):
#     movement = [0,0]
#     res1, res2, res3 = 0, 0, 0
#     # f = list(map(int, input()).strip().split())
#     # d = list(map(int, input()).strip().split())
#     # u = list(map(int, input()).strip().split())
    
#     if f:
#         res1 = sum(f)
#     elif d:
#         res2 = sum(d)
#     elif u:
#         res3 = sum(u)
    
#     horizontal_movement = res1
#     depth_movement = res2 + res3
    
#     movement[0] += horizontal_movement
#     movement[1] += depth_movement
    
#     return movement


# f = list(map(int, input("\nEnter forward Movements: ").strip().split()))
# d = list(map(int, input("\nEnter downward movements: ").strip().split()))
# u = list(map(int, input("\nEnter upward movements ").strip().split()))

# print(submarine(f,d,u))

def subbmarine(f,d,u):
    movement = [0,0]
    keys = {'forward':5, 'upward': 2, 'downward':8}
    res1, res2, res3 = 0,0,0
    match keys:
        case 'forward':
            res1= sum('forward')
        case 'downward':
            res2 = sum('dowmward')
        case 'upward':
            res3 = sum('upward')
        
    keys['forward'] = res1
    keys['downward'] = res2
    keys['upward'] = res3
    horizontal_movement = res1
    depth_movement = res2 + res3
    
    movement[0]+=horizontal_movement
    movement[1]+= depth_movement
    
    return movement

    
f = list(map(str, input("\nEnter forward Movements: ").strip().split()))
d = list(map(str, input("\nEnter downward movements: ").strip().split()))
u = list(map(str, input("\nEnter upward movements ").strip().split()))

print(subbmarine(f,d,u))