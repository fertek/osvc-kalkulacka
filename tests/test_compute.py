from decimal import Decimal

from osvc_kalkulacka.core import Inputs, compute


def test_compute_regression_2025_example():
    inp = Inputs(
        income_czk=800_000,
        child_months_by_order=(12,),
        min_wage_czk=20_800,
        expense_rate=Decimal("0.60"),
        section_15_allowances_czk=150_000,
        tax_rate=Decimal("0.15"),
        taxpayer_credit_czk=30_840,
        spouse_allowance_czk=24_840,
        child_bonus_annual_tiers_czk=(15_204, 22_320, 27_840),
        avg_wage_czk=46_557,
        zp_rate=Decimal("0.135"),
        sp_rate=Decimal("0.292"),
        zp_vym_base_share=Decimal("0.50"),
        sp_vym_base_share=Decimal("0.55"),
        zp_min_base_share=Decimal("0.50"),
        sp_min_base_share=Decimal("0.35"),
    )

    res = compute(inp)

    assert res.tax.base_profit_czk == 320_000
    assert res.tax.tax_final_czk == 0
    assert res.tax.bonus_to_pay_czk == 15_204
    assert res.ins.zp_annual_payable_czk == 37_712
    assert res.ins.sp_annual_payable_czk == 57_098


def test_child_bonus_ineligible_when_income_below_minimum():
    inp = Inputs(
        income_czk=100_000,
        child_months_by_order=(12,),
        min_wage_czk=20_800,
        expense_rate=Decimal("0.60"),
        section_15_allowances_czk=0,
        tax_rate=Decimal("0.15"),
        taxpayer_credit_czk=30_840,
        spouse_allowance_czk=0,
        child_bonus_annual_tiers_czk=(15_204, 22_320, 27_840),
        avg_wage_czk=0,
        zp_rate=Decimal("0.135"),
        sp_rate=Decimal("0.292"),
        zp_vym_base_share=Decimal("0.50"),
        sp_vym_base_share=Decimal("0.55"),
        zp_min_base_share=Decimal("0.0"),
        sp_min_base_share=Decimal("0.0"),
    )

    res = compute(inp)

    assert res.tax.child_bonus_eligible is False
    assert res.tax.child_bonus_czk == 0


def test_minimums_use_avg_wage_when_profit_low():
    inp = Inputs(
        income_czk=0,
        child_months_by_order=(),
        min_wage_czk=0,
        expense_rate=Decimal("0.60"),
        section_15_allowances_czk=0,
        tax_rate=Decimal("0.15"),
        taxpayer_credit_czk=0,
        spouse_allowance_czk=0,
        child_bonus_annual_tiers_czk=(15_204, 22_320, 27_840),
        avg_wage_czk=100,
        zp_rate=Decimal("0.10"),
        sp_rate=Decimal("0.20"),
        zp_vym_base_share=Decimal("0.50"),
        sp_vym_base_share=Decimal("0.55"),
        zp_min_base_share=Decimal("0.50"),
        sp_min_base_share=Decimal("0.40"),
    )

    res = compute(inp)

    assert res.ins.min_zp_monthly_czk == 5
    assert res.ins.min_sp_monthly_czk == 8
    assert res.ins.zp_annual_payable_czk == 60
    assert res.ins.sp_annual_payable_czk == 96
