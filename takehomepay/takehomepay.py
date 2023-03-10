from dataclasses import dataclass


@dataclass
class TakeHomePayBase:
    personal_allowance: int
    basic_rate: int
    higher_rate: int
    basic_rate_percentage: int
    higher_rate_percentage: int
    additional_rate_percentage: int
    national_insurance_rate: int
    lower_earnings_limit_ni: int  # 0% up to this limit
    upper_earnings_limit_ni: int  # 12% up to this limit, then 2% after

    def _calculate_basic_tax(self, gross, deductions):
        gross_minus_deductions = min(gross - deductions - self.personal_allowance, self.basic_rate - self.personal_allowance)
        if gross_minus_deductions < 0:
            return 0
        else:
            tax = (gross_minus_deductions / 100) * self.basic_rate_percentage
            return tax

    def _calculate_higher_tax(self, gross, deductions):
        gross_minus_deductions = min(gross - deductions - self.basic_rate, self.higher_rate - self.basic_rate)
        if gross_minus_deductions < 0:
            return 0
        else:
            tax = (gross_minus_deductions / 100) * self.higher_rate_percentage
            return tax

    def _calculate_additional_tax(self, gross, deductions):
        return 0

    def calculate_tax(self, gross, deductions):
        basic_tax = self._calculate_basic_tax(gross, deductions)
        deductions += basic_tax
        higher_tax = self._calculate_higher_tax(gross, deductions)
        deductions += higher_tax
        additional_tax = self._calculate_additional_tax(gross, deductions)
        total_tax = basic_tax + higher_tax + additional_tax

        return total_tax

    def calculate_national_insurance(self, gross, freq: str = "yearly"):
        weekly = gross / 52

        if int(weekly) in range(0, 184):
            ni = 0

        elif int(weekly) in range(184, 963):
            ni = (weekly - 183) * 0.12

        else:
            ni = (779 * 0.12) + ((weekly - 779 - 183) * 0.02)

        return ni

    def calculate_pension(self):
        pass


@dataclass
class TwentyTwentyTwo(TakeHomePayBase):
    personal_allowance: str = 12_570
    basic_rate: int = 50_270
    higher_rate: int = 150_000
    basic_rate_percentage: int = 20
    higher_rate_percentage: int = 40
    additional_rate_percentage: int = 45
    national_insurance_rate: int = 5
    lower_earnings_limit_ni: int = 6  # 0% up to this limit
    upper_earnings_limit_ni: int = 7  # 12% up to this limit, then 2% after

    def __post_init__(self):
        super().__init__(
            self.personal_allowance,
            self.basic_rate,
            self.higher_rate,
            self.basic_rate_percentage,
            self.higher_rate_percentage,
            self.additional_rate_percentage,
            self.national_insurance_rate,
            self.lower_earnings_limit_ni,
            self.upper_earnings_limit_ni,
        )
