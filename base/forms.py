from django import forms

class MoneyField(forms.DecimalField):
    def __init__(self, **kwargs):
        super(MoneyField, self).__init__(
            max_digits=15, decimal_places=2, **kwargs)

class BasicForm(forms.Form):
    age = forms.IntegerField(min_value=1, label="How old are you?")
    retire = forms.IntegerField(min_value=1, initial=65,
        label="When would you like to retire?",
        help_text="A typical age is 65 years old, although for Social Security purposes you can retire as early as 62 (with reduced benefits).")
    yearly_salary = MoneyField(label="What is your yearly salary?",
        help_text="How much does your job pay you?  Forget income from investing or other gains - just your job.")

class IncomeForm(forms.Form):
    monthly_salary = MoneyField(label="After-tax salary")
    interest = MoneyField(label="Interest income")
    other = MoneyField(label="Other income")

class ExpensesForm(forms.Form):
    rent = MoneyField(label="Rent/mortgage")
    credit_card = MoneyField(label="Credit card bills")
    cash = MoneyField(label="Cash spent")
    checks = MoneyField(label="Checks written")
    big_plans = forms.BooleanField(required=False,
        label="Do you have any big planned expenses in the next 6 to 12 months?  (New house, boat, etc.)")

class AssetsForm(forms.Form):
    cash = MoneyField(label="Cash")
    stock = MoneyField(label="Stocks/equities")
    fixed = MoneyField(label="Fixed income (bonds)")
    ira = MoneyField(label="401(k)/Roth IRA")

class LiabilitiesForm(forms.Form):
    credit_card = MoneyField(label="Credit card balance")
    mortgage = MoneyField(label="Mortgages")
    loan = MoneyField(label="Student loans")
    other = MoneyField(label="Other debt")

class RiskForm(forms.Form):
    friend_description = forms.TypedChoiceField(
        label="How would your best friend describe you as a risk taker?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (4, "A real gambler"),
            (3, "Willing to take risks after completing adequate research"),
            (2, "Cautious"),
            (1, "A real risk avoider"),
        )
    )
    tv = forms.TypedChoiceField(
        label="You are on a TV game show and can choose one of the following.  Which would you take?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "$1,000 in cash"),
            (2, "A 50% chance at winning $5,000"),
            (3, "A 25% chance at winning $10,000"),
            (4, "A 5% chance at winning $100,000"),
        )
    )
    vacation = forms.TypedChoiceField(
        label="You have just finished saving for a \"once-in-a-lifetime\" vacation.  Three weeks before you plan to leave, you lose your job.  You would:",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Cancel the vacation"),
            (2, "Take a much more modest vacation"),
            (3, "Go as scheduled, reasoning that you need the time to prepare for a job search"),
            (4, "Extend your vacation, because this might be your last chance to go first-class"),
        )
    )
    receive_20000 = forms.TypedChoiceField(
        label="If you unexpectedly received $20,000 to invest, what would you do?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Deposit it in a bank account, money market account, or an insured CD"),
            (2, "Invest it in safe high quality bonds or bond mutual funds"),
            (3, "Invest it in stocks or stock mutual funds"),
        )
    )
    experience = forms.TypedChoiceField(
        label="In terms of experience, how comfortable are you investing in stocks or stock mutual funds?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Not at all comfortable"),
            (2, "Somewhat comfortable"),
            (3, "Very comfortable"),
        )
    )
    word_association = forms.TypedChoiceField(
        label="When you think of the word \"risk\" which of the following words comes to mind first?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Loss"),
            (2, "Uncertainty"),
            (3, "Opportunity"),
            (4, "Thrill"),
        )
    )
    hard_assets = forms.TypedChoiceField(
        label="Some experts are predicting prices of gold and real estate (hard assets) to increase in value.  Most of your current investment assets are in high interest government bonds which are very safe, but may fall slightly in value.  What would you do?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Hold the bonds"),
            (2, "Sell the bonds, put half the proceeds into money market accounts, and the other half into hard assets"),
            (3, "Sell the bonds and put the total proceeds into hard assets"),
            (4, "Sell the bonds, put all the money into hard assets, and borrow additional money to buy more"),
        )
    )
    four = forms.TypedChoiceField(
        label="Given the best and worst case returns of the four investment choices below, which would you prefer?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "$200 gain best case; $0 gain/loss worst case"),
            (2, "$800 gain best case; $200 loss worst case"),
            (3, "$2,600 gain best case; $800 loss worst case"),
            (4, "$4,800 gain best case; $2,400 loss worst case"),
        )
    )
    choose = forms.TypedChoiceField(
        label="Choose between:",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "A sure gain of $500"),
            (2, "A 50% chance to gain $1,000 and 50% chance to gain nothing"),
        )
    )
    given_2000 = forms.TypedChoiceField(
        label="You have been given $2,000.  You are now asked to choose between:",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "A sure loss of $500 (you would now have only $1500)"),
            (2, "A 50% chance to lose $1,000 and a 50% chance to lose nothing"),
        )
    )
    inherit_100000 = forms.TypedChoiceField(
        label="Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL the money in ONE of the following choices.  Which one would you select?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "A savings account or money market mutual fund"),
            (2, "A mutual fund that owns stocks and bonds"),
            (3, "A portfolio of 15 common stocks"),
            (4, "Commodities like gold, silver, and oil"),
        )
    )
    invest_20000 = forms.TypedChoiceField(
        label="If you had to invest $20,000, which of the following investment choices would you find most appealing?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "60% in low-risk investments 30% in medium-risk investments 10% in high-risk investments"),
            (2, "30% in low-risk investments 40% in medium-risk investments 30% in high-risk investments"),
            (3, "10% in low-risk investments 40% in medium-risk investments 50% in high-risk investments"),
        )
    )
    geologist = forms.TypedChoiceField(
        label="Your trusted friend and neighbor, an experienced geologist, is putting together a group of investors to fund an exploratory gold mining venture.  The venture could pay back 50 to 100 times the investment if successful.  If the mine is a bust, the entire investment is worthless.  Your friend estimates the chance of success is only 20%.  If you had the money, how much would you invest?",
        widget=forms.RadioSelect, coerce=int, choices=(
            (1, "Nothing"),
            (2, "One month's salary"),
            (3, "Three month's salary"),
            (4, "Six month's salary"),
        )
    )
