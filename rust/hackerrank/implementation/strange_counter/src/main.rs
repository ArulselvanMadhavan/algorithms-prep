extern crate utils;

fn get_counter_val(time_val:u64) -> u64 {
    let mut i:u32 = 0;
    let mut total_counter_val:u64 = 3 * 2u64.pow(i);
    while time_val > total_counter_val {
        i += 1;
        total_counter_val = total_counter_val + (3 * 2u64.pow(i));
    }
    (total_counter_val - time_val) + 1
}

fn main() {
    let time_val = utils::read_line_of_integers()[0];
    println!("{}", get_counter_val(time_val as u64));
}


#[cfg(test)]
mod test {
    use super::get_counter_val;

    #[test]
    fn test_basic() {
        assert_eq!(get_counter_val(3), 1);
        assert_eq!(get_counter_val(20), 2);
        assert_eq!(get_counter_val(21), 1);
    }
}
