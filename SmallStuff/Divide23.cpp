bool divided_by_23(unsigned int w) {
    int bits = 8*sizeof(unsigned int);
    int i = 0;
    bool s;
    while(w) {
        s = ((1<<(bits-1)&w) == 0);
        i = i*2 +s;
        if(i >= 23) {
            i -= 23;
        }
    }
    return i==0;
}