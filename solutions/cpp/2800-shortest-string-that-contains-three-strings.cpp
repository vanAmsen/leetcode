class Solution {
public:
    string minimumString(string a, string b, string c) {
        auto merge = [](string s1, string s2) {
            if (s1.find(s2) != string::npos) return s1;
            for (int i = 0; i < s1.size(); i++) {
                if (s2.rfind(s1.substr(i), 0) == 0) return s1.substr(0, i) + s2;
            }
            return s1 + s2;
        };

        string res = "";
        int l = INT_MAX;
        for (string s : vector<string>{
            merge(merge(a, b), c),
            merge(merge(b, a), c),
            merge(merge(c, b), a),
            merge(merge(b, c), a),
            merge(merge(a, c), b),
            merge(merge(c, a), b)
        }) {
            if (s.size() < l) {
                res = s;
                l = s.size();
            } else if (s.size() == l) {
                res = min(res, s);
            }
        }

        return res;
    }
};
