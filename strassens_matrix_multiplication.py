'''
-------------------------------
Strassens Matrix Multiplication
-------------------------------
Performs matrix multiplication in sub-cubic time, performing only 7 recursive calls 
rather than the 8 required by standard multiplication.

The function assumes 2 square matrices that have height/width that is a power of 2.
'''
def strassen_multiply(m1, m2):
    def split_matrix(m):
        n = len(m) / 2

        ma = map(lambda x : x[:n], m[:n])
        mb = map(lambda x : x[n:], m[:n])
        mc = map(lambda x : x[:n], m[n:])
        md = map(lambda x : x[n:], m[n:])

        return ma, mb, mc, md

    def add_rows(r):
        return map(sum, zip(r[0], r[1]))

    def add(m1, m2):
        return map(add_rows, zip(m1, m2))

    def negate_row(r):
        return map(lambda x : -x, r)

    def negate(m):
        return map(negate_row, m)

    def multiply(m1, m2):
        if len(m1) == 1:
            return [[m1[0][0] * m2[0][0]]]

        ma, mb, mc, md = split_matrix(m1)
        me, mf, mg, mh = split_matrix(m2)

        p1 = multiply(ma, add(mf, negate(mh)))
        p2 = multiply(add(ma, mb), mh)
        p3 = multiply(add(mc, md), me)
        p4 = multiply(md, add(mg, negate(me)))
        p5 = multiply(add(ma, md), add(me, mh))
        p6 = multiply(add(mb, negate(md)), add(mg, mh))
        p7 = multiply(add(ma, negate(mc)), add(me, mf))

        r1 = add(add(p5, p4), add(negate(p2), p6))
        r2 = add(p1, p2)
        r3 = add(p3, p4)
        r4 = add(add(p1, p5), negate(add(p3, p7)))

        ra = map(lambda t : t[0] + t[1], zip(r1, r2))
        rb = map(lambda t : t[0] + t[1], zip(r3, r4))
        
        return ra + rb
        
    return multiply(m1, m2)

         