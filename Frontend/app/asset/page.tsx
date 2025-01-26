"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useState } from "react";

export default function AssetPage() {
  // State for form inputs
  const [ageGroup, setAgeGroup] = useState("");
  const [incomeLevel, setIncomeLevel] = useState("");
  const [financialGoal, setFinancialGoal] = useState("");
  const [riskTolerance, setRiskTolerance] = useState("");
  const [currentPortfolio, setCurrentPortfolio] = useState({
    Stocks: 0,
    Bonds: 0,
    "Real Estate": 0,
    "Mutual Funds": 0,
    ETFs: 0,
    Cryptocurrency: 0,
  });

  // State for recommendation
  const [recommendation, setRecommendation] = useState(null);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Prepare payload
    const payload = {
      age_group: ageGroup,
      income_level: incomeLevel,
      financial_goal: financialGoal,
      risk_tolerance: riskTolerance,
    };

    // Debugging: Log the payload
    console.log("Payload:", payload);

    // Send data to the API endpoint
    try {
      const response = await fetch("http://localhost:5000/asset", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      console.log("API Response:", data); // Debugging line
      setRecommendation(data);
    } catch (error) {
      console.error("Error fetching recommendation:", error);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8 bg-gray-50 min-h-screen">
      {/* Header */}
      <header className="text-center mb-12">
        <h1 className="text-5xl font-bold text-gray-900 mb-4">AI Asset Allocation</h1>
        <p className="text-xl text-gray-600">
          Optimize your portfolio with AI-driven asset allocation recommendations.
        </p>
      </header>

      {/* AI Asset Allocation Form */}
      <form onSubmit={handleSubmit} className="mt-8 max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">Input Your Details</h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Age Group */}
          <div>
            <label className="block text-sm font-medium text-gray-700">Age Group</label>
            <select
              value={ageGroup}
              onChange={(e) => setAgeGroup(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
              required
            >
              <option value="">Select Age Group</option>
              <option value="18-25">18-25</option>
              <option value="26-35">26-35</option>
              <option value="36-45">36-45</option>
              <option value="46-55">46-55</option>
              <option value="56+">56+</option>
            </select>
          </div>

          {/* Income Level */}
          <div>
            <label className="block text-sm font-medium text-gray-700">Income Level</label>
            <select
              value={incomeLevel}
              onChange={(e) => setIncomeLevel(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
              required
            >
              <option value="">Select Income Level</option>
              <option value="Low">Low</option>
              <option value="Medium">Medium</option>
              <option value="Medium-High">Medium-High</option>
              <option value="High">High</option>
            </select>
          </div>

          {/* Financial Goal */}
          <div>
            <label className="block text-sm font-medium text-gray-700">Financial Goal</label>
            <select
              value={financialGoal}
              onChange={(e) => setFinancialGoal(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
              required
            >
              <option value="">Select Financial Goal</option>
              <option value="Retirement">Retirement</option>
              <option value="Wealth Accumulation">Wealth Accumulation</option>
              <option value="Education">Education</option>
              <option value="Home Purchase">Home Purchase</option>
            </select>
          </div>

          {/* Risk Tolerance */}
          <div>
            <label className="block text-sm font-medium text-gray-700">Risk Tolerance</label>
            <select
              value={riskTolerance}
              onChange={(e) => setRiskTolerance(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
              required
            >
              <option value="">Select Risk Tolerance</option>
              <option value="Low">Low</option>
              <option value="Balanced">Balanced</option>
              <option value="High">High</option>
            </select>
          </div>
        </div>

        {/* Current Portfolio Inputs */}
        <div className="mt-6">
          <h3 className="text-lg font-medium text-gray-700 mb-4">Current Portfolio Allocation (%)</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {Object.keys(currentPortfolio).map((asset) => {
              console.log("Asset:", asset, "Value:", currentPortfolio[asset]); // Debugging line
              return (
                <div key={asset}>
                  <label className="block text-sm font-medium text-gray-700">{asset}</label>
                  <input
                    type="number"
                    value={currentPortfolio[asset] || 0} // Fallback to 0 if undefined
                    onChange={(e) =>
                      setCurrentPortfolio({
                        ...currentPortfolio,
                        [asset]: parseInt(e.target.value) || 0, // Ensure value is a number
                      })
                    }
                    className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    min="0"
                    max="100"
                    required
                  />
                </div>
              );
            })}
          </div>
        </div>

        {/* Submit Button */}
        <div className="mt-6">
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition-colors"
          >
            Get Recommendation
          </button>
        </div>
      </form>

      {/* Display Recommendation */}
      {recommendation && (
        <div className="mt-12">
          <h2 className="text-3xl font-bold text-gray-900 mb-6">Your AI Recommendation</h2>
          <Card className="bg-white">
            <CardHeader>
              <CardTitle className="text-2xl font-bold text-gray-800">
                Strategy: {recommendation.strategy}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <h3 className="text-xl font-bold text-gray-800 mb-4">Recommended Allocation:</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {Object.entries(recommendation.allocation).map(([asset, allocation]) => (
                  <div key={asset} className="bg-gray-50 p-4 rounded-lg">
                    <p className="text-lg text-gray-700">
                      {asset}: <span className="font-bold">{allocation}%</span>
                    </p>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      )}

      {/* Footer */}
      <footer className="text-center py-6 border-t border-gray-200 bg-white">
        <p className="text-gray-600">
          &copy; 2023 AI Portfolio Insights. All rights reserved.
        </p>
      </footer>
    </div>
  );
}