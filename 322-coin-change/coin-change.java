class Solution {
    public int coinChange(int[] coins, int amount) {
        int INF = 1000000000;
        int n = coins.length;
        int[] dp = new int[amount+1];
        Arrays.fill(dp,INF);
        dp[0] = 0;
        for(int i=1;i<=amount;i++){
            for (int j=0;j<n;j++){
                if (i-coins[j]>=0){
                    dp[i] = Math.min(dp[i],dp[i-coins[j]]+1);
                }
            }
        }
        if (dp[amount] == INF) return -1;
        return dp[amount];

    }
}