def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    def generate(p,l,r,paren = []):
        if l: generate(p+'(',l-1,r)
        if r>l: generate(p+')',l,r-1)
        if not r: paren+=p,
        return paren
    return generate('',n,n)

