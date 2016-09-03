use std::io;

fn can_meet(x1: i32, v1: i32, x2: i32, v2: i32) -> String{
    let mut result:String = "NO".to_string();
    if x1 == x2 {
        if v1 == v2 {
            result = "YES".to_string();
        } else {
            result = "NO".to_string();
        }
    } else if x1 < x2 {
        if v1 <= v2 {
            result = "NO".to_string();
        } else {
            if (x2 - x1) % (v1 - v2) == 0 {
                result = "YES".to_string();
            } else {
                result = "NO".to_string();
            }
        }
    }
    result
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).ok().expect("Failed to read input");
    let input_vals_iter = buffer.split_whitespace();
    let mut input_vals_vec:Vec<i32> = vec![];
    for val in input_vals_iter {
        input_vals_vec.push(val.trim().parse().ok().expect("Failed to parse Integer"));
    }
    println!("{}", can_meet(input_vals_vec[0], input_vals_vec[1],
                      input_vals_vec[2], input_vals_vec[3]));
}

#[cfg(test)]
mod test {
    use super::can_meet;

    #[test]
    fn kangaroo_basic() {
        assert!(can_meet(0, 3, 4, 2) == "YES");
        assert!(can_meet(0, 2, 5 ,3) == "NO");
    }
}
