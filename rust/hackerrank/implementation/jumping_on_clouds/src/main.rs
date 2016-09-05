extern crate utils;

fn get_min_jumps_count(clouds:Vec<i32>, num_clouds: i32) -> i32 {
    let mut cur_pos:i32 = 0;
    let mut count:i32 = 0;
    while cur_pos < (num_clouds - 1) {
        if (cur_pos + 2) < num_clouds && clouds[(cur_pos + 2) as usize] != 1 {
            cur_pos += 2;
        } else {
            cur_pos += 1;
        }
        count += 1;
    }
    count
}

fn main() {
    let num_clouds = utils::read_line_of_integers()[0];
    let clouds = utils::read_line_of_integers();
    println!("{}", get_min_jumps_count(clouds, num_clouds));
}

#[cfg(test)]
mod test {
    use super::get_min_jumps_count;

    #[test]
    fn test_basic() {
        assert_eq!(get_min_jumps_count(vec![0, 0, 0, 0, 1, 0], 6), 3);
    }
}
