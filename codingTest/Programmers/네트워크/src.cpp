#include <string>
#include <vector>
#include <iostream>
using namespace std;
bool visited[200][200];
void dfs(int x, int y, vector<vector<int>> &computers, int &n){
    visited[x][y] = true;
    visited[y][x] = true;
    
    for(int j = 0; j<n;j++){
        if(!visited[y][j] && computers[y][j] == 1){
            dfs(y, j, computers, n);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(computers[i][j] == 1 && !visited[i][j]){
                cout << i << "E" << j ;
                dfs(i, j, computers, n);
                answer++;
            }
        }
    }
    
    return answer;
}
