import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm/')
from pythonds.basic.stack.myStack import Stack

# =============================================================================
#                                   10 -> 2
# =============================================================================
# =============================================================================
# def decToBinary(decnum):
#     st = Stack()    
#     while decnum > 0:
#         bin = decnum % 2
#         st.push(bin)
#         decnum = decnum // 2
#     binaryStr = ''
#     while not st.isEmpty():
#         binaryStr += str(st.pop())
#     return binaryStr
# 
# print(decToBinary(233))
# =============================================================================

# =============================================================================
#                                10 -> any(below 16)
# =============================================================================

def decToany(decnum, base):
    digtal = '0123456789ABCDEF'
    st = Stack()
    while decnum > 0:
        res = decnum % base
        st.push(res)
        decnum = decnum // base
    baseStr = ''
    while not st.isEmpty():
        baseStr += digtal[st.pop()]
    return baseStr

print(decToany(233, 2))
print(decToany(233, 16))
print(decToany(25, 16))
print(decToany(25, 8))
    
    
    
    
    
    
    
    
    
    