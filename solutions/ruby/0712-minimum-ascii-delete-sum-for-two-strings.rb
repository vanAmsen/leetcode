# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
    prev_row = Array.new(s2.length + 1, 0)
    (1..s2.length).each { |j| prev_row[j] = prev_row[j - 1] + s2[j - 1].ord }

    (1..s1.length).each do |i|
        curr_row = [prev_row[0] + s1[i - 1].ord]
        (1..s2.length).each do |j|
            if s1[i - 1] == s2[j - 1]
                curr_row << prev_row[j - 1]
            else
                curr_row << [prev_row[j] + s1[i - 1].ord, curr_row[j - 1] + s2[j - 1].ord].min
            end
        end
        prev_row = curr_row
    end

    prev_row[-1]
end
