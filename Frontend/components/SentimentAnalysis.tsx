"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

const sentiments = [
  { text: "RBI's new policy may boost economic growth", sentiment: "Positive" },
  { text: "Global tensions affecting crude oil prices", sentiment: "Negative" },
  { text: "Tech sector showing resilience amid market volatility", sentiment: "Neutral" },
  { text: "Government announces new incentives for startups", sentiment: "Positive" },
  { text: "Inflation concerns grow as consumer prices rise", sentiment: "Negative" },
  { text: "Gold prices touch record high amid global uncertainties", sentiment: "Positive" },
  { text: "IDFC First Bank Q3 Results: Net profit down nearly 53% at Rs 339.4 crore; NII up 14.4%", sentiment: "Negative" },
  { text: "NTPC group eyes continued capacity expansion with approval for thermal and increased renewable energy focus", sentiment: "Positive" },
  { text: "US may put 'very big bounty' on Taliban leaders, says Secretary of State Marco Rubio", sentiment: "Positive" },
]

export default function SentimentAnalysis() {
  const [currentSentiment, setCurrentSentiment] = useState(sentiments[0])

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSentiment((prevSentiment) => {
        const currentIndex = sentiments.indexOf(prevSentiment)
        const nextIndex = (currentIndex + 1) % sentiments.length
        return sentiments[nextIndex]
      })
    }, 10000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="bg-background py-4">
      <div className="container">
        <Card>
          <CardHeader>
            <CardTitle>Market Sentiment Analysis</CardTitle>
            <CardDescription>Real-time analysis of financial news and trends</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-lg mb-2">{currentSentiment.text}</p>
            <p
              className={`font-bold ${
                currentSentiment.sentiment === "Positive"
                  ? "text-green-500"
                  : currentSentiment.sentiment === "Negative"
                    ? "text-red-500"
                    : "text-yellow-500"
              }`}
            >
              Sentiment: {currentSentiment.sentiment}
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}