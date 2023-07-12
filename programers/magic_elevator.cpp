int solution(int storey) {
    int ans = 0;
    
    while (storey != 0) {
        int temp = storey % 10;
        
        if (temp == 5)
        {
            if (4 < (storey % 100) / 10) storey += 10;
            ans += 5;
        }
        else if (temp < 5) ans += temp;
        else {
            storey += 10;
            ans += 10 - temp;
        }
        storey /= 10;
    }
    
    return ans;
}