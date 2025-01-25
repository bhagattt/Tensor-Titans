from flask import Blueprint, request, jsonify
from app.services.investment_service import recommend_investment_strategy

investment_bp = Blueprint('investment', __name__)

@investment_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()

    age_group = data.get('age_group')
    income_level = data.get('income_level')
    financial_goal = data.get('financial_goal')
    risk_tolerance = data.get('risk_tolerance')
    current_portfolio = data.get('current_portfolio')

    if not all([age_group, income_level, financial_goal, risk_tolerance, current_portfolio]):
        return jsonify({'error': 'Missing required fields'}), 400

    recommendation = recommend_investment_strategy(
        age_group=age_group,
        income_level=income_level,
        financial_goal=financial_goal,
        risk_tolerance=risk_tolerance,
        current_portfolio=current_portfolio
    )

    return jsonify(recommendation)