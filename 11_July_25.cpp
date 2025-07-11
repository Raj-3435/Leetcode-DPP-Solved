// Problem 2402. Meeting Rooms III
//https://leetcode.com/problems/meeting-rooms-iii/editorial

class Solution{
public:
    int mostBooked(int n, vector<vector<int>>& meetings){
        sort(meetings.begin(), meetings.end());

        priority_queue<int, vector<int>, greater<int>> free;
        for (int i=0;i<n;++i) free.push(i);

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> busy;
        vector<int> count(n);
        for (const auto& m:meetings){
            int start = m[0], end = m[1];

            while(!busy.empty() && busy.top().first <= start){
                free.push(busy.top().second);
                busy.pop();
            }

            int room;
            long long actualStart;

            if(!free.empty()){
                room = free.top();
                free.pop();
                actualStart = start;
            }else{
                auto[availableTime, freeRoom] = busy.top(); busy.pop();
                room = freeRoom;
                actualStart = availableTime;
            }

            long long actualEnd = actualStart + (end-start);
            busy.push({actualEnd, room});
            count[room]++;
        }
            int maxRoom = 0;
            for (int i =1;i<n;i++){
                if (count[i]>count[maxRoom]) maxRoom = i;
     }
        return maxRoom;
}
};