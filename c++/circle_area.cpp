#include <bits/stdc++.h>

using namespace std;

int main() {
  double A, n, R;

  n = 3.14159; 
  cout << "Enter radius";
  cin >> R;

  A = n*(R*R);

  cout << fixed << setprecision(3) << "Area = " << A << endl;

  return 0;
}
