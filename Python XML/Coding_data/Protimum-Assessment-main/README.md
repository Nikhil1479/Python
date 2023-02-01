# Protimum-Assessment

Problem Statement:-
You have been given bureau report of some customers in XML format. Bureau report is loan history
of the customer.The report has information of his historical trade experience, inquiries he/she has
made for loan requests. Trade experience includes information such as his/her the loan amount
taken by him/her, loan disbursed date, Date of report when his information is reported in bureau
and others information such as his payment dpd status and months.
DPD is days past due during his EMI duration. For example if a customer doesn’t repay his/her emi
for more than 30 days after his given repayment date, then it is said that a customer has gone
30+dpd.
The report has information about multiple trades according to the customer’s trade types (eg:-
Business Loan, Personal Loan ,etc.) , disbursed date, disbursed amount etc.
For each single trade you will have Disbursed Amount (loan amount) a customer has taken for that
loan (eg-100000(Disbursed Amount) for Business Loan(Account Type) on 01-06-2011(Disbursed
date) and for each trade you will have his payment history of that particular loan that has his/her
DPD value, status and month for which he has to pay back his EMI.
An example is shown below for a particular customer from his XML bureau report.
“<LOAN-DETAILS>
<ACCT-NUMBER>XXXX</ACCT-NUMBER>
<CREDIT-GUARANTOR>XXXX</CREDITGUARANTOR>
<ACCT-TYPE>Personal Loan</ACCT-TYPE>
<DATE-REPORTED>01-04-2019</DATE-REPORTED>
<OWNERSHIP-IND>Individual</OWNERSHIP-IND>
<ACCOUNT-STATUS>Active</ACCOUNT-STATUS>
<DISBURSED-AMT>60,000</DISBURSED-AMT>
<DISBURSED-DATE>16-08-2018</DISBURSED-DATE>
<INSTALLMENT-AMT>7,293</INSTALLMENT-AMT>
<OVERDUE-AMT>0</OVERDUE-AMT>
<WRITE-OFF-AMT>0</WRITE-OFF-AMT>
<CURRENT-BAL>14,252</CURRENT-BAL>
<SECURITY-STATUS>Un-secured</SECURITYSTATUS>
<COMBINED-PAYMENTHISTORY>Apr:2019,000/STD|Mar:2019,DDD/DDD|Feb:2019,31/xxx|Jan:2019,000/STD|Dec:2018,
DDD/DDD|Nov:2018,000/STD|Oct:2018,000/STD|Sep:2018,000/STD|Aug:2018,000/STD|</COMB
INED-PAYMENT-HISTORY>
<MATCHED-TYPE>PRIMARY</MATCHED-TYPE>
<SECURITY-DETAILS></SECURITY-DETAILS>
<LINKED-ACCOUNTS></LINKED-ACCOUNTS>
</LOAN-DETAILS>”
The information marked in red has Disbursed Amount and Payment history information of a
particular customer for a single trade.
<DISBURSED-AMT>60,000</DISBURSED-AMT>:-Loan amount is 60000 for this loan.
<COMBINED-PAYMENTHISTORY>Apr:2019,000/STD|Mar:2019,DDD/DDD|Feb:2019,31/xxx|Jan:2019,000/STD|Dec:2018,
DDD/DDD|Nov:2018,000/STD|Oct:2018,000/STD|Sep:2018,000/STD|Aug:2018,000/STD|</COMB
INED-PAYMENT-HISTORY>:- for April 2019 he has 0 DPD(he has paid his EMI on time) in Feb 2019
he has gone more than 30 days past due.
You are given ~10 customers datafiles. Calculate below mentioned 3 elements for all the 10
customers. Send out the csv/excel along with your working code for the problems.
Based on the above statement you have to write a python/R code to solve the following problems:-
1) What percentage of trades are with 30+ DPD (more than 30 days past due) among all
the trades available?
2) What is the sum of total disbursed amount for all loans for each customer?
3) What is the maximum number of months of 30+ due per trade was there?
e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
for trade 3 there are 3 occurrences then the answer will be 6.
