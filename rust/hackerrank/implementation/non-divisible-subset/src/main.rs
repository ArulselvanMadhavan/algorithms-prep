extern crate utils;
use std::cmp;

fn non_divisible_subset_length(nums:Vec<i32>, n:i32, k:i32) -> i32 {
    let mut count:Vec<i32> = vec![0;k as usize];
    for i in 0..n as usize {
        count[(nums[i] % k) as usize] += 1;
    }
    let mut final_count = cmp::min(count[0], 1);
    for i in 1..(k/2 + 1){
        if i != k - i {
            final_count += cmp::max(count[i as usize], count[(k - i) as usize]);
        }
    }
    if k % 2 == 0 {
        final_count += 1
    }
    final_count
}

fn main() {
    let line:Vec<i32> = utils::read_line_of_integers();
    let n = line[0];
    let k = line[1];
    let numbers:Vec<i32> = utils::read_line_of_integers();
    println!("{:?}", non_divisible_subset_length(numbers, n, k));
}

#[cfg(test)]
mod test {
    use super::non_divisible_subset_length;

    #[test]
    fn test_basic() {
        let result = non_divisible_subset_length(vec![1, 7, 2, 4], 4, 3);
        assert!(result == 3);
    }
}
