class Solution {
    private String merge(String s1, String s2) {
        if (s1.contains(s2)) return s1;
        for (int i = 0; i < s1.length(); i++) {
            if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2;
        }
        return s1 + s2;
    }

    public String minimumString(String a, String b, String c) {
        String res = "";
        int l = Integer.MAX_VALUE;
        for (String s : new String[]{
            merge(merge(a, b), c),
            merge(merge(b, a), c),
            merge(merge(c, b), a),
            merge(merge(b, c), a),
            merge(merge(a, c), b),
            merge(merge(c, a), b)
        }) {
            if (s.length() < l) {
                res = s;
                l = s.length();
            } else if (s.length() == l) {
                res = res.compareTo(s) < 0 ? res : s;
            }
        }
        return res;
    }
}
