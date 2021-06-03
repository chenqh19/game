第一回合：自己计算牌的价值并下注

其它回合：认为对手在计算牌的价值，自己模拟：随机很多副牌，查看其中哪些是不会对手肯定不会有的操作，去掉它们。然后在剩下的可能的样本中查看自己赢的概率。


Two Nash equilibriums:

1. When we are almost sure we will win, we should let the opposite lost more. Suppose the opposite has spent $S$, we should raise to $S'$, and we have probability $p$ to win. No matter whether the opposite person fold or call, he will lose the same amount of money: 
$$
-S = (1-p)S'+p(-S')\ \Rightarrow\ S'=\frac{S}{2p-1}
$$

2. When we think we may lose, we should decide whether to fold or to call. Suppose we have spent $S$ and the opposite has spent $S'$, we will choose the one expected to lose less:
$$
\min\big{-S, \big(pS'-(1-P)S'\big)\big}
$$