#include"list"
#include"cstdio"
#include"iostream"
#include"fstream"
#include"algorithm"
#include"string"
using namespace std;

class BUFFER
{
    private:
    list<string> text_strs;
    int lineNum;
    int linenow;
    list<string>::iterator it;
    list<string>::iterator line_now;

    public:
    void PrintLine();
    bool ReadBUFF();
    bool WriteBUFF();
    bool InsertNewline();
    int Find(string sub);
    bool SubStitude();
    bool NextLine();
    bool PreviousLine();
    bool ChangeLine(int line);
    bool View();
    bool End();
    bool Begin();
    bool Delete();
};

int main()
{
    BUFFER texteditor;
    printf("Welcome the HU\n");
    char op;
    while(true) {
        printf("Input the operation Code:");
        cin >> op;
        switch(op) {
            case 'R':texteditor.ReadBUFF();break;
            case 'W':texteditor.WriteBUFF();break;
            case 'I':texteditor.InsertNewline();break;
            case 'F':
            {
                printf("Input the substring you want to find:");
                string sub;
                cin >> sub;
                texteditor.Find(sub);
            }
            break;
            
            case 'S':
            {
                texteditor.SubStitude();
            }
            break;

            case 'N':texteditor.NextLine();break;
            case 'P':texteditor.PreviousLine();break;
            case 'C':
            {
                int line;
                printf("Input the line you want to switch to:");
                cin >> line;
                texteditor.ChangeLine(line);
            }
            break;
            
            case 'V':texteditor.View();break;
            case 'B':texteditor.Begin();break;
            case 'E':texteditor.End();break;
            case 'D':texteditor.Delete();break;
            case 'Q':return 1;
            case 'p':texteditor.PrintLine();break;
        }
    }
    return 0;
}

void BUFFER::PrintLine() {
    cout << linenow << ":" << *line_now << endl;
}

bool BUFFER::ReadBUFF()
{
    bool flag;
    ifstream inFile;
    string temp;
    inFile.open(".\\TEXT");
    flag = inFile.good();
    if(flag == false) {
        return flag;
    }
    lineNum = 0;
    linenow = 0;
    text_strs.clear();
    while(inFile.peek() != EOF) {
        getline(inFile,temp);
        text_strs.push_back(temp);
        lineNum++;
    }
    if(text_strs.empty()) {
        inFile.close();
        return false;
    }
    line_now = text_strs.begin();
    linenow = 1;
    inFile.close();
    return true;
}

bool BUFFER::WriteBUFF() {
    bool flag;
    ofstream outFile;
    outFile.open(".\\TEXT");
    flag = outFile.good();
    if(flag == false) {
        return flag;
    }
    if(!text_strs.empty()) {
        for(it = text_strs.begin(); it != text_strs.end(); it++) {
            outFile << *it << endl;
        }
    }
    outFile.close();
    return true;
}

bool BUFFER::InsertNewline() {
    int n;
    string newline;
    printf("Please Input the Line No. you want to insert:");
    scanf("%d",&n);
    if(n <= 0 || n > lineNum+1) {
        printf("Invalid Line No. Operation Failed.\n");
        return false;
    }
    printf("Now you can input the content of the new line:\n");
    cin.ignore(1024,'\n');
    getline(cin,newline);
    line_now = text_strs.begin();
    for(int i = 1; i < n; i++) {
        line_now++;
    }
    text_strs.insert(line_now,newline);
    linenow = n;
    lineNum++;
    return true;
}

int BUFFER::Find(string sub) {
    int line = 1;
    it = text_strs.begin();
    for(; it != text_strs.end(); it++, line++) {
        if(it->find(sub) !=string::npos) {
            return line;
        }
    }
    return -1;
}

bool BUFFER::SubStitude() {
    if(text_strs.empty()) {
        return true;
    }
    string sub, substition;
    printf("Input the substring you want to find:");
    cin >> sub;
    printf("Input the substitution:");
    cin >> substition;
    it = text_strs.begin();
    char op;
    int len = sub.length();
    string::size_type index;
    printf("Is All-content-valid(Y/N):");
    cin >> op;
    switch(op) {
        case 'y':
        case 'Y':
            for(; it != text_strs.end(); it++) {
                index = 0;
                while(index = it->find(sub), index != string::npos) {
                    it->replace(index,len,substition);
                }
            }
            //implementation
            break;

        case 'n':
        case 'N':
            index = 0;
            while(index = it->find(sub), index != string::npos) {
                it->replace(index,len,substition);
            }
            //implementation
            break;
    }
    return true;
}

bool BUFFER::NextLine() {
    if(line_now !=text_strs.end()) {
        line_now++;
        linenow++;
        return true;
    }
    return false;
}

bool BUFFER::PreviousLine() {
    if(line_now != text_strs.begin()) {
        line_now--;
        linenow--;
        return true;
    }
    return false;
}

bool BUFFER::ChangeLine(int line) {
    if(line >= 1 && line <= text_strs.size()) {
        advance(line_now,line-linenow);
        linenow = line;
        return true;
    }
    return false;
}

bool BUFFER::View() {
    if(text_strs.empty()) {
        return false;
    }
    else {
        for(it = text_strs.begin(); it != text_strs.end(); it++) {
            cout << *it << endl;
        }
        return true;
    }
}

bool BUFFER::Begin() {
    line_now = text_strs.begin();
    linenow = 1;
}

bool BUFFER::End() {
    line_now = text_strs.end();
    line_now--;
    linenow = lineNum;
    return true;
}

bool BUFFER::Delete() {
    if(text_strs.empty()) {
        return false;
    }
    this->PrintLine();
    line_now = text_strs.erase(line_now);
    lineNum--;
    return true;
}