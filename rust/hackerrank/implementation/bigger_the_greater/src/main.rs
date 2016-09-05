extern crate utils;

fn next_lexicographically_greater<T:Ord>(mut arr: Vec<T>) -> Option<Vec<T>>{
    let mut i:usize = arr.len() - 1;
    while i > 0 && arr[i - 1] >= arr[i] {
        i -= 1;
    }
    if i <= 0 {
        return None;
    }
    let mut j:usize = arr.len() - 1;
    while arr[i - 1] >= arr[j] {
        j -= 1;
    }
    arr.swap(i - 1, j);
    reverse_from_end(&mut arr, i);
    Some(arr)
}

fn reverse_from_end<T:Ord>(arr: &mut Vec<T>, mut start:usize){
    let mut end = arr.len() - 1;
    while end > start {
        arr.swap(start, end);
        start += 1;
        end -= 1;
    }
}

fn main() {
    let num_testcases = utils::read_line_of_integers()[0];
    for _ in 0..num_testcases {
        let input_str = utils::read_line_as_string();
        let result = next_lexicographically_greater(input_str.into_bytes());
        if let Some(arr) = result {
            println!("{}", String::from_utf8(arr).unwrap());
        } else {
            println!("no answer");
        }
    }
}

#[cfg(test)]

mod test {
    use super::next_lexicographically_greater;

    #[test]
    fn test_basic() {
        let mut result = next_lexicographically_greater("ab".to_string().into_bytes());
        assert_eq!(String::from_utf8(result.unwrap()).unwrap(), "ba");
        result = next_lexicographically_greater("bb".to_string().into_bytes());
        assert_eq!(result, None);
        if let Some(arr) = next_lexicographically_greater("hefg".to_string().into_bytes()) {
            assert_eq!(String::from_utf8(arr).unwrap(), "hegf");
        }
    }

    #[test]
    fn test_type() {
        let mut result = next_lexicographically_greater(vec![1, 3, 6, 5]);
        assert_eq!(result.unwrap(), vec![1, 5, 3, 6]);
        result = next_lexicographically_greater(vec![1, 5, 5, 5]);
        assert_eq!(result.unwrap(), vec![5, 1, 5, 5]);
        result = next_lexicographically_greater(vec![5, 5, 5]);
        assert_eq!(result, None);
    }
}
