#include <iostream>
using namespace std;

int main() {
    cout << fixed;

    int a = 13;
    double m = 0.165000;
    double r = a*m;

    cout.precision(6);
    cout << a << " * "<<m<<" = "<<r;

    return 0;
}