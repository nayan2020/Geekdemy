# Problem statement
 Geekdemy provides a wide variety of online education programmes. Students can purchase them and enroll in these programmes. Geekdemy offers attractive discounts through their coupons so that students can spend less while purchasing these programmes.
 
Programmes
 There are 3 different categories of online programmes, and the cost is different for each category. A student can purchase any number of programmes at a time.
 
 * CERTIFICATION - Rs.3000 
 * DEGREE - Rs. 5000 
 * DIPLOMA - Rs 2500
 
 
# Coupons
   The discount coupons offered by Geekdemy are based on different criteria. Only one discount coupon can be applied at a time.
 
   * B4G1 - This coupon is applied automatically if 4 or more programmes are being purchased. The student gets one programme for free. The lowest priced programme is      given for FREE.
 
   * DEAL_G20 - This coupon can be applied if the purchased programmes value is Rs.10,000/- or above. It provides a 20% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
   * DEAL_G5 - This coupon can only be applied if there are a minimum of 2 programmes being purchased. It provides a 5% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
# Enrollment Fee
   If the total programme cost is below Rs. 6666/, an extra enrollment fee Rs.500/- is added to the cart. The enrollment fee is applied after the discount. If the total programme cost is or above Rs.6666/- the enrollment fee is waived off.
 
# Pro Membership Fee
   A student can choose to purchase a Pro Membership for a small amount of Rs.200/- . The pro membership provides an additional membership discount on each of the individual programmes on top of the other discounts.
 
 * DIPLOMA - 1% discount 
 * CERTIFICATION - 2% discount 
 * DEGREE - 3% discount
 
![table_greek](https://user-images.githubusercontent.com/59414392/196351936-b6fb45a0-59e1-40bc-bb43-166796cc4d58.png)


# Pre-requisites
* Python 3.8/3.9
* Pip

# How to run the code

We have provided scripts to execute the code. 

Use `run.sh` if you are Linux/Unix/macOS Operating systems and `run.bat` if you are on Windows.  Both the files run the commands silently and prints only output from the input file `sample_input/input1.txt`. You are supposed to add the input commands in the file from the appropriate problem statement. 

Internally both the scripts run the following commands 

 * `pip install -r requirements.txt` - This will install the dependencies mentioned in the requirement.file
 * `python -m geektrust sample_input/input1.txt` - This will run the solution passing in the sample input file as the command line argument

If you are providing a solution without using the build file, we want you to name your Main file as geektrust.py. This is the file that will contain your main method.

 We expect your program to take the location to the text file as parameter. Input needs to be read from a text file, and output should be printed to the console. The text file will contain only commands in the format prescribed by the respective problem.

 # Running the code for multiple test cases

 Please fill `input1.txt` and `input2.txt` with the input commands and use those files in `run.bat` or `run.sh`. Replace `python -m geektrust sample_input/input1.txt` with `python -m geektrust sample_input/input2.txt` to run the test case from the second file. 

 # How to execute the unit tests

 `python -m unittest discover` will execute the unit test cases.

 The unit test coverage is found by the command :
`coverage run -m unittest discover`

# Help

You can refer our help documents [here](https://help.geektrust.com)
You can read build instructions [here](https://github.com/geektrust/coding-problem-artefacts/tree/master/Python)
