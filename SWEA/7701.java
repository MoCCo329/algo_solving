// No.33 염라대황의 이름 정렬  2023-02-16


import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
	
	static String[] words;
	static String[] newWords;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= T; tc++) {
			
			int N = Integer.parseInt(in.readLine());
			words = new String[N];
			newWords = new String[N];
			for (int i = 0; i < N; i++) words[i] = in.readLine();
			
			mergeSort(0, N - 1);
			
			System.out.println("#" + tc);
			System.out.println(newWords[0]);
			for (int i = 1; i < N; i++) if (!newWords[i].equals(newWords[i - 1])) System.out.println(newWords[i]);
		}
	}
	
	public static void mergeSort(int l, int r) {
		if (l >= r) return;
		
		int m = (l + r) / 2;
		mergeSort(l, m);
		mergeSort(m + 1, r);
		merge(l, r, m);
	}
	
	public static void merge(int l, int r, int mid) {
		int start = l;
		int end = r;
		r = mid + 1;
		int now = l;
		
		while (l <= mid && r <= end) {
			int temp = compare(words[l], words[r]);
			if (temp == 0) {
				newWords[now++] = words[l++];
				newWords[now++] = words[r++];
			} else if (temp < 0) newWords[now++] = words[l++];
			else newWords[now++] = words[r++];				
		}
		
		while (l <= mid) newWords[now++] = words[l++];
		while (r <= end) newWords[now++] = words[r++];
		
		for (int i = start; i <= end; i++) words[i] = newWords[i];
	}
	
	public static int compare(String o1, String o2) {
		if (o1.length() != o2.length()) return o1.length() - o2.length();
		for (int i = 0, size = o1.length(); i < size; i++) if (o1.charAt(i) != o2.charAt(i)) return o1.charAt(i) - o2.charAt(i);
		return 0;
	}
}
