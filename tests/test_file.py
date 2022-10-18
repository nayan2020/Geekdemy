import unittest
import os
import solution


class Unitest(unittest.TestCase):

    def test_func_1(self):
        import os
        this_dir = os.path.dirname(__file__)
        file_path = this_dir + '/../sample_input/input1.txt'

        result = solution.solution(file_path)
        flag = False
        if result["sub_total"] == "13000.00" and \
                result["applied_coupon"] == "B4G1" and \
                result["applied_coupon_amount"] == "2500.00" and \
                result["if_pro_member"] == "0.00" and \
                result["pro_member_fee"] == "0.00" and \
                result["enrollment_fee"] == "0.00" and \
                result["total_bill"] == "10500.00":
            flag = True

        self.assertTrue(flag)

    def test_func_2(self):
        this_dir = os.path.dirname(__file__)
        file_path = this_dir + '/../sample_input/input2.txt'
        result = solution.solution(file_path)

        flag = False
        if result["sub_total"] == "10000.00" and \
                result["applied_coupon"] == "DEAL_G20" and \
                result["applied_coupon_amount"] == "2000.00" and \
                result["if_pro_member"] == "0.00" and \
                result["pro_member_fee"] == "0.00" and \
                result["enrollment_fee"] == "0.00" and \
                result["total_bill"] == "8000.00":
            flag = True

        self.assertTrue(flag)


if __name__ == "__main__":
    unittest.main()
