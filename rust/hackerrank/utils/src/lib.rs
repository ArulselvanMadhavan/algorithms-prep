use std::io;

pub fn read_line_of_integers() -> Vec<i32> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).ok().expect("Failed to read input");
    let input_vals_iter = buffer.split_whitespace();
    let mut input_vals_vec:Vec<i32> = vec![];
    for val in input_vals_iter {
        input_vals_vec.push(val.trim().parse().ok().expect("Failed to parse Integer"));
    }
    input_vals_vec
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
    }
}
