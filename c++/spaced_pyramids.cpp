#include <iostream>
using namespace std;

int main() {
    int N = 8;

    for (int i = 1; i <= N; i++) {
        // cetak tinggi

        for (int j = 1; j<=N ;j++) {
            // cetak piramida kiri

            if (j > (N-i)){
                cout << "#";
            } else {
                cout << " ";
            }
        }

        cout << ("  ");
        // cetak spasi

        for (int j = 1; j <= i; j++) {
            //cetak piramida kanan

            cout << "#";
        }

        cout << endl;
    
    }
}
 
