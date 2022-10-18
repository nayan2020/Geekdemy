from class_file import Programme


def solution(*args) -> dict:
    products = [
        ["CERTIFICATION", 3000, .02],
        ["DEGREE", 5000, .03],
        ["DIPLOMA", 2500, .01],
    ]

    coupons = {
        "B4G1": 0,
        "DEAL_G20": .2,
        "DEAL_G5": .05,
        "None": 0,
    }

    programme = Programme()
    for product in products:
        programme.add_programme(name=product[0], rate=product[1], pro_discount=product[2])

    sub_total = 0  # total of the purchase
    total_bill = 0  # total of the bill
    total_bill_10000 = 10000
    total_bill_6666 = 6666
    if_pro_member = 0  # if pro member present then discount will be count
    no_of_product = 0
    no_of_product_2 = 2
    no_of_product_4 = 4
    applied_coupon = "None"  # replaced by applied coupon
    applied_coupon_amount = 0
    applied_pro_member = False  # Pro membership is applied or not
    pro_member_fee = 200  # given
    applied_enrollment_fee = False  # Enrollment Fee is applied or not
    enrollment_fee = 500  # given
    low_price_product = products[0][1]
    low_price_product_name = ""

    file_path = args[0]
    f = open(file_path, 'r')
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        if line[0] == "ADD_PROGRAMME":
            product_price = programme.get_programme_rate(line[1])
            if low_price_product > product_price:
                low_price_product = product_price
                low_price_product_name = line[1]
            quantity = int(line[2])
            sub_total += product_price * quantity
            total_bill = sub_total
            if_pro_member += product_price * programme.get_programme_discount(line[1]) * quantity
            no_of_product += quantity

        elif line[0] == "APPLY_COUPON":
            coupon_name = line[1][:-1]

            if no_of_product >= no_of_product_4:
                applied_coupon = "B4G1"

            else:
                if sub_total >= total_bill_10000 and coupon_name == "DEAL_G20" and \
                        coupons[applied_coupon] < coupons[coupon_name]:
                    applied_coupon = "DEAL_G20"

                if no_of_product >= no_of_product_2 and coupon_name == "DEAL_G5" and \
                        coupons[applied_coupon] < coupons[coupon_name]:
                    applied_coupon = "DEAL_G5"

        elif line[0][:-1] == "ADD_PRO_MEMBERSHIP":
            applied_pro_member = True
            total_bill = sub_total - if_pro_member
            total_bill += pro_member_fee
            sub_total = total_bill

            # lowest product price will be change
            product_price = programme.get_programme_rate(low_price_product_name)
            product_discount = programme.get_programme_discount(low_price_product_name)
            low_price_product = product_price - product_price * product_discount

        elif line[0] == "PRINT_BILL":

            applied_coupon_amount += total_bill * coupons[applied_coupon]

            f.close()

            return calculate_final_bill(sub_total,
                                        applied_coupon, applied_coupon_amount,
                                        applied_pro_member, if_pro_member, pro_member_fee,
                                        applied_enrollment_fee, low_price_product,
                                        enrollment_fee, total_bill_6666, total_bill, )


def calculate_final_bill(sub_total: int,
                         applied_coupon: str, applied_coupon_amount: int,
                         applied_pro_member: bool, if_pro_member: int, pro_member_fee: int,
                         applied_enrollment_fee: bool, low_price_product,
                         enrollment_fee: int, total_bill_6666: int, total_bill: int) -> dict:
    # for unit test
    result = {}
    # applied coupon calculation
    # for B4G1
    if applied_coupon == "B4G1":
        applied_coupon_amount += low_price_product

    total_bill -= applied_coupon_amount

    # Enroll fee calculation if applicable
    if total_bill < total_bill_6666:
        applied_enrollment_fee = True
        total_bill += enrollment_fee

    # print the bill
    result["sub_total"] = f"{sub_total:.2f}"
    if applied_coupon != "None":
        result["applied_coupon"] = applied_coupon
        result["applied_coupon_amount"] = f"{applied_coupon_amount:.2f}"
    else:
        result["applied_coupon"] = applied_coupon
        result["applied_coupon_amount"] = f"{applied_coupon_amount:.2f}"

    if not applied_pro_member:
        result["if_pro_member"] = f"{0:.2f}"
        result["pro_member_fee"] = f"{0:.2f}"
    else:
        result["if_pro_member"] = f"{if_pro_member:.2f}"
        result["pro_member_fee"] = f"{pro_member_fee:.2f}"

    if not applied_enrollment_fee:
        result["enrollment_fee"] = f"{0:.2f}"
    else:
        result["enrollment_fee"] = f"{enrollment_fee:.2f}"

    result["total_bill"] = f"{total_bill:.2f}"
    return result
