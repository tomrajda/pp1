# 19. Write a program, in which, import the module stack.py. 
# Then do the following:
# a.	Display stack
# b.	Put the number 2 on the stack
# c.	Put the number 14 on the stack
# d.	Put the number 9 on the stack
# e.	Display stack
# f.	Get element from stack
# g.	Display stack
# h.	Put the number 31 on the stack
# i.	Put the number 6 on the stack
# j.	Display stack
# k.	Get two elements from stack
# l.	Display stack

import stack

# a
stack.display()
# b
stack.push(2)
# c
stack.push(14)
# d
stack.push(9)
# e
stack.display()
# f
stack.pop()
# g
stack.display()
# h
stack.push(31)
# i
stack.push(6)
# j
stack.display()
# k
for _ in range(2):
    stack.pop()
# l
stack.display()