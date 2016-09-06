extern crate utils;
use std::cmp::max;

fn bribe_count(arr:Vec<i32>, array_len:i32) -> Option<u32> {
    let mut bribe_count:u32 = 0;
    for i in (0..array_len).rev(){
        if (arr[i as usize] - (i + 1)) > 2 {
            return None
        }
        for j in max(0, arr[i as usize] - 2)..i {
            if arr[j as usize] > arr[i as usize] {
                bribe_count+=1;
            }
        }
    }
    Some(bribe_count)
}

fn main() {
    let num_tests = utils::read_line_of_integers()[0];
    for _ in 0..num_tests {
        let array_len = utils::read_line_of_integers()[0];
        let arr = utils::read_line_of_integers();
        if let Some(count) = bribe_count(arr, array_len) {
            println!("{}", count);
        } else {
            println!("Too chaotic");
        }
    }
}

#[cfg(test)]
mod test {
    use super::bribe_count;

    #[test]
    fn test_basic() {
        assert_eq!(bribe_count(vec![2, 1, 5, 3, 4], 5), Some(3));
        assert_eq!(bribe_count(vec![2, 5, 1, 3, 4], 5), None);
    }
}
