def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here

    #keep track of cummilative account

    total = 1.0
    arr = []

    for i in range(len(returns)):
        wt = total * (1+returns[i])
        rt = wt - 1
        arr.append(rt)
        total = wt
    
    return arr