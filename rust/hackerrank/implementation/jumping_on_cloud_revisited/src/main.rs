extern crate utils;

fn get_final_energy(clouds:Vec<i32>, num_clouds:i32, jump_size:i32) -> i32 {
    let mut rem_energy = 100;
    let total_jumps = num_clouds / jump_size;
    for jump_id in 1..total_jumps + 1 {
        if clouds[((jump_id * jump_size) % num_clouds) as usize] == 1 {
            rem_energy -= 2;
        }
        rem_energy -= 1;
    }
    rem_energy
}

fn main() {
    let line:Vec<i32> = utils::read_line_of_integers();
    let clouds:Vec<i32> = utils::read_line_of_integers();
    println!("{}", get_final_energy(clouds, line[0], line[1]))
}

#[cfg(test)]

mod test {
    use super::get_final_energy;

    #[test]
    fn test_basic() {
        assert_eq!(get_final_energy(vec![0, 0, 1, 0, 0, 1, 1, 0], 8, 2), 92);
    }
}
