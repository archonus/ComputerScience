public class LCS {
    public static String longestCommonSubsequence(String xs, String ys){
        int n = xs.length();
        int m = ys.length();
        String[][] memo = new String[n][m];
        for (int i = 0; i < n; i++){
            memo[i][0] = "";
        }
        for(int j = 0; j < m; j ++){
            memo[0][j] = "";
        }
        return lcs_memo(xs, ys, n,m,memo);
    }

    private static String lcs_memo(String xs, String ys, int i, int j, String[][] memo){

        if(i < 0 || j < 0){
            throw new IllegalArgumentException();
        }
        var result = new StringBuilder();
        if(memo[i][j] != null){
            return memo[i][j];
        }
        else{ // Not in memo
            if (i == 0 || j == 0){ //If memo correctly constructed, should not occur
                // Nothing to do: return empty string
            }
            else if(xs.charAt(i) == ys.charAt(j)){
                result.append(
                        lcs_memo(xs,ys,i-1,j-1,memo)
                );
                result.append(xs.charAt(i));

            }
            else{
                var s1 = lcs_memo(xs,ys, i-1, j, memo);
                var s2 = lcs_memo(xs,ys,i, j-1, memo);
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
