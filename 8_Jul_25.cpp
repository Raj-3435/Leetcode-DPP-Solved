//  Problem 1751: Maximum Number of Events That Can Be Attended II


class Solution {
    public:
        static bool cmp(const vector<int>& a, const vector<int>& b){
            return a[1]<b[1];
        }
        
        int maxValue(vector<vector<int>>& events, int k) {
            int n = events.size();
            sort(events.begin(),events.end(),cmp);
    
            vector<int> endTimes(n);
            for (int i=0;i<n;++i)
                endTimes[i] = events[i][1];
    
            vector<vector<int>> dp(n+1,vector<int>(k+1,0));
    
            for (int i=1;i<=n;++i){
                int start = events[i-1][0];
                int end = events[i-1][1];
                int val = events[i-1][2];
    
                int l=0,r=i-1;
                int prev = 0;
                while(l<r){
                    int mid = (l+r+1)/2;
                    if (endTimes[mid-1]<start)
                        l = mid;
                    else
                        r=mid-1;
                }
                if (l>0 && endTimes[l-1]<start)
                    prev = l;
                else if (l==0 && endTimes[0] < start)
                    prev=1;
    
                for (int j=1;j<=k;++j){
                    dp[i][j] = max(dp[i-1][j],dp[prev][j-1]+val);
                }
            }
    
            return dp[n][k];
        }
    };
