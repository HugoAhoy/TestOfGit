#include"iostream"
#include"cstring"
using namespace std;

void string_reverse(char *);//反转函数声明

int main () {
    char raw[101];
    cin >> raw;
    cout << raw << endl;    
    string_reverse(raw);
    cout << raw << endl;
    return 0;
}

void string_reverse (char * raw_string) {
    int len = strlen(raw_string);
    if(len > 100) {
        len = 100;
    }
    char temp;
    for(int i = 0; i < len / 2; i++) {
        temp = *(raw_string + i);
        *(raw_string + i) = *(raw_string + len - 1 - i);
        *(raw_string + len - 1 - i) = temp;
    }
    return;
}