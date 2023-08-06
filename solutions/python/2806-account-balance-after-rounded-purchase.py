class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        initial_balance = 100 
        rounded_amount = (purchaseAmount + 5) // 10 * 10 
        return initial_balance - rounded_amount 
                             
