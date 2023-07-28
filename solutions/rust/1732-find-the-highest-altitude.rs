impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut max_altitude = 0; 
        let mut current_altitude = 0; 

        for &g in gain.iter() { 
            current_altitude += g; 
            if current_altitude > max_altitude { 
                max_altitude = current_altitude; 
            } 
        } 
        max_altitude 
                                                                                                   
    }
}
