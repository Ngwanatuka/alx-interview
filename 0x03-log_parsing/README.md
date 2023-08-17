# 0x03-log_parsing

This script reads log lines from standard input (stdin), process the lines, and computes metrics according to a specified format. It's designed to calculate statistics based on the input log lines, such as total file and the status code. The script also handles interruption gracefully, providing results even if interrupted.

## Usage

1. **Generating Log Lines:** If you don't have log lines to use as input, you can generate them using the provided `0-generator.py` script. This script simulates the generation of log lines with random data. To generate log lines, run the following command:

```bash
./0-generator.py > log_input.txt
```

2. **Running the Script:** You can use the generated log lines as input for the `0-stats.py` script. To process the log lines and compute metrics, run the following command:
    
    ```
    ./0-generator.py | ./0-stats.py
    ```

## Script Breakdown

    Here's a simple breakdown of the `0-stats.py` script:

1. Import necessary modules:
   
   - `sys` is used to read from starndard input and write to standard output.
   - `status_codes_dict` is a dictionary to store the count of each status code.
   - `total_size` keeps track of the total file size.
   - `line_count` keeps track of how many lines have been processed.

2. The script reads log lines from the standard input line by line using a loop.
3. Each line is split into part using th `.split()` function, breaking into words.
4. If a line has at 10 words, it's considered valid and can be processed.
5. The status code and file size are extracted from the line.
6. If the status code is none of the desired codes (200, 301, etc.), its count in `status_code_dict` is increased.
7. The file size is added to the `total_size`.
8. The `line_count` is increased to keep track of the number of lines processed.
9. When `line_count` reaches 10, statistics are printed:
    - The total file size is printed.
    - The count of each status code is printed, in ascending order.
10. If someone inturrupts the program (using CTRL + C), it's handles gracefully using a `KeyboardInterrupt` exception.
11. In the `finally` block, the scipt prints the final results:
    - The total file size is printed.
    - The count of each status code is printed, in ascending order.

## Conclusion

This script helps you analyze log lines and calculates important metrics from them. It's designed to handle interruptions and provide meaningul statistics. Feel free to modify the script according to your specific needs.
