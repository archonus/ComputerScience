public class LCS {
    public static String longestCommonSubsequence(String xs, String ys){
        int n = xs.length();
        int m = ys.length();
        String[][] memo = new String[n+1][m+1]; // Includes the empty string
        for (int i = 0; i < n; i++){
            memo[i][0] = "";
        }
        for(int j = 0; j < m; j ++){
            memo[0][j] = "";
        }
        return lcs_memo(xs, ys, n,m,memo);
    }

    /** Find a maximal common subsequence between the strings xs[0:i] and ys[0:j]
     * @param xs The full first string
     * @param ys The full second string
     * @param i The number of characters from the start of xs being considered:
     *         i = xs.length() means entire string being considered
     * @param j The number of characters from the start of ys being considered
     * @param memo The memo which stores previously computed values
     * @return A maximal common subsequence between xs[0:i] and ys[0:j]
     */
    private static String lcs_memo(String xs, String ys, int i, int j, String[][] memo){

        if(i < 0 || j < 0 || i > xs.length() || j > ys.length()){
            throw new IllegalArgumentException();
        }
        var result = new StringBuilder();
        if(memo[i][j] != null){
            return memo[i][j];
        }
        else{ // Not in memo
            if (i == 0 || j == 0){ //If memo correctly constructed, should not occur
                // i = 0 means considering empty string
            }
            else if(xs.charAt(i-1) == ys.charAt(j-1)){ // 0 based indexing means index of last character is i-1
                result.append(
                        lcs_memo(xs,ys,i-1,j-1,memo)
                );
                result.append(xs.charAt(i-1)); // i-1 because 0 based indexing

            }
            else{
                var s1 = lcs_memo(xs,ys, i-1, j, memo); // Shorten xs
                var s2 = lcs_memo(xs,ys,i, j-1, memo); // Shorten ys
                if(s1.length() >= s2.length()){
                    result.append(s1); // If they are equal, arbitrarily choose s1
                }
                else{
                    result.append(s2);
                }
            }
            var s = result.toString();
            memo[i][j] = s;
            return s;
        }
    }
}
