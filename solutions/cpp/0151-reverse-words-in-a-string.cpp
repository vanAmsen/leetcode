class Solution {
public:
    string reverseWords(string s) {
        std::istringstream iss(s);
        std::vector<std::string> words;
        std::string word;
        
        while (iss >> word) {
            words.push_back(word);
        }
        
        std::reverse(words.begin(), words.end());
        
        std::string result;
        for (int i = 0; i < words.size(); ++i) {
            result += words[i];
            if (i < words.size() - 1) result += ' ';
        }
        
        return result;        
    }
};
