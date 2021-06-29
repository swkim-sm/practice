#include <iostream>
#include <queue>
using namespace std;
int N, M;
int map[8][8];
int temp[8][8];
int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };
int answer = 0;

void copyMap(int (*from)[8], int (*to)[8]) {
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			to[n][m] = from[n][m];
		}
	}
}
void spreadVirus() {
	int result[8][8];
	copyMap(temp, result);
	queue<pair<int, int>> q;
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			if (result[n][m] == 2) {
				q.push({ n, m });
			}
		}
	}
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
				if (result[nx][ny] == 0) {
					result[nx][ny] = 2;
					q.push({ nx, ny });
				}
			}
		}
	}
	int noVirus = 0;
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			if (result[n][m] == 0) noVirus++;
		}
	}
	if (noVirus > answer) answer = noVirus;
}
void buildWall(int cnt) {
	if (cnt == 3) {
		spreadVirus();
		return;
	}
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			if (temp[n][m] == 0) {
				temp[n][m] = 1;
				buildWall(cnt+1);
				temp[n][m] = 0;
			}
		}
	}
}
int main(void) {
	scanf("%d %d", &N, &M);
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			scanf("%d", &map[n][m]);
		}
	}
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			if (map[n][m] == 0) {
				copyMap(map, temp);
				temp[n][m] = 1;
				buildWall(1);
				temp[n][m] = 0;
			}
		}
	}
	printf("%d\n", answer);
}
