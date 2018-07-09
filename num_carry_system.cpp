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
    static map<int,char> valKey;
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
            temp += numWithBase::valKey.at(m%carry);
            m = m/carry;
        }
        reverse(temp.begin(),temp.end());
    }
    return numWithBase(temp,carry);
}

map<char, int> initialkeyVal() {
    map<char,int> keyValue;
    ifstream inFile(".\\keyValFile");
    int i = 0;
    char temp;
    while(!inFile.eof()) {
        inFile >> temp;
        keyValue.insert(make_pair(temp,i));
        i++;
    }
    inFile.close();
    return keyValue;
}

map<int,char> initialvalKey() {
    map<int,char> valueKey;
    ifstream inFile(".\\keyValFile");
    int i = 0;
    char temp;
    while(!inFile.eof()) {
        inFile >> temp;
        valueKey.insert(make_pair(i,temp));
        i++;
    }
    inFile.close();
    return valueKey;
}

map<char,int> numWithBase::keyVal(initialkeyVal());
map<int,char> numWithBase::valKey(initialvalKey());

int main() {
    string a;
    int carry, tocarry;
    cin >> a;
    cin >> carry >> tocarry;
    numWithBase num(a, carry);
    change(num, tocarry).show();
    return 0;
}