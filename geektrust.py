from sys import argv
import solution


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    result = solution.solution(file_path)

    print(f"SUB_TOTAL {result['sub_total']}")
    print(f"COUPON_DISCOUNT {result['applied_coupon']} {result['applied_coupon_amount']}")
    print(f"TOTAL_PRO_DISCOUNT {result['if_pro_member']}")
    print(f"PRO_MEMBERSHIP_FEE {result['pro_member_fee']}")
    print(f"ENROLLMENT_FEE {result['enrollment_fee']}")
    print(f"TOTAL {result['total_bill']}")

    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """


if __name__ == "__main__":
    main()
