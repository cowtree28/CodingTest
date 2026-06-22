using namespace std;

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int distance = arr[1] - arr[0];
        bool is_arithmetic = true;
        for(int i = 1;i < arr.size()-1;i++) {
            if (arr[i] + distance != arr[i+1]) {
                is_arithmetic = false;
                break;
            }
        }
        return is_arithmetic;
    }
};