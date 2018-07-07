#include<sstream>
#include<map>
#include<iostream>
#include<string>
using namespace std;

class numWithBase{
    private:
    static map<char, int>reflectTbl;
    int carry;
    string num;
    public:
    numWithBase(string a, int k);
    ~numWithBase(){};
    void show() {
        cout << num << endl;
    }
    friend numWithBase change(const numWithBase &obj);
};

numWithBase::numWithBase(string a, int k):carry(k) {
    num = a;
}

numWithBase change(const numWithBase &obj) {
    stringstream ss;
    string temp = obj.num;
    int m = 0;
    for(int i = 0; i < obj.num.length(); i++) {
        m = m * obj.carry + (temp[i] - '0');
    }
    ss<< m;
    ss >> temp;
    return numWithBase(temp, 10);
}

map<char, int> initial() {

}

int main() {
    string a;
    int carry;
    cin >> a;
    cin >> carry;
    numWithBase num(a, carry);
    change(num).show();
    return 0;
}