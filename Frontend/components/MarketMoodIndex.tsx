"use client"

import { useState, useEffect } from "react"
import { PieChart, Pie, Cell, ResponsiveContainer, Legend } from "recharts"

// Define the type for sentiment data
interface SentimentData {
  sentiment: string
  value: number
}

// Simulated sentiment data
const initialSentiments: SentimentData[] = [
  { sentiment: "Positive", value: 60 }, // 60% positive
  { sentiment: "Negative", value: 20 }, // 20% negative
  { sentiment: "Neutral", value: 20 },  // 20% neutral
]

// Colors for the pie chart
const COLORS = ["#10B981", "#EF4444", "#FBBF24"]

export default function MarketMoodIndex() {
  const [sentiments, setSentiments] = useState<SentimentData[]>(initialSentiments)

  // Simulate live updates to the market mood index
  useEffect(() => {
    const interval = setInterval(() => {
      setSentiments((prevSentiments) =>
        prevSentiments.map((sentiment) => ({
          ...sentiment,
          value: Math.max(0, Math.min(100, sentiment.value + (Math.random() * 10 - 5))), // Randomly adjust values
        }))
      )
    }, 5000) // Update every 5 seconds

    return () => clearInterval(interval)
  }, [])

  // Calculate the overall market mood index
  const marketMoodIndex = (
    (sentiments[0].value - sentiments[1].value) / 100
  ).toFixed(2)

  // Convert marketMoodIndex to a number for comparison
  const moodIndexNumber = parseFloat(marketMoodIndex)

  return (
    <div className="bg-background py-4">
      <div className="container">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Market Mood Index */}
          <div className="p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Market Mood Index</h2>
            <p className="text-4xl font-semibold">
              {moodIndexNumber > 0 ? `+${marketMoodIndex}` : marketMoodIndex}
            </p>
            <p className="text-sm text-gray-500 mt-2">
              A positive value indicates bullish sentiment, while a negative value indicates bearish sentiment.
            </p>
          </div>

          {/* Pie Chart */}
          <div className="p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Sentiment Distribution</h2>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={sentiments}
                  dataKey="value"
                  nameKey="sentiment"
                  cx="50%"
                  cy="50%"
                  outerRadius={100}
                  fill="#8884d8"
                  label={({ sentiment, value }) => `${sentiment}: ${value}%`} // Add a proper label function
                >
                  {sentiments.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  )
}