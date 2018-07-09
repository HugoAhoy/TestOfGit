#include<sstream>
#include<map>
#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
using namespace std;

class numWithBase{
    private:
    static map<char, int> keyVal;
    int carry;
    string num;
    public:
    numWithBase(string a, int k);
    ~numWithBase(){};
    void show() {
        cout << num << endl;
    }
    friend numWithBase change(const numWithBase &obj, int carry);
};

numWithBase::numWithBase(string a, int k):carry(k) {
    num = a;
}

numWithBase change(const numWithBase &obj, int carry) {
    stringstream ss;
    string temp = obj.num;
    int m = 0;
    for(int i = 0; i < obj.num.length(); i++) {
        m = m * obj.carry + numWithBase::keyVal.at(temp[i]);
    }
    ss << m;
    ss >> temp;
    if(carry != 10) {
        temp = "";
        while(m) {
            temp += (char)(m%carry + '0');
            m = m/carry;
        }
        reverse(temp.begin(),temp.end());
    }
    return numWithBase(temp, carry);
}

map<char, int> initial() {
    map<char,int> keyValue;
    ifstream inFile(".\\keyValFile");
    int i = 1;
    char temp;
    while(!inFile.eof()) {
        inFile >> temp;
        keyValue.insert(make_pair(temp,i));
        i++;
    }
    inFile.close();
    return keyValue;
}
map<char,int> numWithBase::keyVal(initial());
int main() {
    string a;
    int carry, tocarry;
    cin >> a;
    cin >> carry >> tocarry;
    numWithBase num(a, carry);
    change(num, tocarry).show();
    return 0;
}