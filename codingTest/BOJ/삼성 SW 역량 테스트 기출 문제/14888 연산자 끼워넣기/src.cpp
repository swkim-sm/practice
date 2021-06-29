#include <iostream>
#include <limits>
using namespace std;
int N;
int arr[11];
int op[4];
int max_result = numeric_limits<int>::min();
int min_result = numeric_limits<int>::max();

void dfs(int tmp, int op[4], int idx, int cur_op) {
	if (cur_op == 0) tmp += arr[idx];
	else if (cur_op == 1) tmp -= arr[idx];
	else if (cur_op == 2) tmp *= arr[idx];
	else tmp /= arr[idx];

	if (idx == N - 1) {
		if (tmp > max_result) max_result = tmp;
		if (tmp < min_result) min_result = tmp;
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (op[i]) {
			op[i]--;
			dfs(tmp, op, idx + 1, i);
			op[i]++;
		}
	}
}

int main(void) {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	cin >> op[0] >> op[1] >> op[2] >> op[3];
	for (int i = 0; i < 4; i++) {
		if (op[i]) {
			int tmp = arr[0];
			op[i]--;
			dfs(tmp, op, 1, i);
			op[i]++;
		}
	}
	cout << max_result << endl << min_result << endl;
}
