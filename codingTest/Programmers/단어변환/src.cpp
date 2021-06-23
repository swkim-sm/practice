#include <string>
#include <vector>
#include <queue>

#include <iostream>
using namespace std;
queue<int> q;
int result[50];
bool visited[50];
int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int len = begin.length();
    for(int i = 0; i < words.size(); i++) {
        int cnt = 0;
        for(int j = 0; j<len; j++){
            if(begin[j] != words[i][j]) cnt++;
            if(cnt == 2) break;
        }
        if(cnt == 1) {
            q.push(i); visited[i] = true;
            result[i] = 1;
        }
    }
    while(!q.empty()){
        int now_idx = q.front();
        string now = words[now_idx];
        q.pop();
        //종료조건
        for(int i = 0; i < len; i++){
            if(target[i] != now[i]) break;
            if(i == len-1) return result[now_idx];
        }
        for(int i = 0; i < words.size(); i++) {
            int cnt = 0;
            if(!visited[i]){
                for(int j = 0; j < len; j++){
                    if(now[j] != words[i][j]) cnt++;
                    if(cnt == 2) break;
                }
                if(cnt == 1) {
                    q.push(i);
                    visited[i] = true;
                    result[i] = result[now_idx]+1;
                }
            }
            else continue;
        }
    }
    return answer;
}
