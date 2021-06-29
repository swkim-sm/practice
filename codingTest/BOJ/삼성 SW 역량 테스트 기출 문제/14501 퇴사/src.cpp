#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int arr[15][2];
int answer;
void getNext(int day, int &sum) { 
	
	bool stop = true;
	for (int i = day; i < N; i++) {
		if (i + arr[i][0] <= N) {
			sum += arr[i][1];
			getNext(i + arr[i][0], sum);
			sum -= arr[i][1];
			stop = false;
		}
	}
	if (stop) {
		if (answer < sum) answer = sum;
		return;
	}
}
int main(void) {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i][0] >> arr[i][1];
	}
	for (int i = 0; i < N; i++) {
		if (i + arr[i][0] <= N) {
			int sum = arr[i][1];
			getNext(i + arr[i][0], sum);
		}
	}
	cout << answer << endl;
}
