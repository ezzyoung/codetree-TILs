#include <iostream>
using namespace std;

int main() {
    cout << fixed;
    double ft = 9.2;
    double mile = 1.3;
    double ftanswer = ft * 30.48;
    double mileanswer = mile * 160934;

    cout.precision(1);
    cout << ft << "ft = "<<ftanswer<<"cm"<<"\n";
    cout << mile << "mi = "<<mileanswer<<"cm"<<"\n";    

    return 0;
}