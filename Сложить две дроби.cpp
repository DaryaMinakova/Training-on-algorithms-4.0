#include <iostream>
#include <algorithm>
#include <set>
#include <numeric>
#define ll long long
#define F first
#define S second

using namespace std;
const int N = 2e5 + 10;

int a, b, c, d;

int main() {
    cin >> a >> b >> c >> d;
    int denominator = b * d;
    int numerator = a * d + c * b;
    int gcd_num = gcd(numerator,denominator);
    denominator /= gcd_num;
    numerator /= gcd_num;
    cout << numerator << " " << denominator;
    return 0;
}
