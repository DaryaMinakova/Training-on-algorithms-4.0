#include <iostream>
#include <algorithm>
#include <set>
#include <numeric>
#define ll long long
#define F first
#define S second

using namespace std;
const int N = 2e5 + 10;

int n, a[N], sum_all, sum_prev;


int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum_all += a[i];
    }
    for (int i = 0; i < n; i++) {
        sum_prev += a[i];
        sum_all -= a[i];
        cout << (i + 1) * a[i] - sum_prev + sum_all - (n - i - 1) * a[i] << " ";
    }
    return 0;
}
