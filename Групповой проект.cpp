#include <iostream>
#include <algorithm>
#include <set>
#include <numeric>
#define ll long long
#define F first
#define S second

using namespace std;
const int N = 2e5 + 10;

ll t, n, a, b;

int main() {
    cin >> t;
    while (t--) {
        cin >> n >> a >> b;
        ll k = n / b;
        n -= (k * b);
        n -= (n / a * a);
        if (n >= a or n == 0)
            cout << "YES\n";
        else if (a == b)
            cout << "NO\n";
        else if (a - n <= k * (b - a))
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}
