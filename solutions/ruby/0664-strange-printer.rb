def strange_printer(s)
    n = s.size
    dp = Array.new(n) {Array.new(n, 0)}

    (n-1).downto(0) do |i|
        dp[i][i] = 1
        (i+1...n).each do |j|
            dp[i][j] = dp[i][j-1] + 1
            (i...j).each do |k|
                if s[k] == s[j]
                    dp[i][j] = [dp[i][j], dp[i][k] + (k+1<=j-1 ? dp[k+1][j-1] : 0)].min
                end
            end
        end
    end

    dp[0][n-1]
end
