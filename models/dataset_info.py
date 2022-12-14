class Info:
    def __init__(self):
        # mutated, passing, failing
        self.train_data = [
            ['cli_15', 273, 463, 2],
            ['cli_16', 346, 463, 7],
            ['cli_17',  98, 138, 1],
            ['cli_18', 100, 139, 1],
            ['cli_19', 101, 140, 1],
            ['cli_20', 101, 141, 1],
            ['cli_21', 300, 486, 1],
            ['cli_22', 131, 166, 2],
            ['cli_23', 124, 159, 2],
            ['cli_24', 119, 162, 1],
            ['cli_25', 121, 162, 1],
            ['cli_26', 136, 175, 1],
            ['cli_27', 164, 202, 3],
            ['cli_28', 242, 268, 1],
            ['cli_29', 265, 280, 1],
            ['cli_30', 239, 286, 9],
            ['cli_31', 255, 295, 1],
            ['cli_32', 266, 299, 2],
            ['cli_33', 273, 301, 1],
            ['cli_34', 259, 301, 2]
        ]


        self.test_data = [
            # ['cli_15', 273, 463, 2],
            # ['cli_16', 346, 463, 7],
            # ['cli_17',  98, 138, 1],
            # ['cli_18', 100, 139, 1],
            # ['cli_19', 101, 140, 1],
            # ['cli_20', 101, 141, 1],
            # ['cli_21', 300, 486, 1],
            # ['cli_22', 131, 166, 2],
            # ['cli_23', 124, 159, 2],
            # ['cli_25', 121, 162, 1],
            # ['cli_26', 136, 175, 1],
            ['cli_27', 164, 202, 3],
            # ['cli_28', 242, 268, 1],
            # ['cli_29', 265, 280, 1],
            # ['cli_30', 239, 286, 9],   #1
            # ['cli_31', 255, 295, 1],     #2
            # ['cli_32', 266, 299, 2],     #1
            # ['cli_33', 273, 301, 1],     #histo 2
            # ['cli_34', 259, 301, 2],
            # ['cli_35', 270, 357, 1],
            # ['cli_36', 241, 301, 1],
            # ['cli_37', 235, 303, 1],
            # ['cli_38', 235, 304, 1],
            # ['cli_39', 260, 322, 2]
        ]


def main():
    i = Info()
    print(i.num_of_testcases)


if __name__ == "__main__":
    main()