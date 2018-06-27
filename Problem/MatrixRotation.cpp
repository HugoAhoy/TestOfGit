#include <iostream>
#include <cstring>
using namespace std;

int matrix[101][101];

int main()
{
	int N, M, K, sum, res;
	bool flag;
	while (cin >> N >> M >> K)
	{
		res = N * K + 1;
		flag = false;
		memset(matrix, 0, sizeof(matrix));
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				cin >> matrix[i][j];
			}
		}
		
		for (int w = 1; w <= N; w++) {
			for (int h = 1; h <= M; h++) {
				for (int i = 1; i <= N - w + 1; i++) {
					for (int j = 1; j <= M - h + 1; j++) {
						sum = 0;
						for (int p = 0; p < w; p++) {
							for (int q = 0; q < h; q++) {
								sum += matrix[i + p][j + q];
							}
						}
						if (sum >= K) {
							flag = true;
							if (res > w * h) {
								res = w * h;
							}
						}
					}
				}
			}
		}
		
		if (flag) {
			cout << res << endl;
		}
		else {
			cout << -1 << endl;
		}
	}
	return 0;
}