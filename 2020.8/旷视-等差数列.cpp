#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    while(true) {
        int n, tmp;
        cin >> n;
        vector<int> array;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            array.push_back(tmp);
        }
        sort(array.begin(), array.end());
        int magicNums = 0;
        while (!array.empty() && array[magicNums] == 0)
            magicNums++;
        int i = magicNums + 1;
        bool vaild = true;
        while(i < array.size()) {
            if(array[i] == array[i-1]) {
                vaild = false;
                break;
            }
            if(array[i] - array[i - 1] > 1) {
                int need = array[i] - array[i - 1] - 1;
                if (magicNums >= need)
                    magicNums -= need;
                else
                {
                    vaild = false;
                    break;
                }
            }
            i++;
        }
        if (vaild)
            cout << "Valid"<<endl;
        else
            cout<<"Invalid"<<endl;
    }
    return 0;
}
