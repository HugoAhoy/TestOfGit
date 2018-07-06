#include<iostream>
#include<string>
using namespace std;

class numWithCARRY{
    private:
    int carry;
    string num;
    public:
    numWithCARRY(string a, int k);
    ~numWithCARRY(){};
    void show() {
        cout << num << endl;
    }
    friend numWithCARRY change(const numWithCARRY &obj, int toCarry);
};

numWithCARRY::numWithCARRY(string a, int k):carry(k) {
    num = a;
}

numWithCARRY change(const numWithCARRY &obj, int toCarry) {
    string temp = obj.num;
    for(int i = 0; i < obj.num.length(); i++) {

    }
    return numWithCARRY(temp, toCarry);
}

int main() {
    string a;
    int carry, toCarry;
    cin >> a >> carry;
    numWithCARRY num(a, carry);
    cin >> toCarry;
    change(num, toCarry).show();
    return 0;
}