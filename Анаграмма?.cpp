#include <iostream>
#include <algorithm>
#include <set>
#include <numeric>
#define ll long long
#define F first
#define S second

using namespace std;
const int N = 2e5 + 10;

string a, b;

int main() {
    cin >> a >> b;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    if (a == b)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
