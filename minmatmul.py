# You need to calculate the product of N matrices A1A2 . . . An
# determine the order in which to perform the multiplication to be able to do it with the minimum number of operations.
# input: list of tuples, each tuple contains the number of rows and columns of a matrix S
# output: integer, minimum number of operations and list of indexes of matrices in the order of multiplication
# constrainst: we have atleast 3 elemetns as input

# solution: create two axiulary cost  for amortization that store two previous costs (C1,C2)
# appraoch Greedy and DP
# A B C => C0 = c{A}, C1 = c{AB}  => c{ABC} = min(C0+c{BC} + C{A(BC)}, C1 + c {(AB)C})
# each cost is calculated as follow: c{AB} = S[0][0] *S[0][1]*S[1][1]


def minmatmul(S):
    C0, C1 = 0, 0
    Ct = 0
    order = [(0,1)]
    for i in range(len(S)):
        if i<2: # first visit
            C1 = S[0][0] *S[0][1]*S[1][1]
            Ct = C1
            continue
        # compute cost
        C1tmp = C1
        C1 = min(C0 + S[i-1][0]*S[i-1][1]*S[i][1] + S[0][0]*S[i-1][0]*S[i][1], C1 + S[0][0]*S[i-1][1]*S[i][1])
        if C1 == C0 + S[i-1][0]*S[i-1][1]*S[i][1]+ S[0][0]*S[i-1][0]*S[i][1]:
            # first the BC and then A
            Ct = Ct - C1tmp + C0 + C1
            tmp = order[-1]
            order[-1] = (i,i-1)
            order.append(tmp)
        else:
            # first AB then C
            Ct += C1
            order.append((i,i-1))
        C0 = C1tmp
    return order, Ct

if __name__ == "__main__":
    S = [(100,5),(5,200), (200,200), (200, 2)]
    print(minmatmul(S))