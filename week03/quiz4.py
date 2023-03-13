def main():
    num_row = int(input("Number of row: "))
    num_col = int(input("Number of column: "))
    grid_szie = int(input("Grid size: "))
    print((("+" + "-" * grid_szie) * num_col + "+\n" + (("|" + " " * grid_szie) * num_col + "|\n") * grid_szie) * num_row +
     ("+" + "-" * grid_szie) * num_col + "+")
